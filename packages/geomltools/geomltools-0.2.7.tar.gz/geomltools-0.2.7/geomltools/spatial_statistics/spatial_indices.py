import numpy as np
import pandas as pd
import warnings
from scipy.stats import norm
from scipy.spatial.distance import cdist
from scipy.spatial import ConvexHull
from sklearn.neighbors import NearestNeighbors
from .spatial_relationships import knn_weight_matrix
from .spatial_relationships import distance_band_weight_matrix
from .spatial_relationships import grid_contiguity_weight_matrix


def _validate_and_convert_input(data, variable=None):
    """
    Validate and convert different input types to standardized format for spatial analysis.
    
    Parameters
    ----------
    data : array-like, pandas.DataFrame, geopandas.GeoDataFrame/GeoSeries, or ESRI SEDF
        Input spatial data. Can be:
        - Array-like: 2D array with coordinates and values
        - pandas.DataFrame: DataFrame with coordinate columns and variable column
        - geopandas.GeoDataFrame/GeoSeries: GeoPandas object with geometry column
        - ESRI SEDF: Spatially enabled DataFrame with 'SHAPE' column
    variable : str, optional
        Name of the variable column (required for DataFrame inputs)
    
    Returns
    -------
    tuple
        (coords, values, n) where:
        - coords: numpy.ndarray of shape (n, 2) with x,y coordinates
        - values: numpy.ndarray of shape (n,) with variable values
        - n: int, number of observations
    
    Raises
    ------
    ValueError
        If input format is not supported or required parameters are missing
    TypeError
        If input type is not recognized
    """
    # Handle ESRI SEDF (Spatially Enabled DataFrame)
    if hasattr(data, 'spatial') and hasattr(data, 'SHAPE'):
        coords = np.array([[geom.x, geom.y] for geom in data['SHAPE']])
        n = len(coords)
        
        if variable is not None:
            if variable not in data.columns:
                raise ValueError(f"Variable '{variable}' not found in DataFrame columns")
            values = np.asarray(data[variable].values)
        else:
            # For geometry-only calculations, create dummy values
            values = np.ones(n)
        
    # Handle GeoPandas GeoDataFrame/GeoSeries
    elif hasattr(data, 'geometry') and hasattr(data, 'crs'):
        # Extract coordinates from geometry
        if hasattr(data.geometry.iloc[0], 'x'):  # Point geometries
            coords = np.array([[geom.x, geom.y] for geom in data.geometry])
        else:
            # For non-point geometries, use centroids
            coords = np.array([[geom.centroid.x, geom.centroid.y] for geom in data.geometry])
        
        n = len(coords)
        
        if variable is not None:
            if variable not in data.columns:
                raise ValueError(f"Variable '{variable}' not found in GeoDataFrame columns")
            values = np.asarray(data[variable].values)
        else:
            # For geometry-only calculations, create dummy values
            values = np.ones(n)
        
    # Handle pandas DataFrame
    elif isinstance(data, pd.DataFrame):
        # Check for common coordinate column names
        coord_cols = None
        for x_col, y_col in [('x', 'y'), ('X', 'Y'), ('longitude', 'latitude'), 
                            ('lon', 'lat'), ('lng', 'lat'), ('LONGITUDE', 'LATITUDE')]:
            if x_col in data.columns and y_col in data.columns:
                coord_cols = (x_col, y_col)
                break
        
        if coord_cols is None:
            raise ValueError("Could not find coordinate columns. Expected pairs like (x,y), (X,Y), (longitude,latitude), etc.")
        
        x_col, y_col = coord_cols
        coords = np.column_stack([data[x_col].values, data[y_col].values])
        n = len(coords)
        
        if variable is not None:
            if variable not in data.columns:
                raise ValueError(f"Variable '{variable}' not found in DataFrame columns")
            values = np.asarray(data[variable].values)
        else:
            # For geometry-only calculations, create dummy values
            values = np.ones(n)
        
    # Handle array-like input
    elif hasattr(data, '__array__'):
        data_array = np.asarray(data)
        
        if data_array.ndim == 1:
            # 1D array - assume it's just values, need coordinates separately
            raise ValueError("1D array provided but coordinates are required. Use DataFrame format with coordinate columns.")
        elif data_array.ndim == 2:
            if data_array.shape[1] < 3:
                raise ValueError("2D array must have at least 3 columns: x, y, and variable values")
            
            # Assume first two columns are x,y coordinates, third column is variable
            coords = data_array[:, :2]
            values = data_array[:, 2]
            n = len(values)
        else:
            raise ValueError("Array must be 1D or 2D")
            
    else:
        raise TypeError(f"Unsupported input type: {type(data)}. Expected array-like, pandas.DataFrame, geopandas.GeoDataFrame, or ESRI SEDF.")
    
    # Validate the extracted data
    if n == 0:
        raise ValueError("Input data is empty")
    
    if coords.shape[0] != n:
        raise ValueError("Mismatch between number of coordinates and values")
    
    if np.any(np.isnan(coords)):
        raise ValueError("NaN values found in coordinates")
    
    if np.any(np.isnan(values)):
        warnings.warn("NaN values found in variable data. These will be handled by the analysis function.")
    
    return coords, values, n


