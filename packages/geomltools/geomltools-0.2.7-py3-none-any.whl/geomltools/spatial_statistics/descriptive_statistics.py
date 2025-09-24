import numpy as np
from scipy.spatial.distance import cdist
from scipy.optimize import minimize
import pandas as pd
from shapely.geometry import Point

def weighted_median(data, weights):
    """Compute the weighted median of data."""
    data, weights = np.array(data), np.array(weights)
    sorted_idx = np.argsort(data)
    data, weights = data[sorted_idx], weights[sorted_idx]
    cum_weights = np.cumsum(weights)
    cutoff = weights.sum() / 2.0
    return data[cum_weights >= cutoff][0]

def _normalize_geometries(sdf, geometry_col=None):
    """
    Normalize spatial input to a GeoPandas GeoSeries of geometries, with input type and metadata.

    This utility function auto-detects and converts a variety of spatial data formats to a standard
    GeoPandas GeoSeries for internal processing. It supports:
      - NumPy arrays of shape (n_samples, 2) (interpreted as points)
      - Pandas DataFrames with 'x'/'y' columns or a geometry column
      - GeoPandas GeoDataFrames/GeoSeries
      - ESRI Spatially Enabled DataFrames (SEDF, from arcgis.features)

    Parameters
    ----------
    sdf : array-like, pandas.DataFrame, geopandas.GeoDataFrame/GeoSeries, or ESRI SEDF
        The spatial data to normalize. Can be:
          - NumPy array of shape (n_samples, 2)
          - Pandas DataFrame with 'x'/'y' columns or a geometry column
          - GeoPandas GeoDataFrame or GeoSeries
          - ESRI SEDF (arcgis.features.SpatialDataFrame)
    geometry_col : str or None, optional
        Name of the geometry column to use (for DataFrames). If None, tries to auto-detect:
          - 'geometry' (GeoPandas or Pandas)
          - 'SHAPE' (ESRI SEDF or Pandas)
          - 'x'/'y' columns (Pandas)

    Returns
    -------
    geoms : geopandas.GeoSeries
        The normalized geometries as a GeoSeries (points or polygons).
    input_type : str
        One of 'numpy', 'pandas', 'geopandas', or 'sedf', indicating the original input type.
    original_input : object
        The original input object (for output conversion).
    geometry_col_name : str or None
        The name of the geometry column used (if applicable).

    Raises
    ------
    ValueError
        If the input type or geometry column cannot be determined or is unsupported.

    Example
    -------
    >>> _normalize_geometries(np.array([[0, 1], [2, 3]]))
    (GeoSeries of Points, 'numpy', ...)
    >>> _normalize_geometries(df, geometry_col='geometry')
    (GeoSeries, 'pandas', ...)
    >>> _normalize_geometries(gdf)
    (GeoSeries, 'geopandas', ...)
    >>> _normalize_geometries(sedf)
    (GeoSeries, 'sedf', ...)
    """
    import geopandas as gpd
    from shapely.geometry import Point, Polygon, shape
    # ESRI SEDF
    try:
        from arcgis.features import SpatialDataFrame
        is_sedf = isinstance(sdf, SpatialDataFrame)
    except ImportError:
        is_sedf = False
    # GeoPandas
    if hasattr(sdf, "geometry"):
        geometry_col = geometry_col or sdf.geometry.name
        geoms = sdf.geometry
    # ESRI SEDF
    elif is_sedf:
        gdf = sdf.spatial.to_geodataframe()
        geometry_col = geometry_col or gdf.geometry.name
        geoms = gdf.geometry
    # Pandas DataFrame with x/y or geometry
    elif hasattr(sdf, "columns"):
        if geometry_col is None:
            if 'geometry' in sdf.columns:
                geometry_col = 'geometry'
            elif 'SHAPE' in sdf.columns:
                geometry_col = 'SHAPE'
            elif set(['x', 'y']).issubset(sdf.columns):
                geometry_col = None
            else:
                raise ValueError("Could not auto-detect geometry column. Please specify geometry_col.")
        if geometry_col is not None:
            geoms = sdf[geometry_col]
        elif set(['x', 'y']).issubset(sdf.columns):
            geoms = gpd.GeoSeries([Point(xy) for xy in zip(sdf['x'], sdf['y'])])
        else:
            raise ValueError("Could not auto-detect geometry column. Please specify geometry_col.")
    # Numpy array
    else:
        arr = np.asarray(sdf)
        if arr.ndim == 2 and arr.shape[1] == 2:
            geoms = gpd.GeoSeries([Point(xy) for xy in arr])
        else:
            raise ValueError("Unsupported input type for spatial data. Supported: numpy, pandas, geopandas, ESRI SEDF.")
    # Robustly convert all geometries to Shapely objects
    def to_shapely(g):
        from shapely.geometry import Point, Polygon, shape
        if isinstance(g, (Point, Polygon)):
            return g
        if isinstance(g, dict):
            try:
                return shape(g)
            except Exception:
                if 'x' in g and 'y' in g:
                    return Point(g['x'], g['y'])
        if isinstance(g, (tuple, list)) and len(g) == 2 and all(isinstance(val, (int, float)) for val in g):
            return Point(g)
        if isinstance(g, str):
            try:
                from shapely import wkt
                return wkt.loads(g)
            except Exception:
                pass
        return g
    geoms = geoms.apply(to_shapely)
    # Determine input type string
    if is_sedf:
        input_type = 'sedf'
    elif hasattr(sdf, "geometry"):
        input_type = 'geopandas'
    elif hasattr(sdf, "columns"):
        input_type = 'pandas'
    else:
        input_type = 'numpy'
    return geoms, input_type, sdf, geometry_col


