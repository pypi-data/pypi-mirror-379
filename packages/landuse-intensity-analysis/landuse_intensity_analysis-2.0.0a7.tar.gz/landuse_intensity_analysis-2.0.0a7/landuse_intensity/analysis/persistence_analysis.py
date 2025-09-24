#!/usr/bin/env python3
"""
📍 PERSISTENCE ANALYSIS MODULE  
==============================

Specialized functions for analyzing persistence patterns in LULC data:
- Class-specific persistence mapping
- Temporal persistence analysis
- Persistence intensity calculations
- Stability zone identification

Author: LULC Package Development Team
"""

import numpy as np
import pandas as pd
from typing import Dict, List, Optional, Tuple
from ..processing.raster import RasterStack


class PersistenceAnalysis:
    """
    Specialized class for analyzing persistence patterns in LULC data.
    """
    
    def __init__(self, raster_stack: RasterStack):
        """
        Initialize PersistenceAnalysis.
        
        Parameters:
        -----------
        raster_stack : RasterStack
            Stack of LULC rasters for analysis
        """
        self.raster_stack = raster_stack
        self.years = raster_stack.years
    
    def generate_persistence_maps(self) -> Dict[str, np.ndarray]:
        """
        Generate comprehensive persistence maps.
        
        Returns:
        --------
        Dict containing various persistence maps
        """
        
        results = {}
        
        # 1. Overall persistence (all periods)
        results['overall_persistence'] = self._calculate_overall_persistence()
        
        # 2. Class-specific persistence maps
        class_persistence = self._calculate_class_persistence()
        results.update(class_persistence)
        
        # 3. Period-specific persistence
        period_persistence = self._calculate_period_persistence()
        results.update(period_persistence)
        
        # 4. Persistence duration map
        results['persistence_duration'] = self._calculate_persistence_duration()
        
        return results
    
    def _calculate_overall_persistence(self) -> np.ndarray:
        """
        Calculate overall persistence across all years.
        
        Returns:
        --------
        np.ndarray: Binary map (1 = persistent throughout, 0 = changed)
        """
        
        first_processor = self.raster_stack.get_processor(self.years[0])
        reference_data = first_processor.data.copy()
        
        # Initialize persistence map (all pixels start as persistent)
        persistence_map = np.ones(reference_data.shape, dtype=np.uint8)
        
        # Check each subsequent year
        for year in self.years[1:]:
            processor = self.raster_stack.get_processor(year)
            
            # Mark pixels that changed as non-persistent
            changed_pixels = reference_data != processor.data
            persistence_map[changed_pixels] = 0
        
        return persistence_map
    
    def _calculate_class_persistence(self) -> Dict[str, np.ndarray]:
        """
        Calculate persistence maps for each individual class.
        
        Returns:
        --------
        Dict with class-specific persistence maps
        """
        
        results = {}
        first_processor = self.raster_stack.get_processor(self.years[0])
        
        # Get all unique classes
        unique_classes = np.unique(first_processor.data)
        
        for class_val in unique_classes:
            class_val_int = int(class_val)
            
            # Initialize class persistence map
            class_mask = (first_processor.data == class_val)
            persistence_map = np.zeros(first_processor.data.shape, dtype=np.uint8)
            
            # For pixels of this class in first year, check persistence
            for year in self.years[1:]:
                processor = self.raster_stack.get_processor(year)
                
                # Check if pixels of this class remained the same
                still_same_class = (processor.data == class_val) & class_mask
                persistence_map[still_same_class] = 1
                
                # Update mask to only include pixels still in this class
                class_mask = class_mask & (processor.data == class_val)
            
            results[f'persistence_class_{class_val_int}'] = persistence_map
        
        return results
    
    def _calculate_period_persistence(self) -> Dict[str, np.ndarray]:
        """
        Calculate persistence for consecutive periods.
        
        Returns:
        --------
        Dict with period-specific persistence maps
        """
        
        results = {}
        
        for i in range(len(self.years) - 1):
            year1, year2 = self.years[i], self.years[i + 1]
            
            processor1 = self.raster_stack.get_processor(year1)
            processor2 = self.raster_stack.get_processor(year2)
            
            # Calculate persistence for this period
            persistence_map = (processor1.data == processor2.data).astype(np.uint8)
            
            results[f'persistence_{year1}_{year2}'] = persistence_map
        
        return results
    
    def _calculate_persistence_duration(self) -> np.ndarray:
        """
        Calculate how long each pixel remained in the same class.
        
        Returns:
        --------
        np.ndarray: Duration map (number of consecutive years unchanged)
        """
        
        first_processor = self.raster_stack.get_processor(self.years[0])
        duration_map = np.ones(first_processor.data.shape, dtype=np.uint8)
        
        # Track current class for each pixel
        current_classes = first_processor.data.copy()
        
        # Check each subsequent year
        for year in self.years[1:]:
            processor = self.raster_stack.get_processor(year)
            
            # Find pixels that remained the same
            same_pixels = (current_classes == processor.data)
            
            # Increment duration for unchanged pixels
            duration_map[same_pixels] += 1
            
            # Reset duration for changed pixels and update their current class
            changed_pixels = ~same_pixels
            duration_map[changed_pixels] = 1
            current_classes[changed_pixels] = processor.data[changed_pixels]
        
        return duration_map
    
    def calculate_persistence_statistics(self) -> pd.DataFrame:
        """
        Calculate comprehensive persistence statistics.
        
        Returns:
        --------
        pd.DataFrame: Persistence statistics by class and period
        """
        
        stats_data = []
        
        # Overall persistence statistics
        persistence_maps = self.generate_persistence_maps()
        overall_persistence = persistence_maps['overall_persistence']
        
        total_pixels = overall_persistence.size
        persistent_pixels = np.sum(overall_persistence)
        persistence_rate = (persistent_pixels / total_pixels) * 100
        
        stats_data.append({
            'Analysis': 'Overall',
            'Class': 'All',
            'Period': f"{self.years[0]}-{self.years[-1]}",
            'Total_Pixels': total_pixels,
            'Persistent_Pixels': persistent_pixels,
            'Persistence_Rate_%': persistence_rate
        })
        
        # Class-specific persistence statistics
        first_processor = self.raster_stack.get_processor(self.years[0])
        unique_classes = np.unique(first_processor.data)
        
        for class_val in unique_classes:
            class_val_int = int(class_val)
            class_persistence_key = f'persistence_class_{class_val_int}'
            
            if class_persistence_key in persistence_maps:
                class_persistence = persistence_maps[class_persistence_key]
                
                # Count pixels of this class in first year
                class_pixels_t1 = np.sum(first_processor.data == class_val)
                
                # Count persistent pixels of this class
                persistent_class_pixels = np.sum(class_persistence)
                
                if class_pixels_t1 > 0:
                    class_persistence_rate = (persistent_class_pixels / class_pixels_t1) * 100
                else:
                    class_persistence_rate = 0
                
                stats_data.append({
                    'Analysis': 'Class-specific',
                    'Class': f'Class_{class_val_int}',
                    'Period': f"{self.years[0]}-{self.years[-1]}",
                    'Total_Pixels': class_pixels_t1,
                    'Persistent_Pixels': persistent_class_pixels,
                    'Persistence_Rate_%': class_persistence_rate
                })
        
        # Period-specific persistence statistics
        for i in range(len(self.years) - 1):
            year1, year2 = self.years[i], self.years[i + 1]
            period_key = f'persistence_{year1}_{year2}'
            
            if period_key in persistence_maps:
                period_persistence = persistence_maps[period_key]
                
                total_pixels = period_persistence.size
                persistent_pixels = np.sum(period_persistence)
                persistence_rate = (persistent_pixels / total_pixels) * 100
                
                stats_data.append({
                    'Analysis': 'Period-specific',
                    'Class': 'All',
                    'Period': f"{year1}-{year2}",
                    'Total_Pixels': total_pixels,
                    'Persistent_Pixels': persistent_pixels,
                    'Persistence_Rate_%': persistence_rate
                })
        
        return pd.DataFrame(stats_data)
    
    def identify_stability_zones(self, min_area_pixels: int = 100) -> Dict[str, np.ndarray]:
        """
        Identify stability zones - areas with high persistence.
        
        Parameters:
        -----------
        min_area_pixels : int
            Minimum area (in pixels) for a stability zone
            
        Returns:
        --------
        Dict with stability zone maps
        """
        
        results = {}
        
        # Overall stability zones
        overall_persistence = self._calculate_overall_persistence()
        results['stability_zones_overall'] = self._filter_small_areas(
            overall_persistence, min_area_pixels
        )
        
        # Class-specific stability zones
        first_processor = self.raster_stack.get_processor(self.years[0])
        unique_classes = np.unique(first_processor.data)
        
        for class_val in unique_classes:
            class_val_int = int(class_val)
            
            # Get class persistence map
            class_persistence = self._calculate_class_persistence()
            class_key = f'persistence_class_{class_val_int}'
            
            if class_key in class_persistence:
                stability_zones = self._filter_small_areas(
                    class_persistence[class_key], min_area_pixels
                )
                results[f'stability_zones_class_{class_val_int}'] = stability_zones
        
        return results
    
    def _filter_small_areas(self, binary_map: np.ndarray, 
                          min_area_pixels: int) -> np.ndarray:
        """
        Filter out small areas from binary map.
        
        Parameters:
        -----------
        binary_map : np.ndarray
            Binary map to filter
        min_area_pixels : int
            Minimum area in pixels
            
        Returns:
        --------
        np.ndarray: Filtered binary map
        """
        
        # This is a simplified version - in practice you'd use 
        # connected component analysis (scipy.ndimage.label)
        from scipy.ndimage import label, sum
        
        # Label connected components
        labeled_array, num_features = label(binary_map)
        
        # Calculate size of each component
        component_sizes = sum(binary_map, labeled_array, range(num_features + 1))
        
        # Create mask for components larger than minimum size
        size_mask = component_sizes >= min_area_pixels
        
        # Apply mask
        filtered_map = np.isin(labeled_array, np.where(size_mask)[0])
        
        return filtered_map.astype(np.uint8)
    
    def calculate_persistence_intensity(self) -> np.ndarray:
        """
        Calculate persistence intensity based on duration and stability.
        
        Returns:
        --------
        np.ndarray: Persistence intensity map (0-100 scale)
        """
        
        # Get duration map
        duration_map = self._calculate_persistence_duration()
        
        # Normalize to 0-100 scale based on maximum possible duration
        max_duration = len(self.years)
        intensity_map = (duration_map.astype(np.float32) / max_duration * 100).astype(np.uint8)
        
        return intensity_map