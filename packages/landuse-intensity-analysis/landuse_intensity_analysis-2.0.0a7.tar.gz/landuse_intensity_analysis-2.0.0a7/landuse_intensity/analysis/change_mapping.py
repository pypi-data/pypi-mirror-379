#!/usr/bin/env python3
"""
🗺️ CHANGE MAPPING MODULE
========================

Specialized functions for generating change maps, including:
- Binary change detection maps
- Cumulative change analysis
- Transition-specific maps
- Multi-temporal change patterns

Author: LULC Package Development Team
"""

import numpy as np
from typing import Dict, List, Optional, Tuple
from ..processing.raster import RasterStack


class ChangeMapping:
    """
    Specialized class for generating various types of change maps.
    """
    
    def __init__(self, raster_stack: RasterStack):
        """
        Initialize ChangeMapping.
        
        Parameters:
        -----------
        raster_stack : RasterStack
            Stack of LULC rasters for analysis
        """
        self.raster_stack = raster_stack
        self.years = raster_stack.years
    
    def create_change_map(self, year1: int, year2: int, 
                         change_type: str = 'binary') -> np.ndarray:
        """
        Create change map between two years.
        
        Parameters:
        -----------
        year1, year2 : int
            Years to compare
        change_type : str
            'binary', 'transition', or 'intensity'
            
        Returns:
        --------
        np.ndarray: Change map
        """
        
        processor1 = self.raster_stack.get_processor(year1)
        processor2 = self.raster_stack.get_processor(year2)
        
        if change_type == 'binary':
            # Simple binary change map (0 = no change, 1 = change)
            return (processor1.data != processor2.data).astype(np.uint8)
        
        elif change_type == 'transition':
            # Transition map showing from->to class codes
            # Formula: from_class * 10 + to_class (assumes classes 1-9)
            change_map = np.where(
                processor1.data != processor2.data,
                processor1.data * 10 + processor2.data,
                0  # No change
            )
            return change_map.astype(np.uint16)
        
        elif change_type == 'intensity':
            # Change intensity based on class distance
            class_hierarchy = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5}  # Can be customized
            
            intensity_map = np.abs(
                processor1.data.astype(np.float32) - 
                processor2.data.astype(np.float32)
            )
            
            return intensity_map.astype(np.uint8)
    
    def create_cumulative_change_map(self) -> np.ndarray:
        """
        Create cumulative change map showing areas that changed in any period.
        
        Returns:
        --------
        np.ndarray: Cumulative change map (0 = never changed, >0 = number of times changed)
        """
        
        # Initialize cumulative change map
        first_processor = self.raster_stack.get_processor(self.years[0])
        cumulative_change = np.zeros(first_processor.data.shape, dtype=np.uint8)
        
        # Add changes for each consecutive period
        for i in range(len(self.years) - 1):
            year1, year2 = self.years[i], self.years[i + 1]
            change_map = self.create_change_map(year1, year2, 'binary')
            cumulative_change += change_map
        
        return cumulative_change
    
    def create_net_change_map(self, from_class: int, to_class: int) -> np.ndarray:
        """
        Create map showing net change from one specific class to another.
        
        Parameters:
        -----------
        from_class, to_class : int
            Classes to analyze transition between
            
        Returns:
        --------
        np.ndarray: Net change map (1 = transition occurred, 0 = no transition)
        """
        
        first_processor = self.raster_stack.get_processor(self.years[0])
        last_processor = self.raster_stack.get_processor(self.years[-1])
        
        # Find pixels that changed from from_class to to_class
        transition_map = np.where(
            (first_processor.data == from_class) & (last_processor.data == to_class),
            1,  # Transition occurred
            0   # No transition
        )
        
        return transition_map.astype(np.uint8)
    
    def create_stability_map(self) -> np.ndarray:
        """
        Create stability map showing areas that never changed.
        
        Returns:
        --------
        np.ndarray: Stability map (1 = stable, 0 = changed at some point)
        """
        
        cumulative_change = self.create_cumulative_change_map()
        stability_map = (cumulative_change == 0).astype(np.uint8)
        
        return stability_map
    
    def create_change_frequency_map(self) -> np.ndarray:
        """
        Create map showing frequency of change (how many times each pixel changed).
        
        Returns:
        --------
        np.ndarray: Change frequency map
        """
        
        return self.create_cumulative_change_map()  # Same as cumulative
    
    def create_first_change_map(self) -> np.ndarray:
        """
        Create map showing the first year when change occurred.
        
        Returns:
        --------
        np.ndarray: First change map (year when first change occurred, 0 = never changed)
        """
        
        first_processor = self.raster_stack.get_processor(self.years[0])
        first_change_map = np.zeros(first_processor.data.shape, dtype=np.uint16)
        
        # Check each consecutive period
        for i in range(len(self.years) - 1):
            year1, year2 = self.years[i], self.years[i + 1]
            change_map = self.create_change_map(year1, year2, 'binary')
            
            # Mark first change year (only if not already marked)
            mask = (change_map == 1) & (first_change_map == 0)
            first_change_map[mask] = year2
        
        return first_change_map
    
    def create_last_change_map(self) -> np.ndarray:
        """
        Create map showing the last year when change occurred.
        
        Returns:
        --------
        np.ndarray: Last change map (year of most recent change, 0 = never changed)
        """
        
        first_processor = self.raster_stack.get_processor(self.years[0])
        last_change_map = np.zeros(first_processor.data.shape, dtype=np.uint16)
        
        # Check each consecutive period (update whenever change is found)
        for i in range(len(self.years) - 1):
            year1, year2 = self.years[i], self.years[i + 1]
            change_map = self.create_change_map(year1, year2, 'binary')
            
            # Update last change year
            mask = change_map == 1
            last_change_map[mask] = year2
        
        return last_change_map
    
    def create_change_direction_map(self, class_hierarchy: Dict[int, int] = None) -> np.ndarray:
        """
        Create map showing direction of change (increasing/decreasing class values).
        
        Parameters:
        -----------
        class_hierarchy : Dict[int, int], optional
            Mapping of class to hierarchical value for direction analysis
            
        Returns:
        --------
        np.ndarray: Direction map (1 = increasing, -1 = decreasing, 0 = no change)
        """
        
        if class_hierarchy is None:
            # Default: use class values directly
            class_hierarchy = {i: i for i in range(1, 10)}
        
        first_processor = self.raster_stack.get_processor(self.years[0])
        last_processor = self.raster_stack.get_processor(self.years[-1])
        
        # Map class values to hierarchy
        first_hierarchy = np.zeros_like(first_processor.data, dtype=np.float32)
        last_hierarchy = np.zeros_like(last_processor.data, dtype=np.float32)
        
        for class_val, hierarchy_val in class_hierarchy.items():
            first_hierarchy[first_processor.data == class_val] = hierarchy_val
            last_hierarchy[last_processor.data == class_val] = hierarchy_val
        
        # Calculate direction
        direction_map = np.zeros_like(first_processor.data, dtype=np.int8)
        
        # Increasing hierarchy
        direction_map[last_hierarchy > first_hierarchy] = 1
        
        # Decreasing hierarchy  
        direction_map[last_hierarchy < first_hierarchy] = -1
        
        # No change = 0 (default)
        
        return direction_map