def spatial_central_tendency(sdf, method='mean', weight_field=None, case_field=None, geometry_col=None):
    """
    Compute spatial central tendency (mean, median, geometric median, or central feature) for points or polygons.

    Supports input as numpy array, pandas DataFrame, GeoPandas, or ESRI SEDF.
    For polygons, centroids are used for calculations.
    Output format matches input type (GeoPandas, SEDF, Pandas, or NumPy).

    Parameters
    ----------
    sdf : array-like, pandas.DataFrame, geopandas.GeoDataFrame/GeoSeries, or ESRI SEDF
        Spatial data as points or polygons.
    method : str
        Central tendency method:
        - 'mean' : Mean center (average X, Y)
        - 'simple_median' : Coordinate-wise median (median X, Y)
        - 'advanced_median' : Geometric median (minimizes sum of Euclidean distances)
        - 'central_feature' : Actual feature closest to all others
    weight_field : str or None
        Optional. Name of the field in sdf to use as weights.
    case_field : str or None
        Optional. Name of the field in sdf to use for grouping.
    geometry_col : str or None
        Optional. Name of the geometry column. If None, tries to auto-detect.

    Returns
    -------
    Output matches input type:
        - GeoPandas: GeoDataFrame with group and center columns
        - SEDF: SEDF with group and center columns
        - Pandas: DataFrame with group and center columns
        - NumPy: tuple (x, y) or array of centers

    Notes
    -----
    For polygons, the centroid is used for all calculations.
    If case_field is provided, returns a DataFrame/GeoDataFrame/SEDF of group centers.

    Example
    -------
    >>> spatial_central_tendency(gdf, method='mean')
    >>> spatial_central_tendency(sedf, method='advanced_median', case_field='region')
    """
    import geopandas as gpd
    from shapely.geometry import Point
    try:
        from arcgis.features import SpatialDataFrame
        has_sedf = True
    except ImportError:
        has_sedf = False
    geoms, input_type, orig, geometry_col_name = _normalize_geometries(sdf, geometry_col)
    # Use centroids for polygons
    points = geoms.apply(lambda g: g.centroid if not isinstance(g, Point) else g)
    coords = np.array([[pt.x, pt.y] for pt in points])
    weights = None
    if weight_field is not None and hasattr(orig, '__getitem__') and weight_field in orig:
        weights = np.array(orig[weight_field])
    if case_field is not None and hasattr(orig, 'groupby'):
        results = []
        for group_val, group_df in orig.groupby(case_field):
            center = spatial_central_tendency(group_df, method=method, weight_field=weight_field, geometry_col=geometry_col_name)
            if isinstance(center, tuple):
                center_geom = Point(center)
                center_x, center_y = center
            elif hasattr(center, 'iloc'):
                center_x, center_y = center.iloc[0]['x'], center.iloc[0]['y']
                center_geom = Point((center_x, center_y))
            else:
                center_x, center_y = center[0], center[1]
                center_geom = Point(center)
            results.append({
                case_field: group_val,
                'x': center_x,
                'y': center_y,
                'geometry': center_geom
            })
        df = pd.DataFrame(results)
        if input_type == 'geopandas':
            return gpd.GeoDataFrame(df, geometry='geometry')
        elif input_type == 'sedf' and has_sedf:
            return SpatialDataFrame.from_geodataframe(gpd.GeoDataFrame(df, geometry='geometry'))
        else:
            return df
    if method == 'mean':
        if weights is not None:
            center = tuple(np.average(coords, axis=0, weights=weights))
        else:
            center = tuple(np.mean(coords, axis=0))
    elif method == 'simple_median':
        if weights is not None:
            x_med = weighted_median(coords[:, 0], weights)
            y_med = weighted_median(coords[:, 1], weights)
            center = (x_med, y_med)
        else:
            center = tuple(np.median(coords, axis=0))
    elif method == 'advanced_median':
        def total_distance(p):
            dists = np.linalg.norm(coords - p, axis=1)
            if weights is not None:
                return np.sum(weights * dists)
            return np.sum(dists)
        from scipy.optimize import minimize
        result = minimize(total_distance, np.average(coords, axis=0, weights=weights) if weights is not None else np.mean(coords, axis=0), method='Nelder-Mead')
        center = tuple(result.x)
    elif method == 'central_feature':
        from scipy.spatial.distance import cdist
        dist_matrix = cdist(coords, coords)
        if weights is not None:
            total_dists = (dist_matrix * weights).sum(axis=1)
        else:
            total_dists = dist_matrix.sum(axis=1)
        idx = np.argmin(total_dists)
        center = tuple(coords[idx])
    else:
        raise ValueError("Unsupported method. Use 'mean', 'simple_median', 'advanced_median', or 'central_feature'.")
    # Output conversion
    if input_type == 'geopandas':
        return gpd.GeoDataFrame({'x': [center[0]], 'y': [center[1]], 'geometry': [Point(center)]})
    elif input_type == 'sedf' and has_sedf:
        return SpatialDataFrame.from_geodataframe(gpd.GeoDataFrame({'x': [center[0]], 'y': [center[1]], 'geometry': [Point(center)]}))
    elif input_type == 'pandas':
        return pd.DataFrame({'x': [center[0]], 'y': [center[1]], 'geometry': [Point(center)]})
    elif input_type == 'numpy':
        return center
    else:
        return center