def calculate_pvalue(observed_statistic, shuffled_statistics):
    """
    Calculate the p-value of an observed statistic using shuffled statistics.
    
    Parameters:
        observed_statistic (float): The observed value of the statistic.
        shuffled_statistics (np.array): Array of statistics calculated from shuffled data.
    
    Returns:
        pvalue (float): The p-value.
    """
    # Calculate the p-value using SciPy's percentileofscore
    z_score = (observed_statistic - np.array(shuffled_statistics).mean() ) / np.array(shuffled_statistics).std()
    p_value = 2 * (1 - norm.cdf(np.abs(z_score)))
    return p_value


def test_spatial_index_significance(data, variable=None, index_func=None, permutations=999, seed=None, early_termination=True, batch_size=100, **kwargs):
    """
    Generic significance test for any spatial index using Monte Carlo permutations.
    
    Optimized implementation with key features:
    1. Pre-computes spatial weight matrices once
    2. Uses vectorized operations where possible
    3. Implements early termination for clear significance
    4. Processes permutations in batches
    5. Avoids DataFrame reassignment overhead
    
    Parameters
    ----------
    data : array-like, pandas.DataFrame, geopandas.GeoDataFrame/GeoSeries, or ESRI SEDF
        Input spatial data. Can be:
        - Array-like: 2D array with coordinates (first 2 columns) and values (3rd column)
        - pandas.DataFrame: DataFrame with coordinate columns and variable column
        - geopandas.GeoDataFrame/GeoSeries: GeoPandas object with geometry column
        - ESRI SEDF: Spatially enabled DataFrame with 'SHAPE' column
    variable : str, optional
        Name of the variable to analyze. Required for DataFrame/GeoDataFrame/SEDF inputs.
        For array-like inputs, the variable is assumed to be in the 3rd column.
    index_func : callable
        Function to compute the spatial index. Must accept data, variable, and **kwargs.
    permutations : int
        Number of permutations to perform.
    seed : int or None
        Seed for reproducibility.
    early_termination : bool, optional
        If True, stop early if significance is clear (default is True).
    batch_size : int, optional
        Number of permutations to process in each batch (default is 100).
    **kwargs : dict
        Keyword arguments to pass to the index function.

    Returns
    -------
    tuple
        (p_value, dict)
        p_value : float
            The p-value of the significance test
        dict : dict
            {
                'observed': float,
                'permuted': np.ndarray,
                'p_value': float,
                'z_score': float,
                'permutations_used': int
            }
    """
    if seed is not None:
        np.random.seed(seed)

    # Compute the observed index value
    observed = index_func(data, variable, **kwargs)
    
    # Extract coordinates and values once using the validation function
    coords, original_values, n = _validate_and_convert_input(data, variable)
    original_values = original_values.copy()
    
    # Pre-compute weight matrix if the function supports it
    weights = None
    if 'weights' in kwargs:
        weights = kwargs['weights']
    elif 'method' in kwargs:
        # Pre-compute weight matrix based on method
        method = kwargs.get('method', 'knn')
        if method == 'knn':
            k = kwargs.get('k', 4)
            weights = knn_weight_matrix(coords, k=k, 
                                      row_standardized=kwargs.get('row_standardized', False),
                                      return_sparse=True, 
                                      symmetric=kwargs.get('symmetric', True))
        elif method == 'distance_band':
            threshold = kwargs.get('threshold')
            if threshold is None:
                raise ValueError("threshold must be specified for distance_band method")
            weights = distance_band_weight_matrix(coords, threshold=threshold,
                                                row_standardized=kwargs.get('row_standardized', False),
                                                return_sparse=True,
                                                binary=kwargs.get('binary', True))
        elif method == 'grid':
            cell_size = kwargs.get('cell_size')
            if cell_size is None:
                raise ValueError("cell_size must be specified for grid method")
            weights = grid_contiguity_weight_matrix(coords, cell_size=cell_size,
                                                  contiguity=kwargs.get('contiguity', 'rook'),
                                                  row_standardized=kwargs.get('row_standardized', False),
                                                  return_sparse=True)
    
    # Create kwargs with pre-computed weights
    optimized_kwargs = kwargs.copy()
    if weights is not None:
        optimized_kwargs['weights'] = weights
    
    # Process permutations in batches for better memory management
    permuted_stats = []
    permutations_used = 0
    
    for batch_start in range(0, permutations, batch_size):
        batch_end = min(batch_start + batch_size, permutations)
        batch_size_actual = batch_end - batch_start
        
        # Generate permutations for this batch
        batch_permutations = np.array([
            np.random.permutation(original_values) 
            for _ in range(batch_size_actual)
        ])
        
        # Process batch
        batch_stats = []
        for i in range(batch_size_actual):
            # Create temporary data with permuted values
            if hasattr(data, 'spatial') and hasattr(data, 'SHAPE'):
                # ESRI SEDF case
                temp_data = data.copy()
                temp_data[variable] = batch_permutations[i]
            elif hasattr(data, 'geometry') and hasattr(data, 'crs'):
                # GeoPandas case
                temp_data = data.copy()
                temp_data[variable] = batch_permutations[i]
            elif isinstance(data, pd.DataFrame):
                # pandas DataFrame case
                temp_data = data.copy()
                temp_data[variable] = batch_permutations[i]
            else:
                # Array-like case - create new array with permuted values
                temp_data = data.copy()
                temp_data[:, 2] = batch_permutations[i]
            
            # Compute index for this permutation
            try:
                stat = index_func(temp_data, variable, **optimized_kwargs)
                batch_stats.append(stat)
            except Exception as e:
                # Handle any errors in individual permutations
                print(f"Warning: Error in permutation {permutations_used + i}: {e}")
                batch_stats.append(np.nan)
        
        batch_stats = np.array(batch_stats)
        permuted_stats.extend(batch_stats)
        permutations_used += batch_size_actual
        
        # Early termination check
        if early_termination and permutations_used >= 100:
            batch_array = np.array(permuted_stats)
            if not np.any(np.isnan(batch_array)):
                # Check if significance is clear
                temp_p_value = calculate_pvalue(observed, batch_array)
                if temp_p_value < 0.01 or temp_p_value > 0.99:
                    print(f"Early termination: Clear significance detected after {permutations_used} permutations")
                    break
    
    permuted_stats = np.array(permuted_stats)
    
    # Remove any NaN values
    valid_stats = permuted_stats[~np.isnan(permuted_stats)]
    if len(valid_stats) == 0:
        return np.nan, {
            'observed': observed,
            'permuted': permuted_stats,
            'p_value': np.nan,
            'z_score': np.nan,
            'permutations_used': permutations_used
        }
    
    # Compute z-score and p-value
    mean_perm = np.array(valid_stats).mean()
    std_perm = np.array(valid_stats).std()
    z_score = (observed - mean_perm) / std_perm if std_perm not in (0, 0.0) else np.nan
    p_value = 2 * (1 - norm.cdf(np.abs(z_score))) if not np.isnan(z_score) else np.nan
    
    return p_value, {
        'observed': observed,
        'permuted': permuted_stats,
        'p_value': p_value,
        'z_score': z_score,
        'permutations_used': permutations_used
    }





