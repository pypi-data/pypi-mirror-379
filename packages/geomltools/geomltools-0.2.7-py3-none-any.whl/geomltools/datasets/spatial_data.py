import os
import pandas as pd
import geopandas as gpd
import importlib.resources
import numpy as np
import random

def read_csv_spatial(filepath, type='dataframe', x_col=None, y_col=None, wkt_col=None, srid=None, **kwargs):
    """
    Read a CSV file and return as a pandas DataFrame, GeoPandas GeoDataFrame, or ESRI SEDF.

    Parameters
    ----------
    filepath : str
        Path to the CSV file.
    type : str, optional
        Output type: 'dataframe' (default), 'geodataframe', or 'sedf'.
    x_col : str or None, optional
        Name of the column to use for X (longitude) coordinates (for points).
    y_col : str or None, optional
        Name of the column to use for Y (latitude) coordinates (for points).
    wkt_col : str or None, optional
        Name of the column containing WKT geometries (for polygons).
    srid : int or str or None, optional
        EPSG code or CRS string to set for the geometry column.
    **kwargs :
        Additional keyword arguments passed to pandas.read_csv.

    Returns
    -------
    pandas.DataFrame, geopandas.GeoDataFrame, or arcgis.features.SpatialDataFrame
        The loaded data in the requested format.

    Raises
    ------
    ImportError
        If 'sedf' is requested but arcgis is not installed.
    ValueError
        If type is not recognized or required columns are missing.
    """
    df = pd.read_csv(filepath, **kwargs)
    if type == 'dataframe':
        return df
    elif type == 'geodataframe':
        if x_col and y_col and {x_col, y_col}.issubset(df.columns):
            gdf = gpd.GeoDataFrame(df, geometry=gpd.points_from_xy(df[x_col], df[y_col]))
        elif wkt_col and wkt_col in df.columns:
            gdf = gpd.GeoDataFrame(df, geometry=gpd.GeoSeries.from_wkt(df[wkt_col]))
        else:
            raise ValueError("Cannot create GeoDataFrame: provide x_col and y_col for points, or wkt_col for polygons.")
        if srid:
            gdf = gdf.set_crs(srid)
        return gdf
    elif type == 'sedf':
        try:
            import arcgis
        except ImportError:
            raise ImportError("arcgis is required for SEDF output. Please install arcgis package.")
        if x_col and y_col and {x_col, y_col}.issubset(df.columns):
            sdf = df.spatial.from_xy(df,x_column=x_col, y_column=y_col, sr=srid)
        elif wkt_col and wkt_col in df.columns:
            sdf = df.spatial.from_wkt(df,wkt_col, sr=srid)
        else:
            raise ValueError("Cannot create SEDF: provide x_col and y_col for points, or wkt_col for polygons.")
        return sdf
    else:
        raise ValueError(f"Unknown type: {type}. Must be one of 'dataframe', 'geodataframe', or 'sedf'.")
    
 

def get_dataset(dataset_filename, type='dataframe', x_col=None, y_col=None, wkt_col=None, srid=None, **kwargs):
    """
    General function to load a dataset from the data directory.

    Parameters
    ----------
    dataset_filename : str
        Name of the dataset file (e.g., 'Detroit 911 Calls.csv').
    type : str, optional
        Output type: 'dataframe' (default), 'geodataframe', or 'sedf'.
    x_col : str or None, optional
        Name of the column to use for X (longitude) coordinates (for points).
    y_col : str or None, optional
        Name of the column to use for Y (latitude) coordinates (for points).
    wkt_col : str or None, optional
        Name of the column containing WKT geometries (for polygons).
    srid : int or str or None, optional
        EPSG code or CRS string to set for the geometry column.
    **kwargs :
        Additional keyword arguments passed to pandas.read_csv.

    Returns
    -------
    pandas.DataFrame, geopandas.GeoDataFrame, or arcgis.features.SpatialDataFrame
        The loaded data in the requested format.
    """
    with importlib.resources.path("geomltools.datasets.data", dataset_filename) as data_path:
        return read_csv_spatial(
            str(data_path),
            type=type,
            x_col=x_col,
            y_col=y_col,
            wkt_col=wkt_col,
            srid=srid,
            **kwargs
        )


def get_detroit_911_calls(type='dataframe'):
    """
    Load the Detroit 911 Calls dataset from the data directory.

    Parameters
    ----------
    type : str, optional
        Output type: 'dataframe' (default), 'geodataframe', or 'sedf'.

    Returns
    -------
    pandas.DataFrame, geopandas.GeoDataFrame, or arcgis.features.SpatialDataFrame
        The loaded data in the requested format.
    """
    return get_dataset(
        "Detroit 911 Calls.csv",
        type=type,
        x_col='longitude' if type in ('geodataframe', 'sedf') else None,
        y_col='latitude' if type in ('geodataframe', 'sedf') else None
    )