def standard_distance(sdf, weight_field=None, case_field=None, geometry_col=None, plot=False, ax=None, show=True, n_std=1, **scatter_kwargs):
    """
    Compute the (weighted) standard distance of features to the mean center, optionally by group, and optionally plot the result.

    Supports input as numpy array, pandas DataFrame, GeoPandas, or ESRI SEDF.
    For polygons, centroids are used for calculations.
    Output format matches input type (GeoPandas, SEDF, Pandas, or NumPy).

    Parameters
    ----------
    sdf : array-like, pandas.DataFrame, geopandas.GeoDataFrame/GeoSeries, or ESRI SEDF
        Spatial data as points or polygons.
    weight_field : str or None
        Optional. Name of the field in sdf to use as weights.
    case_field : str or None
        Optional. Name of the field in sdf to use for grouping.
    geometry_col : str or None
        Optional. Name of the geometry column. If None, tries to auto-detect.
    plot : bool
        If True, plot the points, mean center, and standard distance circle(s).
    ax : matplotlib.axes.Axes or None
        Optional. Axes to plot on. If None, creates a new figure.
    show : bool
        Whether to call plt.show() after plotting.
    n_std : int or list of int, default 1
        Number(s) of standard deviations for the circle radius. Can be a single int or a list (e.g., [1,2,3]).
    **scatter_kwargs : dict
        Additional keyword arguments for the scatter plot.

    Returns
    -------
    Output matches input type:
        - GeoPandas: GeoDataFrame with group and standard distance columns
        - SEDF: SEDF with group and standard distance columns
        - Pandas: DataFrame with group and standard distance columns
        - NumPy: float or array of standard distances

    Notes
    -----
    For polygons, the centroid is used for all calculations.
    If case_field is provided, returns a DataFrame/GeoDataFrame/SEDF of group results.

    Example
    -------
    >>> standard_distance(gdf, plot=True)
    >>> standard_distance(sedf, case_field='region')
    """
    import geopandas as gpd
    from shapely.geometry import Point
    import matplotlib.pyplot as plt
    try:
        from arcgis.features import SpatialDataFrame
        has_sedf = True
    except ImportError:
        has_sedf = False
    geoms, input_type, orig, geometry_col_name = _normalize_geometries(sdf, geometry_col)
    # Use centroids for polygons
    points = geoms.apply(lambda g: g.centroid if not isinstance(g, Point) else g)
    # Defensive: convert any tuple to Point
    points = points.apply(lambda pt: Point(pt) if isinstance(pt, tuple) else pt)
    coords = np.array([[pt.x, pt.y] for pt in points])
    weights = None
    if weight_field is not None and hasattr(orig, '__getitem__') and weight_field in orig:
        weights = np.array(orig[weight_field])
    if isinstance(n_std, int):
        n_std = [n_std]
    if case_field is not None and hasattr(orig, 'groupby'):
        results = []
        group_axes = None
        if plot:
            if ax is None:
                fig, ax = plt.subplots(figsize=(6, 6))
                group_axes = ax
            else:
                group_axes = ax
            colors = plt.cm.get_cmap('tab10')
        for i, (group_val, group_df) in enumerate(orig.groupby(case_field)):
            sd = standard_distance(group_df, weight_field=weight_field, geometry_col=geometry_col_name, plot=False)
            sd_val = sd if not isinstance(sd, pd.DataFrame) else sd['standard_distance'].iloc[0]
            results.append({
                case_field: group_val,
                'standard_distance': sd_val
            })
            if plot:
                g, _, _, _ = _normalize_geometries(group_df, geometry_col_name)
                pts = g.apply(lambda g: g.centroid if not isinstance(g, Point) else g)
                c = np.array([[pt.x, pt.y] for pt in pts])
                if weight_field is not None and weight_field in group_df:
                    w = np.array(group_df[weight_field])
                    mean_center = np.average(c, axis=0, weights=w)
                else:
                    mean_center = np.mean(c, axis=0)
                color = colors(i % 10)
                group_axes.scatter(c[:, 0], c[:, 1], label=f'Points ({group_val})', color=color, **scatter_kwargs)
                group_axes.scatter([mean_center[0]], [mean_center[1]], color=color, marker='x', s=100, label=f'Mean Center ({group_val})')
                for n in n_std:
                    circle = plt.Circle((mean_center[0], mean_center[1]), n * sd_val, color=color, fill=False, linestyle='--', alpha=0.5, label=f'{n} Std Distance ({group_val})')
                    group_axes.add_patch(circle)
        if plot:
            handles, labels = group_axes.get_legend_handles_labels()
            # Remove duplicate labels
            unique = dict(zip(labels, handles))
            group_axes.legend(unique.values(), unique.keys())
            group_axes.set_aspect('equal')
            group_axes.set_xlabel('X')
            group_axes.set_ylabel('Y')
            group_axes.set_title('Standard Distance Circle (by group)')
            if show:
                plt.show()
        df = pd.DataFrame(results)
        if input_type == 'geopandas':
            return gpd.GeoDataFrame(df)
        elif input_type == 'sedf' and has_sedf:
            return SpatialDataFrame.from_geodataframe(gpd.GeoDataFrame(df))
        else:
            return df
    # Compute mean center
    if weights is not None:
        mean_center = np.average(coords, axis=0, weights=weights)
    else:
        mean_center = np.mean(coords, axis=0)
    # Compute squared distances to mean center
    dists_sq = np.sum((coords - mean_center) ** 2, axis=1)
    if weights is not None:
        sd = np.sqrt(np.sum(weights * dists_sq) / np.sum(weights))
    else:
        sd = np.sqrt(np.mean(dists_sq))
    if plot:
        if ax is None:
            fig, ax = plt.subplots(figsize=(6, 6))
        ax.scatter(coords[:, 0], coords[:, 1], label='Points', **scatter_kwargs)
        ax.scatter([mean_center[0]], [mean_center[1]], color='red', marker='x', s=100, label='Mean Center')
        for n in n_std:
            circle = plt.Circle((mean_center[0], mean_center[1]), n * sd, color='blue', fill=False, linestyle='--', alpha=0.5, label=f'{n} Std Distance')
            ax.add_patch(circle)
        ax.set_aspect('equal')
        ax.legend()
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_title('Standard Distance Circle')
        if show:
            plt.show()
    # Output conversion
    if input_type == 'geopandas':
        return gpd.GeoDataFrame({'standard_distance': [sd]})
    elif input_type == 'sedf' and has_sedf:
        return SpatialDataFrame.from_geodataframe(gpd.GeoDataFrame({'standard_distance': [sd]}))
    elif input_type == 'pandas':
        return pd.DataFrame({'standard_distance': [sd]})
    elif input_type == 'numpy':
        return sd
    else:
        return sd