def coefficient_of_variation_of_local_variance(data, variable=None, weights=None, method='knn', 
                                              k=4, threshold=None, cell_size=None, contiguity="rook",
                                              row_standardized=False, symmetric=True, binary=True, analytical=False):
    """
    Calculate the Coefficient of Variation of Local Variance (CVLV) using various spatial weight matrix methods.

    Parameters
    ----------
    data : array-like, pandas.DataFrame, geopandas.GeoDataFrame/GeoSeries, or ESRI SEDF
        Input spatial data. Can be:
        - Array-like: 2D array with coordinates (first 2 columns) and values (3rd column)
        - pandas.DataFrame: DataFrame with coordinate columns and variable column
        - geopandas.GeoDataFrame/GeoSeries: GeoPandas object with geometry column
        - ESRI SEDF: Spatially enabled DataFrame with 'SHAPE' column
    variable : str, optional
        Name of the variable to analyze. Required for DataFrame/GeoDataFrame/SEDF inputs.
        For array-like inputs, the variable is assumed to be in the 3rd column.
    weights : scipy.sparse.csr_matrix or None, optional
        Pre-computed spatial weights matrix. If None, weights will be calculated.
    method : str, optional
        Method for constructing spatial weights:
        - 'knn': K-nearest neighbors
        - 'distance_band': Fixed distance band
        - 'grid': Grid-based contiguity
        Default is 'knn'.
    k : int, optional
        Number of nearest neighbors for KNN method (default is 4).
    threshold : float, optional
        Distance threshold for distance band method.
    cell_size : float, optional
        Grid cell size for grid contiguity method.
    contiguity : str, optional
        Type of contiguity for grid method ('rook' or 'queen', default is 'rook').
    row_standardized : bool, optional
        Whether to row-standardize the weight matrix (default is False).
    symmetric : bool, optional
        Whether to ensure symmetry in the weight matrix (default is True).
    binary : bool, optional
        If True, use binary weights (1 if within threshold, 0 otherwise) for distance_band method.
        If False, use inverse distance weights (default is True).
    analytical : bool, optional
        If True, return a tuple (CVLV, z_score, p_value) using analytical approximation.
        If False (default), return only the CVLV value.

    Returns
    -------
    float or tuple
        - If analytical is False: CVLV statistic (float). Returns np.nan if calculation fails.
        - If analytical is True: (CVLV, z_score, p_value) where p_value is two-sided analytical p-value.

    Notes
    -----
    The CVLV measures the spatial heterogeneity of local variances by computing the coefficient
    of variation (standard deviation / mean) of local variances across neighborhoods.
    
    Interpretation:
    - High CVLV (> 0.5): High spatial heterogeneity in local variances
    - Medium CVLV (0.2-0.5): Moderate spatial heterogeneity
    - Low CVLV (< 0.2): Low spatial heterogeneity, more uniform local variances
    
    The CVLV is more robust than simple variance ratios and is widely used in spatial statistics
    for detecting spatial non-stationarity and heterogeneity patterns.
    
    Analytical Significance Testing:
    When analytical=True, the function tests the null hypothesis that local variances are 
    spatially homogeneous (CVLV = 0). The z-score and p-value are computed using an 
    approximation based on coefficient of variation theory adapted for spatial context.
    This provides a quick analytical assessment, though permutation testing may be more 
    appropriate for complex spatial patterns.
    """
    # Validate and convert input to standardized format
    coords, values, n = _validate_and_convert_input(data, variable)
    
    if weights is None:
        if method == 'knn':
            W = knn_weight_matrix(coords, k=k, row_standardized=row_standardized,
                                return_sparse=True, symmetric=symmetric)
        elif method == 'distance_band':
            if threshold is None:
                raise ValueError("threshold must be specified for distance_band method")
            W = distance_band_weight_matrix(coords, threshold=threshold,
                                          row_standardized=row_standardized,
                                          return_sparse=True, binary=binary)
        elif method == 'grid':
            if cell_size is None:
                raise ValueError("cell_size must be specified for grid method")
            W = grid_contiguity_weight_matrix(coords, cell_size=cell_size,
                                            contiguity=contiguity,
                                            row_standardized=row_standardized,
                                            return_sparse=True)
        else:
            raise ValueError(f"Method '{method}' not supported. Use 'knn', 'distance_band', or 'grid'")
    else:
        W = weights
        
    # Compute local variances
    local_variances = []
    for i in range(n):
        neighbors = W[i].nonzero()[1]
        if len(neighbors) == 0:
            continue
        neighbor_values = values[neighbors]
        var = np.var(neighbor_values, ddof=1)
        local_variances.append(var)

    if not local_variances:
        return np.nan

    local_variances = np.array(local_variances)
    
    # Calculate CVLV: coefficient of variation of local variances
    mean_local_variance = np.mean(local_variances)
    std_local_variance = np.std(local_variances, ddof=1)
    
    cvlv = std_local_variance / mean_local_variance if mean_local_variance != 0 else np.nan
    
    if analytical:
        # Analytical approach for CVLV significance testing
        # Based on coefficient of variation theory adapted for spatial context
        if np.isnan(cvlv) or len(local_variances) < 3:
            return cvlv, np.nan, np.nan
            
        # For CVLV, we test against the null hypothesis that local variances are homogeneous
        # Under spatial randomness, we expect CVLV ≈ 0 (no spatial heterogeneity)
        n_local = len(local_variances)
        
        # Standard error approximation for coefficient of variation
        # This is adapted from standard CV theory for the spatial context
        se_cvlv = cvlv / np.sqrt(2 * n_local) if cvlv != 0 else np.nan
        
        if np.isnan(se_cvlv) or se_cvlv == 0:
            return cvlv, np.nan, np.nan
            
        # Z-score: test against null hypothesis CVLV = 0 (no spatial heterogeneity)
        z_score = cvlv / se_cvlv
        
        # Two-sided p-value
        p_value = 2 * (1 - norm.cdf(np.abs(z_score))) if not np.isnan(z_score) else np.nan
        
        return cvlv, z_score, p_value
    
    return cvlv


