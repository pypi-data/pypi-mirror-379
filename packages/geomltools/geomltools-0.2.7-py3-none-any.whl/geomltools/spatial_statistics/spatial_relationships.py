# spatial_statistics/spatial_relationships.py

import numpy as np
import pandas as pd
from sklearn.neighbors import NearestNeighbors
from scipy.sparse import csr_matrix
from scipy.spatial import distance_matrix
from collections import defaultdict
import warnings


def row_standardize_matrix(matrix):
    """
    Row-standardize a weight matrix so that each row sums to 1.

    Parameters
    ----------
    matrix : numpy.ndarray or scipy.sparse.csr_matrix
        The weight matrix to be row-standardized. This can either be a dense NumPy ndarray 
        or a sparse CSR matrix.

    Returns
    -------
    numpy.ndarray or scipy.sparse.csr_matrix
        The row-standardized matrix, with the same type as the input matrix.
    """
    if isinstance(matrix, csr_matrix):
        # For sparse matrices, row standardization is performed using the .multiply() method
        row_sums = np.array(matrix.sum(axis=1)).flatten()
        row_sums[row_sums == 0] = 1  # Avoid division by zero (in case of rows with zero sum)
        inv_row_sums = 1.0 / row_sums
        return matrix.multiply(inv_row_sums[:, np.newaxis])
    else:
        # For dense matrices, standardization is done using element-wise division
        row_sums = matrix.sum(axis=1)
        row_sums[row_sums == 0] = 1  # Avoid division by zero
        return matrix / row_sums[:, np.newaxis]
    