def get_earthquakes_2006_2019(type='dataframe'):
    """
    Load the earthquakes_2006_2019 dataset from the data directory.

    Parameters
    ----------
    type : str, optional
        Output type: 'dataframe' (default), 'geodataframe', or 'sedf'.

    Returns
    -------
    pandas.DataFrame, geopandas.GeoDataFrame, or arcgis.features.SpatialDataFrame
        The loaded data in the requested format.
    """
    return get_dataset(
        "earthquakes_2006_2019.csv",
        type=type,
        x_col='Long' if type in ('geodataframe', 'sedf') else None,
        y_col='Lat' if type in ('geodataframe', 'sedf') else None
    )


"""def get_crime_data_2020_2025(type='dataframe'):
    
    Load the Crime_Data_from_2020_to_2025 dataset from the data directory.

    Parameters
    ----------
    type : str, optional
        Output type: 'dataframe' (default), 'geodataframe', or 'sedf'.

    Returns
    -------
    pandas.DataFrame, geopandas.GeoDataFrame, or arcgis.features.SpatialDataFrame
        The loaded data in the requested format.
    
    return get_dataset(
        "Crime_Data_from_2020_to_2025.csv",
        type=type,
        x_col='LON' if type in ('geodataframe', 'sedf') else None,
        y_col='LAT' if type in ('geodataframe', 'sedf') else None
    )"""


def generate_random_points(n_points, extent, float_min=0.0, float_max=1.0, 
                          output_type='dataframe', srid=None, random_seed=None,
                          float_column_name='float_attr', binary_column_name='binary_attr',
                          x_column_name='x', y_column_name='y'):
    """
    Generate random points with random float and binary attributes.
    
    Parameters
    ----------
    n_points : int
        Number of random points to generate.
    extent : tuple or list
        Spatial extent as (xmin, ymin, xmax, ymax) or [xmin, ymin, xmax, ymax].
    float_min : float, optional
        Min value for the uniform distribution of float attributes (default: 0.0).
    float_max : float, optional
        Max value for the uniform distribution of float attributes (default: 1.0).
    output_type : str, optional
        Output type: 'dataframe' (default), 'geodataframe', or 'sedf'.
    srid : int or str or None, optional
        EPSG code or CRS string to set for the geometry column (for geodataframe/sedf).
    random_seed : int or None, optional
        Random seed for reproducible results (default: None).
    float_column_name : str, optional
        Name for the float attribute column (default: 'float_attr').
    binary_column_name : str, optional
        Name for the binary attribute column (default: 'binary_attr').
    x_column_name : str, optional
        Name for the X coordinate column (default: 'x').
    y_column_name : str, optional
        Name for the Y coordinate column (default: 'y').
    
    Returns
    -------
    pandas.DataFrame, geopandas.GeoDataFrame, or arcgis.features.SpatialDataFrame
        Random points with float and binary attributes in the requested format.
    
    Raises
    ------
    ValueError
        If extent is not properly formatted or n_points is not positive.
    ImportError
        If 'sedf' is requested but arcgis is not installed.
    
    """
    # Validate inputs
    if n_points <= 0:
        raise ValueError("n_points must be a positive integer")
    
    if len(extent) != 4:
        raise ValueError("extent must be a tuple or list with 4 elements: (xmin, ymin, xmax, ymax)")
    
    xmin, ymin, xmax, ymax = extent
    if xmin >= xmax or ymin >= ymax:
        raise ValueError("extent must have xmin < xmax and ymin < ymax")
    
    
    # Set random seed if provided
    if random_seed is not None:
        np.random.seed(random_seed)
        random.seed(random_seed)
    
    # Generate random coordinates
    x_coords = np.random.uniform(xmin, xmax, n_points)
    y_coords = np.random.uniform(ymin, ymax, n_points)
    
    # Generate random float attributes using normal distribution
    float_attrs = np.random.uniform(float_min, float_max, n_points)
    
    # Generate random binary attributes (0 or 1)
    binary_attrs = np.random.randint(0, 2, n_points)
    
    # Create DataFrame
    df = pd.DataFrame({
        x_column_name: x_coords,
        y_column_name: y_coords,
        float_column_name: float_attrs,
        binary_column_name: binary_attrs
    })

    df[float_column_name] = df[float_column_name].sample(frac=1).reset_index(drop=True)
    
    # Return based on output type
    if output_type == 'dataframe':
        return df
    elif output_type == 'geodataframe':
        gdf = gpd.GeoDataFrame(df, geometry=gpd.points_from_xy(df[x_column_name], df[y_column_name]))
        if srid:
            gdf = gdf.set_crs(srid)
        return gdf
    elif output_type == 'sedf':
        try:
            import arcgis
        except ImportError:
            raise ImportError("arcgis is required for SEDF output. Please install arcgis package.")
        sdf = df.spatial.from_xy(df, x_column=x_column_name, y_column=y_column_name, sr=srid)
        return sdf
    else:
        raise ValueError(f"Unknown output_type: {output_type}. Must be one of 'dataframe', 'geodataframe', or 'sedf'.")