def morans_i(data, variable=None, weights=None, method='distance_band',
             k=4, threshold=None, cell_size=None, contiguity="rook",
             row_standardized=True, symmetric=True, binary=True, analytical=False):
    """
    Calculate Moran's I statistic for spatial autocorrelation using various weight matrix methods.

    Parameters
    ----------
    data : array-like, pandas.DataFrame, geopandas.GeoDataFrame/GeoSeries, or ESRI SEDF
        Input spatial data. Can be:
        - Array-like: 2D array with coordinates (first 2 columns) and values (3rd column)
        - pandas.DataFrame: DataFrame with coordinate columns and variable column
        - geopandas.GeoDataFrame/GeoSeries: GeoPandas object with geometry column
        - ESRI SEDF: Spatially enabled DataFrame with 'SHAPE' column
    variable : str, optional
        Name of the variable to analyze. Required for DataFrame/GeoDataFrame/SEDF inputs.
        For array-like inputs, the variable is assumed to be in the 3rd column.
    weights : scipy.sparse.csr_matrix or None, optional
        Pre-computed spatial weights matrix. If None, weights will be calculated.
    method : str, optional
        Method for constructing spatial weights:
        - 'knn': K-nearest neighbors
        - 'distance_band': Fixed distance band
        - 'grid': Grid-based contiguity
        Default is 'distance_band'.
    k : int, optional
        Number of nearest neighbors for KNN method (default is 4).
    threshold : float, optional
        Distance threshold for distance band method.
    cell_size : float, optional
        Grid cell size for grid contiguity method.
    contiguity : str, optional
        Type of contiguity for grid method ('rook' or 'queen', default is 'rook').
    row_standardized : bool, optional
        Whether to row-standardize the weight matrix (default is True for Moran's I).
    symmetric : bool, optional
        Whether to ensure symmetry in the weight matrix (default is True).
    binary : bool, optional
        If True, use binary weights (1 if within threshold, 0 otherwise) for distance_band method.
        If False, use inverse distance weights (default is True).
    analytical : bool, optional
        If True, return a tuple (I, p_value, z_score) using a normal approximation under randomization.
        If False (default), return only the Moran's I value.

    Returns
    -------
    float or tuple
        - If analytical is False: Moran's I statistic (float).
        - If analytical is True: (I, p_value, z_score) where p_value is two-sided analytical p-value.

    Raises
    ------
    ValueError
        If all values are identical (zero variance) or if required parameters are missing.

    Notes
    -----
    Moran's I interpretation:
    - I > E[I]: Positive spatial autocorrelation
    - I ≈ E[I]: No spatial autocorrelation
    - I < E[I]: Negative spatial autocorrelation
    Expected value E[I] = -1/(n-1) where n is number of observations
    """
    # Validate and convert input to standardized format
    coords, X, n = _validate_and_convert_input(data, variable)
    
    if weights is None:
        if method == 'knn':
            W = knn_weight_matrix(coords, k=k, row_standardized=row_standardized,
                               return_sparse=True, symmetric=symmetric)
        elif method == 'distance_band':
            if threshold is None:
                raise ValueError("threshold must be specified for distance_band method")
            W = distance_band_weight_matrix(coords, threshold=threshold,
                                          row_standardized=row_standardized,
                                          return_sparse=True, binary=binary)
        elif method == 'grid':
            if cell_size is None:
                raise ValueError("cell_size must be specified for grid method")
            W = grid_contiguity_weight_matrix(coords, cell_size=cell_size,
                                            contiguity=contiguity,
                                            row_standardized=row_standardized,
                                            return_sparse=True)
        else:
            raise ValueError(f"Method '{method}' not supported. Use 'knn', 'distance_band', or 'grid'")
    else:
        W = weights
    
    # Check for zero variance case
    if np.std(X) == 0:
        raise ValueError("All values are identical. Moran's I cannot be calculated.")
    
    # Calculate Moran's I
    X_mean = np.mean(X)
    X_diff = X - X_mean
    #numerator = np.sum(W.multiply(np.outer(X_diff, X_diff)))
    x = np.asarray(X_diff).ravel()
    W = W.tocsr()
    numerator = x @ (W @ x)
    denominator = np.sum(X_diff ** 2)
    S0 = np.sum(W)
    I = (n / S0) * (numerator / denominator)
    if analytical:
        # For analytical p-value, use more stable weight matrix settings
        # Create a fresh weight matrix with binary, non-standardized weights for stability
        try:
            if method == 'distance_band':
                W_analytical = distance_band_weight_matrix(
                    coords,
                    threshold=threshold,
                    row_standardized=False,  # Non-standardized for stability
                    return_sparse=True,
                    binary=True,             # Binary weights for stability
                )
            elif method == 'knn':
                W_analytical = knn_weight_matrix(
                    coords,
                    k=k,
                    row_standardized=False,  # Non-standardized for stability
                    return_sparse=True,
                    symmetric=True,
                )
            else:
                # For other methods, ensure binary, non-standardized
                W_analytical = W.copy()
                if hasattr(W_analytical, 'toarray'):
                    W_analytical = W_analytical.toarray()
                W_analytical = (W_analytical > 0).astype(float)
                from scipy.sparse import csr_matrix as _csr
                W_analytical = _csr(W_analytical)
        except MemoryError:
            # Fallback to KNN if memory error occurs with distance band
            k_safe = min(100, n - 1)
            W_analytical = knn_weight_matrix(
                coords,
                k=k_safe,
                row_standardized=False,
                return_sparse=True,
                symmetric=True,
            )
        
        # If the analytical matrix is unexpectedly dense, fallback to KNN
        try:
            density = W_analytical.nnz / (n * n)
            if density > 0.05:  # 5% density is quite large for 100k+ nodes
                k_safe = min(100, n - 1)
                W_analytical = knn_weight_matrix(
                    coords,
                    k=k_safe,
                    row_standardized=False,
                    return_sparse=True,
                    symmetric=True,
                )
        except Exception:
            pass
        
        # Use analytical normal approximation to return p-value as well
        I_a, z_score, p_value = _moran_analytical(X, W_analytical)
        return I_a, p_value,z_score

    return I


