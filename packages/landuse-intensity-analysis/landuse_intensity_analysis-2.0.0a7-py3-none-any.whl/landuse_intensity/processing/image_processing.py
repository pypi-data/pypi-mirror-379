"""
Essential image processing for land use change analysis.

Simplified image processing functions focusing on core functionality
needed for contingency table generation and basic spatial analysis.
"""

import numpy as np
from typing import Tuple, Optional, Dict, List
from scipy import ndimage


def create_contingency_table(raster1: np.ndarray, raster2: np.ndarray, 
                            labels1: Optional[List] = None, 
                            labels2: Optional[List] = None) -> np.ndarray:
    """
    Create contingency table from two raster arrays.
    
    Parameters
    ----------
    raster1 : np.ndarray
        First time period raster
    raster2 : np.ndarray  
        Second time period raster
    labels1 : list, optional
        Labels for raster1 classes
    labels2 : list, optional
        Labels for raster2 classes
        
    Returns
    -------
    np.ndarray
        Contingency table showing transitions between time periods
    """
    # Validate inputs
    if raster1.shape != raster2.shape:
        raise ValueError("Rasters must have the same shape")
    
    # Get unique values
    unique1 = np.unique(raster1)
    unique2 = np.unique(raster2)
    
    # Create contingency table
    contingency = np.zeros((len(unique1), len(unique2)), dtype=int)
    
    for i, val1 in enumerate(unique1):
        for j, val2 in enumerate(unique2):
            mask = (raster1 == val1) & (raster2 == val2)
            contingency[i, j] = np.sum(mask)
    
    return contingency


def calculate_change_map(raster1: np.ndarray, raster2: np.ndarray) -> np.ndarray:
    """
    Calculate binary change map.
    
    Parameters
    ----------
    raster1 : np.ndarray
        First time period
    raster2 : np.ndarray
        Second time period
        
    Returns
    -------
    np.ndarray
        Binary change map (1 = change, 0 = no change)
    """
    return (raster1 != raster2).astype(int)