def assign_grid_cell(coordinates, cell_size):
    """
    Assign grid cell IDs to spatial coordinates based on a specified cell size.

    Supports input as numpy array, pandas DataFrame, GeoPandas, or ESRI SEDF (points only).

    Parameters
    ----------
    coordinates : array-like, pandas.DataFrame, geopandas.GeoDataFrame/GeoSeries, or ESRI SEDF
        Spatial coordinates of the data points, where each point has an (x, y) coordinate.
    cell_size : float
        Size of each square grid cell (e.g., 1000 for 1km x 1km cells). Used to assign grid columns and rows.

    Returns
    -------
    pandas.DataFrame
        DataFrame with columns:
        - 'x', 'y': Original coordinates
        - 'col', 'row': Grid column and row indices
        - 'grid_id': Tuple of (col, row)
    """
    coords = np.asarray(coordinates)
    x_vals, y_vals = coords[:, 0], coords[:, 1]
    cols = (x_vals // cell_size).astype(int)
    rows = (y_vals // cell_size).astype(int)
    grid_ids = list(zip(cols, rows))


    return pd.DataFrame({'x': x_vals,'y': y_vals,'col': cols,'row': rows,'grid_id': grid_ids})


def knn_weight_matrix(coordinates, k=4, row_standardized=False, return_sparse=True, symmetric=True):
    """
    Compute a K-Nearest Neighbors (KNN) spatial weight matrix for points or polygons.

    Supports input as numpy array, pandas DataFrame, GeoPandas, or ESRI SEDF.
    For polygons, centroids are used for neighbor calculation.
    Output format matches input type (GeoPandas, SEDF, Pandas, or NumPy/sparse).

    Parameters
    ----------
    coordinates : array-like, pandas.DataFrame, geopandas.GeoDataFrame/GeoSeries, or ESRI SEDF
        Spatial data as points or polygons.
    k : int, optional
        Number of nearest neighbors to consider (default is 4).
    row_standardized : bool, optional
        If True, rows will be normalized to sum to 1 (default is False).
    return_sparse : bool, optional
        If True, return a sparse CSR matrix; if False, return a dense NumPy array (default is True).
    symmetric : bool, optional
        If True, ensure the matrix is symmetric, i.e., mutual neighbors (default is True).

    Returns
    -------
    Output matches input type:
        - GeoPandas: GeoDataFrame with 'geometry' and 'weight_matrix' columns
        - SEDF: SEDF with 'weight_matrix' column
        - Pandas: DataFrame with 'weight_matrix' column
        - NumPy: sparse or dense weight matrix
    """
    import geopandas as gpd
    from shapely.geometry import Point
    try:
        from arcgis.features import SpatialDataFrame
        has_sedf = True
    except ImportError:
        has_sedf = False

    geoms, input_type, orig = _normalize_geometries(coordinates)
    # Use centroids for polygons
    if not all(isinstance(g, Point) for g in geoms):
        coords = np.array([[geom.centroid.x, geom.centroid.y] for geom in geoms])
    else:
        coords = np.array([[geom.x, geom.y] for geom in geoms])
    n = coords.shape[0]

    # Compute nearest neighbors using NearestNeighbors from sklearn
    nbrs = NearestNeighbors(n_neighbors=k + 1).fit(coords)
    distances, indices = nbrs.kneighbors(coords)

    # Remove the self-neighbor (first column of indices)
    row_indices = np.repeat(np.arange(n), k)
    col_indices = indices[:, 1:(k+1)].reshape(-1)
    data = np.ones(len(row_indices))

    # Build sparse matrix from the neighbor relationships
    W = csr_matrix((data, (row_indices, col_indices)), shape=(n, n))

    # If symmetric, make sure W is symmetric (mutual neighbors)
    if symmetric:
        W = W.maximum(W.T)

    # Row standardization: normalize each row to sum to 1 (if applicable)
    if row_standardized:
        row_sums = np.array(W.sum(axis=1)).flatten()
        row_sums[row_sums == 0] = 1  # Avoid division by zero
        inv_row_sums = 1.0 / row_sums
        W = W.multiply(inv_row_sums[:, np.newaxis])

    # Output conversion
    if input_type == 'geopandas':
        # Return as GeoDataFrame with index matching input
        df = gpd.GeoDataFrame({'geometry': geoms})
        df['weight_matrix'] = [W.getrow(i).toarray().flatten() for i in range(n)]
        return df
    elif input_type == 'sedf' and has_sedf:
        # Convert to SEDF
        gdf = orig.spatial.to_geodataframe()
        gdf['weight_matrix'] = [W.getrow(i).toarray().flatten() for i in range(n)]
        return SpatialDataFrame.from_geodataframe(gdf)
    elif input_type == 'pandas':
        df = orig.copy()
        df['weight_matrix'] = [W.getrow(i).toarray().flatten() for i in range(n)]
        return df
    elif input_type == 'numpy':
        return W if return_sparse else W.toarray()
    else:
        return W if return_sparse else W.toarray()


def distance_band_weight_matrix(coordinates, threshold, row_standardized=False, return_sparse=True, binary=True):
    """
    Compute a spatial weight matrix using a fixed distance band approach for points or polygons.

    Supports input as numpy array, pandas DataFrame, GeoPandas, or ESRI SEDF.
    For polygons, minimum distance between geometries is used.
    Output format matches input type (GeoPandas, SEDF, Pandas, or NumPy/sparse).

    Parameters
    ----------
    coordinates : array-like, pandas.DataFrame, geopandas.GeoDataFrame/GeoSeries, or ESRI SEDF
        Spatial data as points or polygons.
    threshold : float
        Maximum distance to consider neighbors. Pairs of points/polygons with a distance less than 
        or equal to this threshold will be considered neighbors.
    row_standardized : bool, optional
        If True, the rows of the weight matrix will be normalized so that each row sums to 1 (default is False).
    return_sparse : bool, optional
        If True, return a sparse CSR matrix; if False, return a dense NumPy array (default is True).
    binary : bool, optional
        If True, the weight matrix will be binary (1 if within threshold, 0 otherwise). 
        If False, the weights will be inversely proportional to the distance (default is True).

    Returns
    -------
    Output matches input type:
        - GeoPandas: GeoDataFrame with 'geometry' and 'weight_matrix' columns
        - SEDF: SEDF with 'weight_matrix' column
        - Pandas: DataFrame with 'weight_matrix' column
        - NumPy: sparse or dense weight matrix
    """
    import geopandas as gpd
    from shapely.geometry import Point
    try:
        from arcgis.features import SpatialDataFrame
        has_sedf = True
    except ImportError:
        has_sedf = False

    geoms, input_type, orig = _normalize_geometries(coordinates)
    n = len(geoms)
    
    # Non-point geometries fall back to legacy implementation
    if not all(isinstance(geom, Point) for geom in geoms):
        return _distance_band_weight_matrix_legacy(coordinates, threshold, row_standardized, return_sparse, binary)
    
    # Extract coordinates
    coords_array = np.array([[geom.x, geom.y] for geom in geoms])

    # For large datasets, avoid building a dense pairwise distance matrix.
    # Build a sparse radius-neighbors graph directly using BallTree/KDTree.
    # Use distances if non-binary weights are requested; otherwise build a binary graph.
    if n > 5000:
        # Use scikit-learn to construct sparse neighborhood graph efficiently
        nn = NearestNeighbors(radius=threshold, algorithm='ball_tree')
        nn.fit(coords_array)
        mode = 'distance' if not binary else 'connectivity'
        try:
            W_sparse = nn.radius_neighbors_graph(coords_array, radius=threshold, mode=mode)
        except MemoryError:
            # Fallback: use capped k-NN to limit edges and memory
            k_cap = min(100, n - 1)
            nn_k = NearestNeighbors(n_neighbors=k_cap + 1, algorithm='auto')
            nn_k.fit(coords_array)
            W_sparse = nn_k.kneighbors_graph(coords_array, n_neighbors=k_cap + 1, mode=('distance' if not binary else 'connectivity'))
            # Drop self-neighbors (first column)
            # Convert to CSR and zero the diagonal just in case
            W_sparse = W_sparse.tocsr()
            W_sparse.setdiag(0)
            W_sparse.eliminate_zeros()
        # Remove self-neighbors if any exist (they generally do not in radius graph with > 0 radius)
        W_sparse.setdiag(0)
        W_sparse.eliminate_zeros()
        if not binary:
            # Inverse distance weights where distance > 0
            data = W_sparse.data
            nonzero_mask = data > 0
            data[nonzero_mask] = 1.0 / data[nonzero_mask]
            W_sparse.data = data
        # Row standardize if requested
        if row_standardized:
            W_sparse = row_standardize_matrix(W_sparse)
        weights_sparse = W_sparse.tocsr()
    else:
        # Small/medium: compute dense distances then build sparse
        from scipy.spatial import distance_matrix as _dm
        dist_matrix = _dm(coords_array, coords_array)
        mask = (dist_matrix <= threshold) & (dist_matrix > 0)
        rows, cols = np.where(mask)
        if binary:
            data = np.ones(len(rows), dtype=float)
        else:
            data = 1.0 / dist_matrix[rows, cols]
        weights_sparse = csr_matrix((data, (rows, cols)), shape=(n, n))
        if row_standardized:
            weights_sparse = row_standardize_matrix(weights_sparse)

    # Return format
    if return_sparse:
        return weights_sparse
    else:
        return weights_sparse.toarray()


def _distance_band_weight_matrix_legacy(coordinates, threshold, row_standardized=False, return_sparse=True, binary=True):
    """
    Legacy implementation of distance_band_weight_matrix for non-point data.
    This function is kept for backward compatibility with polygon data.
    """
    import geopandas as gpd
    from shapely.geometry import Point
    try:
        from arcgis.features import SpatialDataFrame
        has_sedf = True
    except ImportError:
        has_sedf = False

    geoms, input_type, orig = _normalize_geometries(coordinates)
    n = len(geoms)
    
    # For polygons, use the original approach but with optimizations
    # Pre-allocate the distance matrix
    dist_matrix = np.zeros((n, n))
    
    # Compute pairwise distances between polygons with early termination
    for i in range(n):
        for j in range(i + 1, n):  # Only compute upper triangle
            dist = geoms.iloc[i].distance(geoms.iloc[j])
            dist_matrix[i, j] = dist
            dist_matrix[j, i] = dist  # Symmetric matrix
    
    # Build the weight matrix based on the distance band approach
    if binary:
        # Binary weights: 1 if within the threshold, otherwise 0
        weights = (dist_matrix <= threshold).astype(float)
    else:
        # Inverse distance weights: 1/distance if within threshold, otherwise 0
        with np.errstate(divide='ignore'):
            weights = 1.0 / dist_matrix
        weights[dist_matrix > threshold] = 0
        weights[np.isinf(weights)] = 0  # Handle division by zero
    
    # Remove self-neighbors (set diagonal to zero)
    np.fill_diagonal(weights, 0)

    # Apply row standardization if requested
    if row_standardized:
        weights = row_standardize_matrix(weights)

    # Output conversion
    if input_type == 'geopandas':
        df = gpd.GeoDataFrame({'geometry': geoms})
        df['weight_matrix'] = [weights[i, :] for i in range(n)]
        return df
    elif input_type == 'sedf' and has_sedf:
        gdf = orig.spatial.to_geodataframe()
        gdf['weight_matrix'] = [weights[i, :] for i in range(n)]
        return SpatialDataFrame.from_geodataframe(gdf)
    elif input_type == 'pandas':
        df = orig.copy()
        df['weight_matrix'] = [weights[i, :] for i in range(n)]
        return df
    elif input_type == 'numpy':
        return csr_matrix(weights) if return_sparse else weights
    else:
        return csr_matrix(weights) if return_sparse else weights


def grid_contiguity_weight_matrix(coordinates, cell_size=None, contiguity="rook", row_standardized=False, return_sparse=True):
    """
    Compute a spatial weight matrix using a grid-based contiguity approach for points, or adjacency for polygons.

    Supports input as numpy array, pandas DataFrame, GeoPandas, or ESRI SEDF.
    For points, grid cell contiguity is used (rook/queen). For polygons, adjacency is defined by 'touches' (rook) or 'intersects' (queen).
    Output format matches input type (GeoPandas, SEDF, Pandas, or NumPy/sparse).

    Parameters
    ----------
    coordinates : array-like, pandas.DataFrame, geopandas.GeoDataFrame/GeoSeries, or ESRI SEDF
        Spatial data as points or polygons.
    cell_size : float, optional
        Size of each square grid cell (required for point data).
    contiguity : {'rook', 'queen'}, optional
        Type of contiguity to define neighbors. 
        'rook' considers neighbors sharing an edge (4 directions for points, touches for polygons), 
        'queen' includes edge and corner neighbors (8 directions for points, intersects for polygons). Default is 'rook'.
    row_standardized : bool, optional
        If True, the rows of the weight matrix will be normalized so that each row sums to 1 (default is False).
    return_sparse : bool, optional
        If True, return a sparse CSR matrix; if False, return a dense NumPy array (default is True).

    Returns
    -------
    Output matches input type:
        - GeoPandas: GeoDataFrame with 'geometry' and 'weight_matrix' columns
        - SEDF: SEDF with 'weight_matrix' column
        - Pandas: DataFrame with 'weight_matrix' column
        - NumPy: sparse or dense weight matrix
    """
    import geopandas as gpd
    from shapely.geometry import Point
    try:
        from arcgis.features import SpatialDataFrame
        has_sedf = True
    except ImportError:
        has_sedf = False

    geoms, input_type, orig = _normalize_geometries(coordinates)
    n = len(geoms)

    # If all points, use grid cell logic as before
    if all(isinstance(g, Point) for g in geoms):
        if cell_size is None:
            raise ValueError("cell_size must be provided for point data.")
        coords = np.array([[geom.x, geom.y] for geom in geoms])
        cols = (coords[:, 0] // cell_size).astype(int)
        rows = (coords[:, 1] // cell_size).astype(int)
        grid_ids = list(zip(cols, rows))
        from collections import defaultdict
        cell_to_indices = defaultdict(list)
        for idx, cell in enumerate(grid_ids):
            cell_to_indices[cell].append(idx)
        if contiguity == "rook":
            offsets = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        elif contiguity == "queen":
            offsets = [(-1, -1), (-1, 0), (-1, 1),
                       ( 0, -1),           ( 0, 1),
                       ( 1, -1), ( 1, 0),  ( 1, 1)]
        else:
            raise ValueError("contiguity must be either 'rook' or 'queen'")
        row_idx = []
        col_idx = []
        data = []
        for idx, cell in enumerate(grid_ids):
            neighbors = [tuple(np.add(cell, offset)) for offset in offsets]
            for neighbor in neighbors:
                for j in cell_to_indices.get(neighbor, []):
                    row_idx.append(idx)
                    col_idx.append(j)
                    data.append(1.0)
        W = csr_matrix((data, (row_idx, col_idx)), shape=(n, n))
        if row_standardized:
            W = row_standardize_matrix(W)
    else:
        # For polygons, use adjacency (rook: touches, queen: intersects)
        W = np.zeros((n, n))
        for i in range(n):
            for j in range(n):
                if i != j:
                    if contiguity == "rook":
                        if geoms.iloc[i].touches(geoms.iloc[j]):
                            W[i, j] = 1.0
                    elif contiguity == "queen":
                        if geoms.iloc[i].intersects(geoms.iloc[j]):
                            W[i, j] = 1.0
                    else:
                        raise ValueError("contiguity must be either 'rook' or 'queen'")
        if row_standardized:
            W = row_standardize_matrix(W)
        W = csr_matrix(W) if return_sparse else W

    # Output conversion
    if input_type == 'geopandas':
        df = gpd.GeoDataFrame({'geometry': geoms})
        if isinstance(W, np.ndarray):
            df['weight_matrix'] = [W[i, :] for i in range(n)]
        else:
            df['weight_matrix'] = [W.getrow(i).toarray().flatten() for i in range(n)]
        return df
    elif input_type == 'sedf' and has_sedf:
        gdf = orig.spatial.to_geodataframe()
        if isinstance(W, np.ndarray):
            gdf['weight_matrix'] = [W[i, :] for i in range(n)]
        else:
            gdf['weight_matrix'] = [W.getrow(i).toarray().flatten() for i in range(n)]
        return SpatialDataFrame.from_geodataframe(gdf)
    elif input_type == 'pandas':
        df = orig.copy()
        if isinstance(W, np.ndarray):
            df['weight_matrix'] = [W[i, :] for i in range(n)]
        else:
            df['weight_matrix'] = [W.getrow(i).toarray().flatten() for i in range(n)]
        return df
    elif input_type == 'numpy':
        return W
    else:
        return W


def _normalize_geometries(coordinates):
    """
    Accepts numpy array, pandas DataFrame, GeoPandas, or ESRI SEDF and returns a tuple:
    (GeoPandas GeoSeries of geometries, input_type_str, original_input)
    input_type_str: 'numpy', 'pandas', 'geopandas', 'sedf'
    """
    import geopandas as gpd
    from shapely.geometry import Point, Polygon
    
    # ESRI SEDF
    try:
        from arcgis.features import SpatialDataFrame
        is_sedf = isinstance(coordinates, SpatialDataFrame)
    except ImportError:
        is_sedf = False
    
    # GeoPandas
    if hasattr(coordinates, "geometry"):
        return coordinates.geometry, 'geopandas', coordinates
    
    # ESRI SEDF
    if is_sedf:
        gdf = coordinates.spatial.to_geodataframe()
        return gdf.geometry, 'sedf', coordinates
    
    # Pandas DataFrame with x/y
    if hasattr(coordinates, "columns") and set(["x", "y"]).issubset(coordinates.columns):
        return gpd.GeoSeries([Point(xy) for xy in zip(coordinates["x"], coordinates["y"])]), 'pandas', coordinates
    
    # Numpy array
    arr = np.asarray(coordinates)
    if arr.ndim == 2 and arr.shape[1] == 2:
        return gpd.GeoSeries([Point(xy) for xy in arr]), 'numpy', coordinates
    
    raise ValueError("Unsupported input type for spatial data. Supported: numpy, pandas, geopandas, ESRI SEDF.")