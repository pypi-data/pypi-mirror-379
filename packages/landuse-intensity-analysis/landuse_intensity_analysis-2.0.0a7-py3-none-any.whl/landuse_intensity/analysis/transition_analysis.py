#!/usr/bin/env python3
"""
🔄 TRANSITION ANALYSIS MODULE
============================

Specialized functions for analyzing land use transitions:
- Transition probability matrices
- Transition flow analysis
- Dominant transition identification
- Transition hotspot mapping

Author: LULC Package Development Team
"""

import numpy as np
import pandas as pd
from typing import Dict, List, Optional, Tuple
from pathlib import Path
import rasterio
from rasterio.transform import from_origin
from ..processing.raster import RasterStack


class TransitionAnalysis:
    """
    Specialized class for analyzing transition patterns in LULC data.
    """
    
    def __init__(self, raster_stack: RasterStack):
        """
        Initialize TransitionAnalysis.
        
        Parameters:
        -----------
        raster_stack : RasterStack
            Stack of LULC rasters for analysis
        """
        self.raster_stack = raster_stack
        self.years = raster_stack.years
    
    def calculate_transition_matrices(self) -> Dict[str, pd.DataFrame]:
        """
        Calculate transition matrices for all periods.
        
        Returns:
        --------
        Dict containing transition matrices for each period
        """
        
        results = {}
        
        for i in range(len(self.years) - 1):
            year1, year2 = self.years[i], self.years[i + 1]
            
            processor1 = self.raster_stack.get_processor(year1)
            processor2 = self.raster_stack.get_processor(year2)
            
            # Create contingency table
            transition_matrix = pd.crosstab(
                processor1.data.flatten(),
                processor2.data.flatten(),
                margins=False
            )
            
            results[f"{year1}-{year2}"] = transition_matrix
        
        return results
    
    def calculate_transition_probabilities(self) -> Dict[str, pd.DataFrame]:
        """
        Calculate transition probability matrices (row-normalized).
        
        Returns:
        --------
        Dict containing probability matrices for each period
        """
        
        transition_matrices = self.calculate_transition_matrices()
        probability_matrices = {}
        
        for period, matrix in transition_matrices.items():
            # Row-normalize to get probabilities
            row_sums = matrix.sum(axis=1)
            prob_matrix = matrix.div(row_sums, axis=0).fillna(0)
            probability_matrices[period] = prob_matrix
        
        return probability_matrices
    
    def identify_dominant_transitions(self, min_pixels: int = 100) -> Dict[str, List[Dict]]:
        """
        Identify dominant transitions for each period.
        
        Parameters:
        -----------
        min_pixels : int
            Minimum number of pixels for a transition to be considered dominant
            
        Returns:
        --------
        Dict containing dominant transitions for each period
        """
        
        transition_matrices = self.calculate_transition_matrices()
        dominant_transitions = {}
        
        for period, matrix in transition_matrices.items():
            transitions = []
            
            # Find off-diagonal elements (actual transitions) above threshold
            for from_class in matrix.index:
                for to_class in matrix.columns:
                    if from_class != to_class:  # Only actual transitions
                        pixel_count = matrix.loc[from_class, to_class]
                        
                        if pixel_count >= min_pixels:
                            # Calculate percentage of total changes
                            total_changes = matrix.sum().sum() - np.diag(matrix).sum()
                            change_percentage = (pixel_count / total_changes) * 100 if total_changes > 0 else 0
                            
                            transitions.append({
                                'from_class': int(from_class),
                                'to_class': int(to_class),
                                'pixel_count': pixel_count,
                                'change_percentage': change_percentage
                            })
            
            # Sort by pixel count (descending)
            transitions.sort(key=lambda x: x['pixel_count'], reverse=True)
            dominant_transitions[period] = transitions
        
        return dominant_transitions
    
    def create_transition_hotspot_maps(self) -> Dict[str, np.ndarray]:
        """
        Create maps showing hotspots of specific transitions.
        
        Returns:
        --------
        Dict containing hotspot maps for major transitions
        """
        
        hotspot_maps = {}
        
        # Get dominant transitions
        dominant_transitions = self.identify_dominant_transitions()
        
        # Create maps for top transitions in each period
        for period, transitions in dominant_transitions.items():
            year1, year2 = period.split('-')
            year1, year2 = int(year1), int(year2)
            
            processor1 = self.raster_stack.get_processor(year1)
            processor2 = self.raster_stack.get_processor(year2)
            
            # Create maps for top 3 transitions in this period
            for i, trans in enumerate(transitions[:3]):
                from_class = trans['from_class']
                to_class = trans['to_class']
                
                # Create binary map showing where this transition occurred
                transition_map = np.where(
                    (processor1.data == from_class) & (processor2.data == to_class),
                    1,  # Transition occurred
                    0   # No transition
                ).astype(np.uint8)
                
                map_key = f"hotspot_{period}_rank{i+1}_{from_class}to{to_class}"
                hotspot_maps[map_key] = transition_map
        
        return hotspot_maps
    
    def calculate_transition_flow_statistics(self) -> pd.DataFrame:
        """
        Calculate comprehensive transition flow statistics.
        
        Returns:
        --------
        pd.DataFrame: Transition flow statistics
        """
        
        flow_data = []
        transition_matrices = self.calculate_transition_matrices()
        probability_matrices = self.calculate_transition_probabilities()
        
        for period in transition_matrices.keys():
            matrix = transition_matrices[period]
            prob_matrix = probability_matrices[period]
            
            year1, year2 = period.split('-')
            time_interval = int(year2) - int(year1)
            
            for from_class in matrix.index:
                for to_class in matrix.columns:
                    if from_class != to_class:  # Only actual transitions
                        pixel_count = matrix.loc[from_class, to_class]
                        probability = prob_matrix.loc[from_class, to_class]
                        
                        if pixel_count > 0:  # Only record actual transitions
                            # Calculate annual transition rate
                            annual_rate = (pixel_count / matrix.loc[from_class, :].sum()) / time_interval * 100
                            
                            flow_data.append({
                                'period': period,
                                'from_class': int(from_class),
                                'to_class': int(to_class),
                                'pixel_count': pixel_count,
                                'probability': probability,
                                'annual_rate_%': annual_rate,
                                'time_interval': time_interval
                            })
        
        return pd.DataFrame(flow_data)
    
    def analyze_transition_patterns(self) -> Dict[str, pd.DataFrame]:
        """
        Analyze patterns in transitions across all periods.
        
        Returns:
        --------
        Dict containing various transition pattern analyses
        """
        
        results = {}
        
        # 1. Transition consistency analysis
        flow_stats = self.calculate_transition_flow_statistics()
        
        # Group by transition type and analyze consistency
        transition_groups = flow_stats.groupby(['from_class', 'to_class'])
        
        consistency_data = []
        for (from_class, to_class), group in transition_groups:
            if len(group) > 1:  # Only analyze transitions that occur in multiple periods
                rates = group['annual_rate_%'].values
                mean_rate = np.mean(rates)
                std_rate = np.std(rates)
                cv = (std_rate / mean_rate) * 100 if mean_rate > 0 else 0
                
                consistency_data.append({
                    'from_class': from_class,
                    'to_class': to_class,
                    'num_periods': len(group),
                    'mean_annual_rate_%': mean_rate,
                    'std_annual_rate_%': std_rate,
                    'coefficient_variation_%': cv,
                    'consistency': 'High' if cv < 25 else 'Medium' if cv < 50 else 'Low'
                })
        
        results['transition_consistency'] = pd.DataFrame(consistency_data)
        
        # 2. Transition directionality analysis
        directionality_data = []
        
        for period in flow_stats['period'].unique():
            period_data = flow_stats[flow_stats['period'] == period]
            
            # Analyze bidirectional transitions
            for from_class in period_data['from_class'].unique():
                for to_class in period_data['to_class'].unique():
                    if from_class != to_class:
                        # Forward transition
                        forward = period_data[
                            (period_data['from_class'] == from_class) & 
                            (period_data['to_class'] == to_class)
                        ]
                        
                        # Reverse transition
                        reverse = period_data[
                            (period_data['from_class'] == to_class) & 
                            (period_data['to_class'] == from_class)
                        ]
                        
                        if not forward.empty and not reverse.empty:
                            forward_pixels = forward.iloc[0]['pixel_count']
                            reverse_pixels = reverse.iloc[0]['pixel_count']
                            
                            net_flow = forward_pixels - reverse_pixels
                            total_flow = forward_pixels + reverse_pixels
                            
                            if total_flow > 0:
                                dominance_ratio = abs(net_flow) / total_flow
                                
                                directionality_data.append({
                                    'period': period,
                                    'class_pair': f"{min(from_class, to_class)}-{max(from_class, to_class)}",
                                    'dominant_direction': f"{from_class}→{to_class}" if net_flow > 0 else f"{to_class}→{from_class}",
                                    'forward_pixels': forward_pixels,
                                    'reverse_pixels': reverse_pixels,
                                    'net_flow': abs(net_flow),
                                    'dominance_ratio': dominance_ratio
                                })
        
        results['transition_directionality'] = pd.DataFrame(directionality_data)
        
        # 3. Transition velocity analysis (rate of change)
        velocity_data = []
        
        for period in flow_stats['period'].unique():
            period_data = flow_stats[flow_stats['period'] == period]
            
            for _, row in period_data.iterrows():
                # Calculate transition velocity (pixels per year)
                velocity = row['pixel_count'] / row['time_interval']
                
                velocity_data.append({
                    'period': period,
                    'transition': f"{row['from_class']}→{row['to_class']}",
                    'pixels_per_year': velocity,
                    'annual_rate_%': row['annual_rate_%']
                })
        
        results['transition_velocity'] = pd.DataFrame(velocity_data)
        
        return results
    
    def create_transition_summary_map(self, top_n: int = 3) -> np.ndarray:
        """
        Create a summary map showing the most important transitions.
        
        Parameters:
        -----------
        top_n : int
            Number of top transitions to include
            
        Returns:
        --------
        np.ndarray: Summary map with coded transitions
        """
        
        # Get first and last year for overall transition
        first_processor = self.raster_stack.get_processor(self.years[0])
        last_processor = self.raster_stack.get_processor(self.years[-1])
        
        # Calculate overall transition matrix
        overall_matrix = pd.crosstab(
            first_processor.data.flatten(),
            last_processor.data.flatten(),
            margins=False
        )
        
        # Find top transitions
        transitions = []
        for from_class in overall_matrix.index:
            for to_class in overall_matrix.columns:
                if from_class != to_class:
                    pixel_count = overall_matrix.loc[from_class, to_class]
                    transitions.append({
                        'from_class': from_class,
                        'to_class': to_class,
                        'pixel_count': pixel_count,
                        'code': from_class * 10 + to_class
                    })
        
        # Sort and get top N
        transitions.sort(key=lambda x: x['pixel_count'], reverse=True)
        top_transitions = transitions[:top_n]
        
        # Create summary map
        summary_map = np.zeros(first_processor.data.shape, dtype=np.uint16)
        
        for i, trans in enumerate(top_transitions):
            # Mark pixels where this transition occurred
            mask = (first_processor.data == trans['from_class']) & (last_processor.data == trans['to_class'])
            summary_map[mask] = i + 1  # Use simple codes 1, 2, 3, etc.
        
        return summary_map
    
    def save_map_as_tiff(self, map_data: np.ndarray, output_file: Path) -> None:
        """
        Save a map as GeoTIFF file.
        
        Parameters:
        -----------
        map_data : np.ndarray
            Map data to save
        output_file : Path
            Output file path
        """
        
        # Get reference raster for georeferencing
        reference_processor = self.raster_stack.get_processor(self.years[0])
        
        # Create output directory if it doesn't exist
        output_file.parent.mkdir(parents=True, exist_ok=True)
        
        # Define transform (simple identity transform if no georeferencing)
        transform = from_origin(-180, 90, 1.0, 1.0)  # Default transform
        
        with rasterio.open(
            output_file,
            'w',
            driver='GTiff',
            height=map_data.shape[0],
            width=map_data.shape[1],
            count=1,
            dtype=map_data.dtype,
            transform=transform,
            crs='EPSG:4326'  # Default to WGS84
        ) as dst:
            dst.write(map_data, 1)