def _moran_analytical(x, W):
    """
    Compute Moran's I, its z-score, and a two-sided p-value using the
    normal approximation under the randomization null hypothesis.
    Works with sparse matrices to handle large datasets efficiently.

    Parameters
    ----------
    x : array-like
        1D numeric array of the variable values.
    W : scipy.sparse matrix
        Spatial weights matrix. Should be symmetric; row-standardization is recommended.

    Returns
    -------
    tuple
        (I, z, p_value)
    """
    import numpy as np
    from scipy.stats import norm
    from scipy.sparse import csr_matrix

    x = np.asarray(x, dtype=float)
    x = x - x.mean()
    n = x.size

    # Ensure W is CSR format for efficient operations
    if hasattr(W, "toarray"):
        W = W.tocsr()
    else:
        W = csr_matrix(W)

    # Symmetrize (sparse operation)
    W = (W + W.T) / 2.0

    # Cliff & Ord / Anselin components (sparse operations)
    S0 = W.sum()
    
    # S1 = 0.5 * sum((W + W.T)^2) = 0.5 * sum(W^2 + W*W.T + W.T*W + W.T^2)
    # Since W is symmetric, this simplifies to sum(W^2)
    W_squared = W.multiply(W)  # Element-wise square
    S1 = W_squared.sum()
    
    # S2 = sum((row_sums + col_sums)^2)
    # Since W is symmetric, row_sums == col_sums
    row_sums = np.array(W.sum(axis=1)).flatten()
    S2 = (2 * row_sums ** 2).sum()

    # Moran's I (sparse operations)
    denom = float(x @ x)
    if denom == 0.0:
        return np.nan, np.nan, np.nan
    
    # W @ x using sparse matrix multiplication
    Wx = W @ x
    I = (n / S0) * float(x @ Wx) / denom

    # Expectation and variance under randomization
    EI = -1.0 / (n - 1)
    
    # More robust variance calculation
    try:
        VI = ((n**2 * S1 - n * S2 + 3 * S0**2) / (((n - 1) * (n - 2) * (n - 3)) * (S0**2))) - (EI**2)
        
        # Check for valid variance
        if VI <= 0 or np.isnan(VI) or np.isinf(VI):
            # Fallback to simpler variance approximation
            VI = (2 * S0**2) / ((n - 1) * (n - 2) * S0**2)
            
        # Additional safety check
        if VI <= 0 or np.isnan(VI) or np.isinf(VI):
            return I, np.nan, np.nan
            
    except (ZeroDivisionError, ValueError):
        return I, np.nan, np.nan

    z = (I - EI) / np.sqrt(VI)
    
    # Check for valid z-score
    if np.isnan(z) or np.isinf(z):
        return I, np.nan, np.nan
        
    p_value = 2 * (1 - norm.cdf(abs(z)))
    
    # Ensure p-value is in valid range
    if np.isnan(p_value) or p_value < 0 or p_value > 1:
        return I, z, np.nan
        
    return I, z, p_value



