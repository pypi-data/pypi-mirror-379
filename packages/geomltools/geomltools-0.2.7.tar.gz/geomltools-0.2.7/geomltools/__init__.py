"""
GeoML: A Python library for spatial machine learning and geospatial analysis.

This library provides tools for analyzing spatial data,
as well as implementing spatial machine learning algorithms.

Key Features:
- Spatial statistics (e.g., Moran's I, Spatial Variance Ratio, Nearest Neighbor Index)

"""

# Import key functions and classes
from .spatial_statistics.spatial_indices import morans_i, coefficient_of_variation_of_local_variance, test_spatial_index_significance, nearest_neighbor_index
from .spatial_statistics.spatial_relationships import knn_weight_matrix, distance_band_weight_matrix
from .spatial_statistics.descriptive_statistics import spatial_central_tendency


# Optional: Define __all__ to control what gets imported with `from geoml import *`
__all__ = [
    'morans_i',
    'coefficient_of_variation_of_local_variance',
    'test_spatial_index_significance',
    'nearest_neighbor_index',
    'row_standardize_matrix',
    'assign_grid_cell',
    'knn_weight_matrix',
    'distance_band_weight_matrix',
    'grid_contiguity_weight_matrix',
    'spatial_central_tendency'
]


__version__ = "0.2.7" 