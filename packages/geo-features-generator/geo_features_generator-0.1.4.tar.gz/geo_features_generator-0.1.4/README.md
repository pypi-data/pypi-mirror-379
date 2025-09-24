geo-features-generator
======================

Генератор гео-признаков в стиле sklearn: расстояния (Haversine, equirectangular, Manhattan), углы/синусы/косинусы, средние точки, дельты, квадраты расстояний, косинусная близость (3D), кластеризация KMeans, расстояния до ближайшего соседа, полярные признаки относительно базовой точки.

Установка
---------

```bash
pip install geo-features-generator
```

Быстрый старт
-------------

```python
import pandas as pd
from geo_features_generator import GeoFeaturesGenerator

df = pd.DataFrame({
    "lat1": [55.75, 59.93],
    "lon1": [37.62, 30.33],
    "lat2": [59.93, 55.75],
    "lon2": [30.33, 37.62],
})

gen = GeoFeaturesGenerator(
    coordinate_pairs=[("lat1", "lon1"), ("lat2", "lon2")],
    enable_squared_distances=True,
    enable_normed_deltas=True,
    enable_cosine_similarity=True,
    enable_kmeans=False,
    enable_nearest_neighbor=False,
    enable_polar_features=True,
    polar_base_point=(55.75, 37.62),
)

features = gen.fit_transform(df)
print(features.head())
```

Параметры
---------

- `coordinate_pairs`: список пар имен столбцов `(lat, lon)`.
- `radius`: радиус сферы (метры), по умолчанию 6_371_000.
- `output_format`: `"pandas"` или `"numpy"`.
- `generate_point_features`: генерировать признаки для каждой точки.
- `generate_pair_features`: генерировать признаки для пар точек.
- `enable_squared_distances`: добавляет `_m2` признаки квадратов расстояний.
- `enable_normed_deltas`: добавляет `abs_dlat_m`, `abs_dlon_m` (в метрах).
- `enable_cosine_similarity`: `cosine_sim`, `cosine_dist` по 3D dot на сфере.
- `enable_kmeans`: добавляет `*_kmeans_label` для каждой точки (требуется scikit-learn).
- `kmeans_n_clusters`, `kmeans_random_state`: параметры KMeans.
- `enable_nearest_neighbor`: добавляет `*_nn_haversine_m` (требуется scikit-learn).
- `enable_polar_features`: добавляет `*_polar_bearing_deg`, `*_polar_dist_m` относительно `polar_base_point`.
- `polar_base_point`: `(lat, lon)` базовой точки.

Контакты
--------

- [![Telegram](https://img.shields.io/badge/Telegram-2CA5E0?style=flat&logo=telegram&logoColor=white)](https://t.me/sefixnep)  
- [![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat&logo=github&logoColor=white)](https://github.com/sefixnep)

Лицензия
--------

MIT. См. файл LICENSE.


