from __future__ import annotations

import numpy as np

_DEG2RAD = np.pi / 180.0
_RAD2DEG = 180.0 / np.pi


def to_radians(values: np.ndarray) -> np.ndarray:
    """Convert degrees to radians if needed.

    If input looks already in radians (abs <= 2*pi), it returns as-is.
    """
    values = np.asarray(values, dtype=float)
    # Heuristic: if max absolute value is > 2*pi, assume degrees
    if np.nanmax(np.abs(values)) > 2.0 * np.pi:
        return values * _DEG2RAD
    return values


def haversine_distance(lat1: np.ndarray, lon1: np.ndarray,
                        lat2: np.ndarray, lon2: np.ndarray,
                        radius: float = 6_371_000.0) -> np.ndarray:
    """Vectorized Haversine distance in meters.

    All angles can be provided in degrees or radians. Auto-detected by `to_radians`.
    """
    lat1 = to_radians(lat1)
    lon1 = to_radians(lon1)
    lat2 = to_radians(lat2)
    lon2 = to_radians(lon2)

    dlat = lat2 - lat1
    dlon = lon2 - lon1

    a = np.sin(dlat / 2.0) ** 2 + np.cos(lat1) * np.cos(lat2) * np.sin(dlon / 2.0) ** 2
    c = 2.0 * np.arctan2(np.sqrt(a), np.sqrt(np.maximum(0.0, 1.0 - a)))
    return radius * c


def equirectangular_distance(lat1: np.ndarray, lon1: np.ndarray,
                             lat2: np.ndarray, lon2: np.ndarray,
                             radius: float = 6_371_000.0) -> np.ndarray:
    """Fast approximate distance using equirectangular projection (meters)."""
    lat1r = to_radians(lat1)
    lon1r = to_radians(lon1)
    lat2r = to_radians(lat2)
    lon2r = to_radians(lon2)

    x = (lon2r - lon1r) * np.cos((lat1r + lat2r) / 2.0)
    y = (lat2r - lat1r)
    return np.sqrt(x * x + y * y) * radius


def manhattan_distance_approx(lat1: np.ndarray, lon1: np.ndarray,
                              lat2: np.ndarray, lon2: np.ndarray,
                              radius: float = 6_371_000.0) -> np.ndarray:
    """Approximate Manhattan distance along parallels/meridians in meters."""
    lat1r = to_radians(lat1)
    lon1r = to_radians(lon1)
    lat2r = to_radians(lat2)
    lon2r = to_radians(lon2)

    dy = np.abs(lat2r - lat1r) * radius
    # meters per radian along parallel depends on latitude (cos(lat))
    avg_lat = (lat1r + lat2r) / 2.0
    dx = np.abs(lon2r - lon1r) * (radius * np.cos(avg_lat))
    return dx + dy


def initial_bearing(lat1: np.ndarray, lon1: np.ndarray,
                    lat2: np.ndarray, lon2: np.ndarray) -> np.ndarray:
    """Initial bearing from point 1 to point 2 in degrees [0, 360)."""
    lat1r = to_radians(lat1)
    lon1r = to_radians(lon1)
    lat2r = to_radians(lat2)
    lon2r = to_radians(lon2)

    dlon = lon2r - lon1r
    y = np.sin(dlon) * np.cos(lat2r)
    x = np.cos(lat1r) * np.sin(lat2r) - np.sin(lat1r) * np.cos(lat2r) * np.cos(dlon)
    brng = np.arctan2(y, x) * _RAD2DEG
    return (brng + 360.0) % 360.0