def _min_area_rect_area(coords: np.ndarray) -> float:
    """
    Compute the area of the minimum-area enclosing rectangle for 2D points.
    Pure NumPy/SciPy (no OpenCV). Handles degenerate/collinear cases.

    Parameters
    ----------
    coords : (n,2) array-like

    Returns
    -------
    float
        Area of the minimum-area rotated rectangle enclosing all points.
    """
    pts = np.asarray(coords, dtype=float)
    if pts.shape[0] == 0:
        return 0.0
    if pts.shape[0] == 1:
        # Single point -> zero area; treat as 0 here (caller will guard with a minimum)
        return 0.0

    # For 2 points, calipers collapses; use bounding box (possibly zero height)
    if pts.shape[0] == 2:
        x_min, y_min = pts.min(axis=0)
        x_max, y_max = pts.max(axis=0)
        return float((x_max - x_min) * (y_max - y_min))

    # Convex hull of points (ordered)
    try:
        hull = ConvexHull(pts)
        H = pts[hull.vertices]
    except Exception:
        # Fallback to axis-aligned bounding box if hull fails
        x_min, y_min = pts.min(axis=0)
        x_max, y_max = pts.max(axis=0)
        return float((x_max - x_min) * (y_max - y_min))

    # Edge directions (wrap last->first)
    edges = np.diff(np.vstack([H, H[0]]), axis=0)  # (m,2)
    # Angles of edges with x-axis, modulo 90 degrees (pi/2) to avoid redundant rotations
    thetas = np.unique(np.mod(np.arctan2(edges[:, 1], edges[:, 0]), np.pi / 2.0))

    # Evaluate area for each candidate angle by rotating hull by -theta and taking AABB
    min_area = np.inf
    for theta in thetas:
        c, s = np.cos(theta), np.sin(theta)
        # Rotation by -theta: R = [[c, s], [-s, c]]
        R = np.array([[c, s], [-s, c]])
        Hr = H @ R.T
        minx, miny = Hr.min(axis=0)
        maxx, maxy = Hr.max(axis=0)
        area = (maxx - minx) * (maxy - miny)
        if area < min_area:
            min_area = area

    # If collinear, min_area can be 0; return as-is (caller will guard)
    return float(min_area if np.isfinite(min_area) else 0.0)