def directional_distribution(
    sdf,
    weight_field=None,
    case_field=None,
    geometry_col=None,
    plot=False,
    ax=None,
    show=True,
    n_std=1,
    ellipse_kwargs=None,
    **scatter_kwargs
):
    """
    Compute and plot the Standard Deviational Ellipse (Directional Distribution) for points or polygons.

    Supports input as numpy array, pandas DataFrame, GeoPandas, or ESRI SEDF.
    For polygons, centroids are used for calculations.
    Output format matches input type (GeoPandas, SEDF, Pandas, or NumPy).

    Parameters
    ----------
    sdf : array-like, pandas.DataFrame, geopandas.GeoDataFrame/GeoSeries, or ESRI SEDF
        Spatial data as points or polygons.
    weight_field : str or None
        Optional. Name of the field in sdf to use as weights.
    case_field : str or None
        Optional. Name of the field in sdf to use for grouping.
    geometry_col : str or None
        Optional. Name of the geometry column. If None, tries to auto-detect.
    plot : bool
        If True, plot the points, mean center, and standard deviational ellipse(s).
    ax : matplotlib.axes.Axes or None
        Optional. Axes to plot on. If None, creates a new figure.
    show : bool
        Whether to call plt.show() after plotting.
    n_std : int or list of int, default 1
        Number(s) of standard deviations for the ellipse axes. Can be a single int or a list (e.g., [1,2,3]).
    ellipse_kwargs : dict or None
        Additional keyword arguments for the Ellipse patch.
    **scatter_kwargs : dict
        Additional keyword arguments for the scatter plot.

    Returns
    -------
    Output matches input type:
        - GeoPandas: GeoDataFrame with ellipse parameters
        - SEDF: SEDF with ellipse parameters
        - Pandas: DataFrame with ellipse parameters
        - NumPy: dict of ellipse parameters

    Notes
    -----
    For polygons, the centroid is used for all calculations.
    If case_field is provided, returns a DataFrame/GeoDataFrame/SEDF of group results.

    Example
    -------
    >>> directional_distribution(gdf, plot=True)
    >>> directional_distribution(sedf, case_field='region')
    """
    import geopandas as gpd
    from shapely.geometry import Point, Polygon, MultiPolygon
    import matplotlib.pyplot as plt
    from matplotlib.patches import Ellipse
    try:
        from arcgis.features import SpatialDataFrame
        has_sedf = True
    except ImportError:
        has_sedf = False
    geoms, input_type, orig, geometry_col_name = _normalize_geometries(sdf, geometry_col)
    points = geoms.apply(lambda g: g.centroid if not isinstance(g, Point) else g)
    coords = np.array([[pt.x, pt.y] for pt in points])
    weights = None
    if weight_field is not None and hasattr(orig, '__getitem__') and weight_field in orig:
        weights = np.array(orig[weight_field])
    if isinstance(n_std, int):
        n_std = [n_std]
    if ellipse_kwargs is None:
        ellipse_kwargs = {}
    def is_polygonal(geom):
        return isinstance(geom, (Polygon, MultiPolygon))
    if case_field is not None and hasattr(orig, 'groupby'):
        results = []
        if plot:
            if ax is None:
                fig, ax = plt.subplots(figsize=(6, 6))
            colors = plt.cm.get_cmap('tab10')
        for i, (group_val, group_df) in enumerate(orig.groupby(case_field)):
            res = directional_distribution(
                group_df,
                weight_field=weight_field,
                geometry_col=geometry_col_name,
                plot=False,
                n_std=n_std,
                ellipse_kwargs=ellipse_kwargs,
                **scatter_kwargs
            )
            if isinstance(res, pd.DataFrame):
                res = res.iloc[0].to_dict()
            res[case_field] = group_val
            results.append(res)
            if plot:
                g, _, _, _ = _normalize_geometries(group_df, geometry_col_name)
                pts = g.apply(lambda g: g.centroid if not isinstance(g, Point) else g)
                c = np.array([[pt.x, pt.y] for pt in pts])
                color = colors(i % 10)
                if all(is_polygonal(geom) for geom in g):
                    gdf_tmp = gpd.GeoDataFrame(geometry=g)
                    gdf_tmp.boundary.plot(ax=ax, color=color, label=f'Polygons ({group_val})')
                    gdf_tmp.centroid.plot(ax=ax, color='red', marker='o', label=f'Centroids ({group_val})')
                else:
                    ax.scatter(c[:, 0], c[:, 1], label=f'Points ({group_val})', color=color, **scatter_kwargs)
                mean_center = res['mean_center']
                if isinstance(mean_center, pd.Series):
                    if set(mean_center.index) >= {'x', 'y'}:
                        mean_center = (mean_center['x'], mean_center['y'])
                    elif len(mean_center) == 1 and isinstance(mean_center.iloc[0], (tuple, list)):
                        mean_center = mean_center.iloc[0]
                    elif len(mean_center) >= 2:
                        mean_center = tuple(mean_center.values[:2])
                ax.scatter([mean_center[0]], [mean_center[1]], color=color, marker='x', s=100, label=f'Mean Center ({group_val})')
                for j, n in enumerate(n_std):
                    ellipse_args = dict(
                        xy=mean_center,
                        width=2 * res['std_x'],
                        height=2 * res['std_y'],
                        angle=res['angle_deg'],
                    )
                    # Set defaults only if not in ellipse_kwargs
                    if 'edgecolor' not in ellipse_kwargs and 'color' not in ellipse_kwargs:
                        ellipse_args['edgecolor'] = color
                    if 'facecolor' not in ellipse_kwargs:
                        ellipse_args['facecolor'] = 'none'
                    if 'linestyle' not in ellipse_kwargs:
                        ellipse_args['linestyle'] = '--'
                    if 'alpha' not in ellipse_kwargs:
                        ellipse_args['alpha'] = 0.5
                    if 'label' not in ellipse_kwargs:
                        ellipse_args['label'] = f'{n} Std Ellipse ({group_val})' if j == 0 else None
                    ellipse_args.update(ellipse_kwargs)
                    ell = Ellipse(**ellipse_args)
                    ax.add_patch(ell)
        if plot:
            ax.set_aspect('equal')
            ax.legend()
            ax.set_xlabel('X')
            ax.set_ylabel('Y')
            ax.set_title('Standard Deviational Ellipse')
            if show:
                plt.show()
        df = pd.DataFrame(results)
        if input_type == 'geopandas':
            return gpd.GeoDataFrame(df)
        elif input_type == 'sedf' and has_sedf:
            return SpatialDataFrame.from_geodataframe(gpd.GeoDataFrame(df))
        else:
            return df
    # Single group (no case_field)
    if weights is not None:
        mean_center = np.average(coords, axis=0, weights=weights)
    else:
        mean_center = np.mean(coords, axis=0)
    centered = coords - mean_center
    if weights is not None:
        cov = np.cov(centered.T, aweights=weights, bias=True)
    else:
        cov = np.cov(centered.T, bias=True)
    eigvals, eigvecs = np.linalg.eigh(cov)
    order = np.argsort(eigvals)[::-1]
    eigvals = eigvals[order]
    eigvecs = eigvecs[:, order]
    std_x, std_y = np.sqrt(eigvals)
    angle_rad = np.arctan2(eigvecs[1, 0], eigvecs[0, 0])
    angle_deg = np.degrees(angle_rad)
    result = {
        'mean_center': tuple(mean_center),
        'std_x': std_x,
        'std_y': std_y,
        'angle_deg': angle_deg,
        'covariance_matrix': cov
    }
    if plot:
        if ax is None:
            fig, ax = plt.subplots(figsize=(6, 6))
        if all(is_polygonal(geom) for geom in geoms):
            gdf_tmp = gpd.GeoDataFrame(geometry=geoms)
            gdf_tmp.boundary.plot(ax=ax, color='black', label='Polygons')
            gdf_tmp.centroid.plot(ax=ax, color='red', marker='o', label='Centroids')
        else:
            ax.scatter(coords[:, 0], coords[:, 1], label='Points', **scatter_kwargs)
        ax.scatter([mean_center[0]], [mean_center[1]], color='blue', marker='x', s=100, label='Mean Center')
        for j, n in enumerate(n_std):
            ellipse_args = dict(
                xy=mean_center,
                width=2 * std_x,
                height=2 * std_y,
                angle=angle_deg,
            )
            if 'edgecolor' not in ellipse_kwargs and 'color' not in ellipse_kwargs:
                ellipse_args['edgecolor'] = 'green'
            if 'facecolor' not in ellipse_kwargs:
                ellipse_args['facecolor'] = 'none'
            if 'linestyle' not in ellipse_kwargs:
                ellipse_args['linestyle'] = '--'
            if 'alpha' not in ellipse_kwargs:
                ellipse_args['alpha'] = 0.5
            if 'label' not in ellipse_kwargs:
                ellipse_args['label'] = f'{n} Std Ellipse' if j == 0 else None
            ellipse_args.update(ellipse_kwargs)
            ell = Ellipse(**ellipse_args)
            ax.add_patch(ell)
        ax.set_aspect('equal')
        ax.legend()
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_title('Standard Deviational Ellipse')
        if show:
            plt.show()
    # Output conversion
    if input_type == 'geopandas':
        return gpd.GeoDataFrame({k: [v] if not isinstance(v, np.ndarray) else [v.tolist()] for k, v in result.items()})
    elif input_type == 'sedf' and has_sedf:
        return SpatialDataFrame.from_geodataframe(gpd.GeoDataFrame({k: [v] if not isinstance(v, np.ndarray) else [v.tolist()] for k, v in result.items()}))
    elif input_type == 'pandas':
        return pd.DataFrame({k: [v] if not isinstance(v, np.ndarray) else [v.tolist()] for k, v in result.items()})
    elif input_type == 'numpy':
        return result
    else:
        return result