def midpoint(lat1: np.ndarray, lon1: np.ndarray,
             lat2: np.ndarray, lon2: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    """Geodesic midpoint of two points (degrees)."""
    lat1r = to_radians(lat1)
    lon1r = to_radians(lon1)
    lat2r = to_radians(lat2)
    lon2r = to_radians(lon2)

    dlon = lon2r - lon1r

    bx = np.cos(lat2r) * np.cos(dlon)
    by = np.cos(lat2r) * np.sin(dlon)

    lat_m = np.arctan2(
        np.sin(lat1r) + np.sin(lat2r),
        np.sqrt((np.cos(lat1r) + bx) ** 2 + by ** 2),
    ) * _RAD2DEG
    lon_m = (lon1r + np.arctan2(by, np.cos(lat1r) + bx)) * _RAD2DEG
    return lat_m, ((lon_m + 540.0) % 360.0) - 180.0


def trig_cyclical(lat: np.ndarray, lon: np.ndarray) -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    """Return sin/cos transforms for latitude and longitude.

    Accepts degrees or radians.
    """
    lat_r = to_radians(lat)
    lon_r = to_radians(lon)
    return np.sin(lat_r), np.cos(lat_r), np.sin(lon_r), np.cos(lon_r)


def latlon_to_unit_xyz(lat: np.ndarray, lon: np.ndarray) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Project latitude/longitude to unit sphere Cartesian coordinates.

    Accepts degrees or radians; output are unit vectors (x, y, z).
    """
    lat_r = to_radians(lat)
    lon_r = to_radians(lon)
    cos_lat = np.cos(lat_r)
    x = cos_lat * np.cos(lon_r)
    y = cos_lat * np.sin(lon_r)
    z = np.sin(lat_r)
    return x, y, z


def cosine_similarity_spherical(lat1: np.ndarray, lon1: np.ndarray,
                                lat2: np.ndarray, lon2: np.ndarray) -> np.ndarray:
    """Cosine similarity (dot product) between two points on a unit sphere.

    Returns values in [-1, 1]. Accepts degrees or radians.
    """
    x1, y1, z1 = latlon_to_unit_xyz(lat1, lon1)
    x2, y2, z2 = latlon_to_unit_xyz(lat2, lon2)
    return x1 * x2 + y1 * y2 + z1 * z2


# H3 functions
def lat_lng_to_h3_cell(lat: np.ndarray, lon: np.ndarray, resolution: int) -> np.ndarray:
    """Convert latitude/longitude to H3 cell indices.
    
    Parameters
    ----------
    lat : np.ndarray
        Latitude in degrees
    lon : np.ndarray
        Longitude in degrees  
    resolution : int
        H3 resolution (0-15)
        
    Returns
    -------
    np.ndarray
        Array of H3 cell indices as strings
    """
    try:
        import h3
    except ImportError:
        raise ImportError("Для H3 функций требуется установленная библиотека 'h3'")
    
    # Ensure inputs are numpy arrays
    lat = np.asarray(lat, dtype=float)
    lon = np.asarray(lon, dtype=float)
    
    # Vectorized conversion
    cells = np.array([h3.latlng_to_cell(lat[i], lon[i], resolution) for i in range(len(lat))])
    return cells


def h3_cell_area(cells: np.ndarray) -> np.ndarray:
    """Get area of H3 cells in square meters.
    
    Parameters
    ----------
    cells : np.ndarray
        Array of H3 cell indices as strings
        
    Returns
    -------
    np.ndarray
        Array of cell areas in square meters
    """
    try:
        import h3
    except ImportError:
        raise ImportError("Для H3 функций требуется установленная библиотека 'h3'")
    
    cells = np.asarray(cells)
    areas = np.array([h3.cell_area(cell) for cell in cells])
    return areas


def h3_cell_resolution(cells: np.ndarray) -> np.ndarray:
    """Get resolution of H3 cells.
    
    Parameters
    ----------
    cells : np.ndarray
        Array of H3 cell indices as strings
        
    Returns
    -------
    np.ndarray
        Array of cell resolutions
    """
    try:
        import h3
    except ImportError:
        raise ImportError("Для H3 функций требуется установленная библиотека 'h3'")
    
    cells = np.asarray(cells)
    resolutions = np.array([h3.get_resolution(cell) for cell in cells])
    return resolutions


def h3_neighbors_count(cells: np.ndarray, k: int = 1) -> np.ndarray:
    """Get count of neighbors for H3 cells.
    
    Parameters
    ----------
    cells : np.ndarray
        Array of H3 cell indices as strings
    k : int
        Number of rings around each cell
        
    Returns
    -------
    np.ndarray
        Array of neighbor counts
    """
    try:
        import h3
    except ImportError:
        raise ImportError("Для H3 функций требуется установленная библиотека 'h3'")
    
    cells = np.asarray(cells)
    counts = np.array([len(h3.grid_disk(cell, k=k)) - 1 for cell in cells])  # -1 to exclude self
    return counts


def h3_cell_to_parent(cells: np.ndarray, parent_resolution: int) -> np.ndarray:
    """Get parent H3 cell for given cells.
    
    Parameters
    ----------
    cells : np.ndarray
        Array of H3 cell indices as strings
    parent_resolution : int
        Resolution of parent cells
        
    Returns
    -------
    np.ndarray
        Array of parent cell indices as strings
    """
    try:
        import h3
    except ImportError:
        raise ImportError("Для H3 функций требуется установленная библиотека 'h3'")
    
    cells = np.asarray(cells)
    parents = np.array([h3.cell_to_parent(cell, parent_resolution) for cell in cells])
    return parents


def h3_cell_to_children_count(cells: np.ndarray, child_resolution: int) -> np.ndarray:
    """Get count of children for H3 cells.
    
    Parameters
    ----------
    cells : np.ndarray
        Array of H3 cell indices as strings
    child_resolution : int
        Resolution of child cells
        
    Returns
    -------
    np.ndarray
        Array of children counts
    """
    try:
        import h3
    except ImportError:
        raise ImportError("Для H3 функций требуется установленная библиотека 'h3'")
    
    cells = np.asarray(cells)
    counts = np.array([len(h3.cell_to_children(cell, child_resolution)) for cell in cells])
    return counts


def h3_grid_distance(cells1: np.ndarray, cells2: np.ndarray) -> np.ndarray:
    """Get grid distance between pairs of H3 cells.
    
    Parameters
    ----------
    cells1 : np.ndarray
        Array of first H3 cell indices as strings
    cells2 : np.ndarray
        Array of second H3 cell indices as strings
        
    Returns
    -------
    np.ndarray
        Array of grid distances
    """
    try:
        import h3
    except ImportError:
        raise ImportError("Для H3 функций требуется установленная библиотека 'h3'")
    
    cells1 = np.asarray(cells1)
    cells2 = np.asarray(cells2)
    
    if len(cells1) != len(cells2):
        raise ValueError("cells1 и cells2 должны иметь одинаковую длину")
    
    distances = np.array([h3.grid_distance(cells1[i], cells2[i]) for i in range(len(cells1))])
    return distances