def nearest_neighbor_index(data, analytical=False):
    """
    Calculate the Nearest Neighbor Index (NNI) to measure spatial clustering or dispersion.
    (Enhanced) The study area is now computed as the minimum-area rotated rectangle
    enclosing all input points (or a safe fallback), which is more appropriate than
    convex hull area or axis-aligned bbox for NNI.

    Parameters
    ----------
    data : array-like, pandas.DataFrame, geopandas.GeoDataFrame/GeoSeries, or ESRI SEDF
        Input spatial data. See original docstring.
    analytical : bool, optional
        If True, returns (NNI, observed_avg_distance, expected_avg_distance, p_value, z_score).

    Returns
    -------
    float or tuple
        Same as original.

    Notes
    -----
    Expected distance uses:
        E[r] = 0.5 * sqrt(A / n)
    where A is the minimum-area enclosing rectangle (rotatable).
    """
    # Validate and convert input to standardized format (your existing utility)
    coords, values, n = _validate_and_convert_input(data, None)

    if n < 2:
        raise ValueError("At least 2 points are required for nearest neighbor analysis")

    # Observed average nearest-neighbor distance (memory-efficient)
    nn = NearestNeighbors(n_neighbors=2, algorithm='auto', metric='euclidean')
    nn.fit(coords)
    distances, _ = nn.kneighbors(coords)
    nearest_distances = distances[:, 1]
    observed_avg_distance = float(np.mean(nearest_distances))

    # --- NEW: Study area via minimum-area enclosing rectangle (rotating) ---
    area = _min_area_rect_area(coords)

    # Guard against degenerate/collinear cases
    if area <= 0 or not np.isfinite(area):
        # Fallback to axis-aligned bbox
        x_min, y_min = coords.min(axis=0)
        x_max, y_max = coords.max(axis=0)
        area = float((x_max - x_min) * (y_max - y_min))

    # Still pathological? enforce a minimal study area to avoid division by ~0
    if area <= 0 or not np.isfinite(area) or area < 1e-12:
        warnings.warn("Study area was zero or ill-conditioned; using minimum area of 1.0")
        area = 1.0

    # Expected distance under CSR
    expected_avg_distance = 0.5 * np.sqrt(area / n)

    # NNI
    nni = observed_avg_distance / expected_avg_distance

    if analytical:
        # Clark & Evans (1954) approximation for SE(NNI)
        se_nni = 0.26136 / np.sqrt(n)
        z_score = (nni - 1.0) / se_nni if se_nni > 0 else np.nan
        from scipy.stats import norm
        p_value = 2 * (1 - norm.cdf(np.abs(z_score))) if np.isfinite(z_score) else np.nan
        return nni, observed_avg_distance, expected_avg_distance, p_value, z_score

    return nni
