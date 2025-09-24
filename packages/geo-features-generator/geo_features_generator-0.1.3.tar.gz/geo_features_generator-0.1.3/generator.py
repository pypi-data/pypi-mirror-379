from __future__ import annotations

from typing import Iterable, List, Optional, Sequence, Tuple, Union, Dict

import numpy as np

try:
    import pandas as pd  # type: ignore
except Exception:  # pragma: no cover
    pd = None  # type: ignore

from .utils import (
    haversine_distance,
    equirectangular_distance,
    manhattan_distance_approx,
    initial_bearing,
    midpoint,
    trig_cyclical,
    cosine_similarity_spherical,
)


ArrayLike = Union[np.ndarray, "pd.DataFrame"]
Pair = Tuple[str, str]


class GeoFeaturesGenerator:
    """Генератор гео-признаков в стиле sklearn.

    Параметры
    ---------
    coordinate_pairs: list[tuple[str, str]]
        Имена столбцов широты и долготы. Например: [('lat1','lon1'), ('lat2','lon2')].
        Можно передать пары точек любой длины (>=1).
    radius: float
        Радиус сферы для расстояний (метры). По умолчанию 6_371_000.
    output_format: {"numpy", "pandas"}
        Формат выхода. Для 'pandas' требуется pandas и вход как DataFrame.
    generate_point_features: bool
        Генерировать ли признаки для каждой точки (sin/cos, нормализованные и т.п.).
    generate_pair_features: bool
        Генерировать ли признаки для каждой пары точек внутри переданного списка (все комбинации).
    selected_pair_indices: Optional[list[tuple[int, int]]]
        Если задан, ограничивает список пар для комбинаторики (индексы по coordinate_pairs).
    feature_prefix: str
        Префикс имён новых признаков.
    safe_nan: bool
        Заменять ли нечисловые значения на NaN и корректно их обрабатывать.
    """

    def __init__(
        self,
        coordinate_pairs: Sequence[Pair],
        radius: float = 6_371_000.0,
        output_format: str = "pandas",
        generate_point_features: bool = True,
        generate_pair_features: bool = True,
        selected_pair_indices: Optional[Sequence[Tuple[int, int]]] = None,
        feature_prefix: str = "geo",
        safe_nan: bool = True,
        enable_squared_distances: bool = True,
        enable_normed_deltas: bool = True,
        enable_cosine_similarity: bool = True,
        enable_kmeans: bool = False,
        kmeans_n_clusters: int = 20,
        kmeans_random_state: Optional[int] = None,
        enable_nearest_neighbor: bool = False,
        enable_polar_features: bool = False,
        polar_base_point: Optional[Tuple[float, float]] = None,
    ) -> None:
        if not isinstance(coordinate_pairs, Sequence) or len(coordinate_pairs) == 0:
            raise ValueError("coordinate_pairs должен быть непустой последовательностью пар (lat, lon)")
        self.coordinate_pairs: List[Pair] = [(str(a), str(b)) for a, b in coordinate_pairs]
        self.radius = float(radius)
        if output_format not in {"numpy", "pandas"}:
            raise ValueError("output_format должен быть 'numpy' или 'pandas'")
        self.output_format = output_format
        self.generate_point_features = bool(generate_point_features)
        self.generate_pair_features = bool(generate_pair_features)
        self.selected_pair_indices = (
            [(int(i), int(j)) for i, j in selected_pair_indices]
            if selected_pair_indices is not None
            else None
        )
        self.feature_prefix = str(feature_prefix)
        self.safe_nan = bool(safe_nan)
        self._feature_names_out: Optional[List[str]] = None
        # Feature toggles
        self.enable_squared_distances = bool(enable_squared_distances)
        self.enable_normed_deltas = bool(enable_normed_deltas)
        self.enable_cosine_similarity = bool(enable_cosine_similarity)
        self.enable_kmeans = bool(enable_kmeans)
        self.kmeans_n_clusters = int(kmeans_n_clusters)
        self.kmeans_random_state = kmeans_random_state
        self.enable_nearest_neighbor = bool(enable_nearest_neighbor)
        self.enable_polar_features = bool(enable_polar_features)
        self.polar_base_point = polar_base_point
        # Holders for fitted models per point index
        self._kmeans_models: Optional[List[object]] = None
        self._nn_models: Optional[List[object]] = None

    # Совместимость с sklearn
    def fit(self, X: ArrayLike, y: Optional[np.ndarray] = None):  # noqa: D401
        """Ничего не обучает, только проверяет наличие столбцов."""
        Xdf = self._to_dataframe(X)
        self._validate_X(Xdf)
        # Fit optional models
        if self.enable_kmeans:
            try:
                from sklearn.cluster import KMeans  # type: ignore
            except Exception as exc:  # pragma: no cover
                raise RuntimeError("Для enable_kmeans=True требуется scikit-learn") from exc
            self._kmeans_models = []
            for lat_col, lon_col in self.coordinate_pairs:
                coords = np.column_stack([
                    Xdf[lat_col].to_numpy(dtype=float),
                    Xdf[lon_col].to_numpy(dtype=float),
                ])
                model = KMeans(n_clusters=self.kmeans_n_clusters, n_init="auto", random_state=self.kmeans_random_state)
                model.fit(coords)
                self._kmeans_models.append(model)
        else:
            self._kmeans_models = None

        if self.enable_nearest_neighbor:
            try:
                from sklearn.neighbors import NearestNeighbors  # type: ignore
            except Exception as exc:  # pragma: no cover
                raise RuntimeError("Для enable_nearest_neighbor=True требуется scikit-learn") from exc
            self._nn_models = []
            # Use haversine metric on radians
            for lat_col, lon_col in self.coordinate_pairs:
                lat = Xdf[lat_col].to_numpy(dtype=float)
                lon = Xdf[lon_col].to_numpy(dtype=float)
                lat_r = np.deg2rad(lat)
                lon_r = np.deg2rad(lon)
                coords_r = np.column_stack([lat_r, lon_r])
                # n_neighbors=2 to skip self (distance 0), then take the second
                nn = NearestNeighbors(n_neighbors=min(2, len(coords_r)), metric="haversine")
                nn.fit(coords_r)
                self._nn_models.append(nn)
        else:
            self._nn_models = None

        self._feature_names_out = self._build_feature_names(Xdf)
        return self

    def fit_transform(self, X: ArrayLike, y: Optional[np.ndarray] = None):
        self.fit(X, y)
        return self.transform(X)

    def transform(self, X: ArrayLike) -> ArrayLike:
        df_mode = self.output_format == "pandas"
        Xdf = self._to_dataframe(X) if df_mode else self._to_dataframe(X, copy=False)

        # Сбор всех новых признаков
        features: Dict[str, np.ndarray] = {}

        # Признаки для каждой точки
        if self.generate_point_features:
            for idx, (lat_col, lon_col) in enumerate(self.coordinate_pairs):
                lat = Xdf[lat_col].to_numpy(dtype=float)
                lon = Xdf[lon_col].to_numpy(dtype=float)

                sin_lat, cos_lat, sin_lon, cos_lon = trig_cyclical(lat, lon)
                base = f"{self.feature_prefix}_p{idx}"
                features[f"{base}_sin_lat"] = sin_lat
                features[f"{base}_cos_lat"] = cos_lat
                features[f"{base}_sin_lon"] = sin_lon
                features[f"{base}_cos_lon"] = cos_lon
                # Дельты к нулю — просто нормализация
                features[f"{base}_lat"] = lat.astype(float)
                features[f"{base}_lon"] = lon.astype(float)

                # Полярные признаки относительно базовой точки
                if self.enable_polar_features and self.polar_base_point is not None:
                    base_lat0, base_lon0 = self.polar_base_point
                    # Угол от базовой точки к текущей
                    pol_bearing = initial_bearing(base_lat0 * np.ones_like(lat), base_lon0 * np.ones_like(lon), lat, lon)
                    pol_dist = haversine_distance(base_lat0 * np.ones_like(lat), base_lon0 * np.ones_like(lon), lat, lon, radius=self.radius)
                    features[f"{base}_polar_bearing_deg"] = pol_bearing
                    features[f"{base}_polar_dist_m"] = pol_dist

                # KMeans кластеры по координатам
                if self.enable_kmeans:
                    if not self._kmeans_models:
                        raise RuntimeError("KMeans модели не обучены. Вызовите fit перед transform.")
                    model = self._kmeans_models[idx]
                    coords = np.column_stack([lat, lon])
                    labels = model.predict(coords)
                    features[f"{base}_kmeans_label"] = labels.astype(float)

                # Ближайший сосед (NN) по Haversine
                if self.enable_nearest_neighbor:
                    if not self._nn_models:
                        raise RuntimeError("NN модели не обучены. Вызовите fit перед transform.")
                    nn = self._nn_models[idx]
                    lat_r = np.deg2rad(lat)
                    lon_r = np.deg2rad(lon)
                    coords_r = np.column_stack([lat_r, lon_r])
                    # kneighbors: returns distances in radians for haversine metric
                    distances_r, indices = nn.kneighbors(coords_r, n_neighbors=min(2, len(coords_r)), return_distance=True)
                    if distances_r.shape[1] == 1:
                        nn_m = distances_r[:, 0] * self.radius
                    else:
                        nn_m = distances_r[:, 1] * self.radius  # skip self
                    features[f"{base}_nn_haversine_m"] = nn_m

        # Признаки для пар точек (полная комбинаторика или подмножество)
        if self.generate_pair_features:
            indices: List[Tuple[int, int]]
            if self.selected_pair_indices is not None:
                indices = list(self.selected_pair_indices)
            else:
                k = len(self.coordinate_pairs)
                indices = [(i, j) for i in range(k) for j in range(i + 1, k)]

            for (i, j) in indices:
                lat1_col, lon1_col = self.coordinate_pairs[i]
                lat2_col, lon2_col = self.coordinate_pairs[j]

                lat1 = Xdf[lat1_col].to_numpy(dtype=float)
                lon1 = Xdf[lon1_col].to_numpy(dtype=float)
                lat2 = Xdf[lat2_col].to_numpy(dtype=float)
                lon2 = Xdf[lon2_col].to_numpy(dtype=float)

                base = f"{self.feature_prefix}_p{i}p{j}"

                # Геодезические расстояния
                dist_h = haversine_distance(lat1, lon1, lat2, lon2, radius=self.radius)
                dist_eq = equirectangular_distance(lat1, lon1, lat2, lon2, radius=self.radius)
                dist_mh = manhattan_distance_approx(lat1, lon1, lat2, lon2, radius=self.radius)

                features[f"{base}_haversine_m"] = dist_h
                features[f"{base}_equirect_m"] = dist_eq
                features[f"{base}_manhattan_m"] = dist_mh

                # Квадраты расстояний
                if self.enable_squared_distances:
                    features[f"{base}_haversine_m2"] = dist_h ** 2
                    features[f"{base}_equirect_m2"] = dist_eq ** 2
                    features[f"{base}_manhattan_m2"] = dist_mh ** 2

                # Азимуты и их синусы/косинусы
                brng = initial_bearing(lat1, lon1, lat2, lon2)
                features[f"{base}_bearing_deg"] = brng
                # циклические компоненты угла
                brng_rad = np.deg2rad(brng)
                features[f"{base}_sin_bearing"] = np.sin(brng_rad)
                features[f"{base}_cos_bearing"] = np.cos(brng_rad)

                # Средняя точка
                mid_lat, mid_lon = midpoint(lat1, lon1, lat2, lon2)
                features[f"{base}_mid_lat"] = mid_lat
                features[f"{base}_mid_lon"] = mid_lon

                # Разности по широте/долготе
                dlat = (lat2 - lat1)
                dlon = (lon2 - lon1)
                features[f"{base}_dlat"] = dlat
                features[f"{base}_dlon"] = dlon

                if self.enable_normed_deltas:
                    # В радианы и в метры по меридиану/параллели
                    lat1r = np.deg2rad(lat1)
                    lat2r = np.deg2rad(lat2)
                    dlat_r = np.abs(lat2r - lat1r)
                    avg_lat_r = (lat1r + lat2r) / 2.0
                    dlon_r = np.abs(np.deg2rad(dlon))
                    dlat_m = dlat_r * self.radius
                    dlon_m = dlon_r * (self.radius * np.cos(avg_lat_r))
                    features[f"{base}_abs_dlat_m"] = dlat_m
                    features[f"{base}_abs_dlon_m"] = dlon_m

                if self.enable_cosine_similarity:
                    cos_sim = cosine_similarity_spherical(lat1, lon1, lat2, lon2)
                    features[f"{base}_cosine_sim"] = cos_sim
                    features[f"{base}_cosine_dist"] = 1.0 - cos_sim

        # Строим выход
        feature_names = list(features.keys())
        data = np.column_stack([features[name] for name in feature_names]) if feature_names else np.empty((len(Xdf), 0))

        if df_mode:
            assert pd is not None
            return pd.DataFrame(data, index=Xdf.index, columns=feature_names)
        else:
            return data

    def get_feature_names_out(self, input_features: Optional[Sequence[str]] = None) -> List[str]:
        if self._feature_names_out is not None:
            return self._feature_names_out
        # Если fit не вызывался — построим по умолчанию
        self._feature_names_out = self._build_feature_names(None)
        return self._feature_names_out

    # ----- Внутренние утилиты -----
    def _to_dataframe(self, X: ArrayLike, copy: bool = True):
        if pd is None:
            raise RuntimeError("Для output_format='pandas' требуется установленный pandas")
        if isinstance(X, np.ndarray):
            # Нет имен столбцов — используем индексы по coordinate_pairs
            cols = []
            for lat, lon in self.coordinate_pairs:
                cols.extend([lat, lon])
            if X.shape[1] < len(cols):
                raise ValueError("Число столбцов в массиве меньше требуемых coordinate_pairs")
            data = {col: X[:, i] for i, col in enumerate(cols)}
            return pd.DataFrame(data).copy() if copy else pd.DataFrame(data)
        elif pd is not None and isinstance(X, pd.DataFrame):
            return X.copy() if copy else X
        else:
            raise TypeError("X должен быть numpy.ndarray или pandas.DataFrame")

    def _validate_X(self, X: ArrayLike) -> None:
        Xdf = self._to_dataframe(X)
        for lat_col, lon_col in self.coordinate_pairs:
            if lat_col not in Xdf.columns or lon_col not in Xdf.columns:
                raise ValueError(f"Отсутствуют столбцы '{lat_col}' и/или '{lon_col}' в X")

    def _build_feature_names(self, X: Optional[ArrayLike]) -> List[str]:
        names: List[str] = []
        if self.generate_point_features:
            for idx, _ in enumerate(self.coordinate_pairs):
                base = f"{self.feature_prefix}_p{idx}"
                names.extend([
                    f"{base}_sin_lat",
                    f"{base}_cos_lat",
                    f"{base}_sin_lon",
                    f"{base}_cos_lon",
                    f"{base}_lat",
                    f"{base}_lon",
                ])
                if self.enable_polar_features and self.polar_base_point is not None:
                    names.extend([
                        f"{base}_polar_bearing_deg",
                        f"{base}_polar_dist_m",
                    ])
                if self.enable_kmeans:
                    names.append(f"{base}_kmeans_label")
                if self.enable_nearest_neighbor:
                    names.append(f"{base}_nn_haversine_m")
        if self.generate_pair_features:
            if self.selected_pair_indices is not None:
                indices = list(self.selected_pair_indices)
            else:
                k = len(self.coordinate_pairs)
                indices = [(i, j) for i in range(k) for j in range(i + 1, k)]
            for (i, j) in indices:
                base = f"{self.feature_prefix}_p{i}p{j}"
                names.extend([
                    f"{base}_haversine_m",
                    f"{base}_equirect_m",
                    f"{base}_manhattan_m",
                    f"{base}_bearing_deg",
                    f"{base}_sin_bearing",
                    f"{base}_cos_bearing",
                    f"{base}_mid_lat",
                    f"{base}_mid_lon",
                    f"{base}_dlat",
                    f"{base}_dlon",
                ])
                if self.enable_squared_distances:
                    names.extend([
                        f"{base}_haversine_m2",
                        f"{base}_equirect_m2",
                        f"{base}_manhattan_m2",
                    ])
                if self.enable_normed_deltas:
                    names.extend([
                        f"{base}_abs_dlat_m",
                        f"{base}_abs_dlon_m",
                    ])
                if self.enable_cosine_similarity:
                    names.extend([
                        f"{base}_cosine_sim",
                        f"{base}_cosine_dist",
                    ])
        return names