class ImageProcessor:
    """
    Image processor for LULC analysis operations.
    
    Provides methods for spatial analysis, filtering, and morphological
    operations commonly used in land use change analysis.
    """
    
    def __init__(self):
        """Initialize ImageProcessor."""
        pass
    
    @staticmethod
    def smooth_raster(raster: np.ndarray, kernel_size: int = 3, 
                     method: str = 'median') -> np.ndarray:
        """
        Smooth raster data using filtering operations.
        
        Parameters
        ----------
        raster : np.ndarray
            Input raster data
        kernel_size : int
            Size of smoothing kernel
        method : str
            Smoothing method ('median', 'gaussian', 'uniform')
            
        Returns
        -------
        np.ndarray
            Smoothed raster data
        """
        if method == 'median':
            return ndimage.median_filter(raster, size=kernel_size)
        elif method == 'gaussian':
            sigma = kernel_size / 3.0
            return ndimage.gaussian_filter(raster, sigma=sigma)
        elif method == 'uniform':
            return ndimage.uniform_filter(raster, size=kernel_size)
        else:
            raise ValueError(f"Unknown smoothing method: {method}")
    
    @staticmethod
    def remove_small_patches(raster: np.ndarray, min_size: int = 4) -> np.ndarray:
        """
        Remove small isolated patches from raster data.
        
        Parameters
        ----------
        raster : np.ndarray
            Input raster data
        min_size : int
            Minimum patch size to keep
            
        Returns
        -------
        np.ndarray
            Filtered raster data
        """
        unique_vals = np.unique(raster)
        output = raster.copy()
        
        for val in unique_vals:
            # Create binary mask for current class
            binary_mask = (raster == val).astype(int)
            
            # Label connected components
            labeled, num_features = ndimage.label(binary_mask)
            
            # Get sizes of each component
            for i in range(1, num_features + 1):
                component_size = np.sum(labeled == i)
                if component_size < min_size:
                    # Remove small patches by setting to most common neighbor
                    patch_mask = labeled == i
                    neighbors = raster[ndimage.binary_dilation(patch_mask) & ~patch_mask]
                    if len(neighbors) > 0:
                        most_common = np.bincount(neighbors).argmax()
                        output[patch_mask] = most_common
        
        return output
    
    @staticmethod
    def calculate_patch_metrics(raster: np.ndarray, class_val: int) -> Dict[str, float]:
        """
        Calculate patch-level metrics for a specific land use class.
        
        Parameters
        ----------
        raster : np.ndarray
            Input raster data
        class_val : int
            Class value to analyze
            
        Returns
        -------
        dict
            Dictionary with patch metrics
        """
        # Create binary mask for the class
        binary_mask = (raster == class_val).astype(int)
        
        # Label patches
        labeled, num_patches = ndimage.label(binary_mask)
        
        if num_patches == 0:
            return {
                'num_patches': 0,
                'total_area': 0,
                'mean_patch_size': 0,
                'largest_patch_size': 0,
                'patch_density': 0
            }
        
        # Calculate patch sizes
        patch_sizes = []
        for i in range(1, num_patches + 1):
            patch_size = np.sum(labeled == i)
            patch_sizes.append(patch_size)
        
        total_area = np.sum(binary_mask)
        raster_area = raster.shape[0] * raster.shape[1]
        
        return {
            'num_patches': num_patches,
            'total_area': total_area,
            'mean_patch_size': np.mean(patch_sizes),
            'largest_patch_size': np.max(patch_sizes),
            'patch_density': num_patches / raster_area * 10000  # patches per 10,000 pixels
        }
    
    @staticmethod
    def create_buffer_zones(raster: np.ndarray, class_val: int, 
                           buffer_size: int = 1) -> np.ndarray:
        """
        Create buffer zones around patches of a specific class.
        
        Parameters
        ----------
        raster : np.ndarray
            Input raster data
        class_val : int
            Class value to create buffers around
        buffer_size : int
            Buffer size in pixels
            
        Returns
        -------
        np.ndarray
            Binary mask showing buffer zones
        """
        # Create binary mask for the class
        binary_mask = (raster == class_val).astype(bool)
        
        # Create structure element for dilation
        structure = ndimage.generate_binary_structure(2, 1)  # 4-connectivity
        
        # Apply dilation multiple times for larger buffers
        buffer_mask = binary_mask.copy()
        for _ in range(buffer_size):
            buffer_mask = ndimage.binary_dilation(buffer_mask, structure=structure)
        
        # Remove the original class pixels to get only the buffer
        buffer_only = buffer_mask & ~binary_mask
        
        return buffer_only.astype(int)
    
    @staticmethod
    def calculate_edge_density(raster: np.ndarray) -> float:
        """
        Calculate edge density of the raster (total edge length per unit area).
        
        Parameters
        ----------
        raster : np.ndarray
            Input raster data
            
        Returns
        -------
        float
            Edge density value
        """
        # Calculate horizontal edges
        h_edges = np.sum(raster[:, :-1] != raster[:, 1:])
        
        # Calculate vertical edges
        v_edges = np.sum(raster[:-1, :] != raster[1:, :])
        
        # Total edge length
        total_edges = h_edges + v_edges
        
        # Total area
        total_area = raster.shape[0] * raster.shape[1]
        
        return total_edges / total_area
    
    @staticmethod
    def create_distance_map(raster: np.ndarray, class_val: int) -> np.ndarray:
        """
        Create distance map from pixels of a specific class.
        
        Parameters
        ----------
        raster : np.ndarray
            Input raster data
        class_val : int
            Class value to calculate distances from
            
        Returns
        -------
        np.ndarray
            Distance map (Euclidean distances)
        """
        # Create binary mask for the class
        binary_mask = (raster == class_val).astype(bool)
        
        # Calculate distance transform
        distance_map = ndimage.distance_transform_edt(~binary_mask)
        
        return distance_map



