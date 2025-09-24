#!/usr/bin/env python3
"""
🌍 LULC ANALYSIS MODULE
======================

Comprehensive Land Use Land Cover analysis functions following the API design 
patterns of OpenLand, Pontius, and other established LULC packages.

This module provides a unified interface for:
- Multi-temporal LULC analysis
- Transition matrices and contingency tables
- Change detection and persistence mapping
- Sankey diagrams and visualizations
- Intensity analysis (Pontius methodology)
- Spatial analysis of changes

Author: LULC Package Development Team
Date: September 2025
"""

import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from pathlib import Path
from typing import Dict, List, Tuple, Optional, Union
import rasterio
from rasterio.transform import from_origin
import warnings

from ..processing.raster import RasterProcessor, RasterStack
from ..utils.utils import create_output_directory, validate_data
from .change_mapping import ChangeMapping
from .persistence_analysis import PersistenceAnalysis
from .transition_analysis import TransitionAnalysis


class LULCAnalysis:
    """
    Main class for comprehensive LULC analysis following OpenLand/Pontius patterns.
    
    This class provides a unified interface for all LULC analysis functions,
    similar to OpenLand's contingencyTable() -> intensityAnalysis() workflow.
    """
    
    def __init__(self, raster_stack: Union[RasterStack, List[str]], 
                 years: List[int] = None,
                 class_names: Dict[int, str] = None,
                 output_dir: str = None):
        """
        Initialize LULC Analysis.
        
        Parameters:
        -----------
        raster_stack : RasterStack or List of file paths
            Stack of LULC rasters for temporal analysis
        years : List[int], optional
            Years corresponding to each raster
        class_names : Dict[int, str], optional
            Mapping of class values to names
        output_dir : str, optional
            Output directory for results
        """
        
        if isinstance(raster_stack, list):
            self.raster_stack = RasterStack(raster_stack, years)
        else:
            self.raster_stack = raster_stack
            
        self.years = years or self.raster_stack.years
        self.class_names = class_names or self._generate_class_names()
        
        self.output_dir = Path(output_dir) if output_dir else Path(create_output_directory("lulc_analysis"))
        
        # Analysis results storage
        self.contingency_tables = {}
        self.area_statistics = None
        self.transition_matrices = {}
        self.change_maps = {}
        self.persistence_maps = {}
        self.intensity_results = {}
        
        # Analysis modules
        self.change_mapping = ChangeMapping(self.raster_stack)
        self.persistence_analysis = PersistenceAnalysis(self.raster_stack)
        self.transition_analysis = TransitionAnalysis(self.raster_stack)
        
        print(f"🌍 LULC Analysis initialized")
        print(f"   📅 Years: {self.years}")
        print(f"   🎯 Classes: {len(self.class_names)}")
        print(f"   📁 Output: {self.output_dir}")
    
    def _generate_class_names(self) -> Dict[int, str]:
        """Generate default class names from unique values."""
        # Get unique values from first raster
        processor = self.raster_stack.get_processor(self.years[0])
        unique_vals = processor.get_unique_values()
        return {int(val): f"Class_{int(val)}" for val in unique_vals}
    
    def contingency_table(self, multistep: bool = True, 
                         onestep: bool = True) -> Dict:
        """
        Generate contingency tables (OpenLand-style function).
        
        Parameters:
        -----------
        multistep : bool
            Generate tables for all consecutive year pairs
        onestep : bool  
            Generate table for first->last year only
            
        Returns:
        --------
        Dict with contingency tables and metadata
        """
        print("\\n📊 GENERATING CONTINGENCY TABLES")
        print("=" * 40)
        
        results = {
            'lulc_Multistep': {},
            'lulc_Onestep': None,
            'totalArea': {},
            'tb_legend': self.class_names,
            'years': self.years
        }
        
        # Multi-step contingency tables (consecutive years)
        if multistep:
            for i in range(len(self.years) - 1):
                year1, year2 = self.years[i], self.years[i + 1]
                transition_key = f"{year1}-{year2}"
                
                p1 = self.raster_stack.get_processor(year1)
                p2 = self.raster_stack.get_processor(year2)
                
                contingency = pd.crosstab(
                    p1.data.flatten(), 
                    p2.data.flatten(),
                    margins=False
                )
                
                results['lulc_Multistep'][transition_key] = contingency
                print(f"   ✅ {transition_key}: {contingency.shape}")
        
        # One-step contingency table (first -> last year)
        if onestep and len(self.years) >= 2:
            first_year, last_year = self.years[0], self.years[-1]
            
            p1 = self.raster_stack.get_processor(first_year)
            p2 = self.raster_stack.get_processor(last_year)
            
            onestep_table = pd.crosstab(
                p1.data.flatten(),
                p2.data.flatten(), 
                margins=False
            )
            
            results['lulc_Onestep'] = onestep_table
            print(f"   ✅ One-step ({first_year}-{last_year}): {onestep_table.shape}")
        
        # Calculate total areas by year
        for year in self.years:
            processor = self.raster_stack.get_processor(year)
            unique_classes, counts = np.unique(processor.data, return_counts=True)
            
            # Convert to areas (assuming 30m pixels for now)
            pixel_area_km2 = (30 * 30) / 1_000_000
            areas = {}
            
            for cls, count in zip(unique_classes, counts):
                areas[int(cls)] = count * pixel_area_km2
            
            results['totalArea'][year] = areas
        
        self.contingency_tables = results
        
        # Save contingency tables
        tables_dir = self.output_dir / "contingency_tables"
        tables_dir.mkdir(exist_ok=True)
        
        for key, table in results['lulc_Multistep'].items():
            output_file = tables_dir / f"contingency_{key}.csv"
            table.to_csv(output_file)
        
        if results['lulc_Onestep'] is not None:
            output_file = tables_dir / f"contingency_onestep_{self.years[0]}_{self.years[-1]}.csv"
            results['lulc_Onestep'].to_csv(output_file)
        
        print(f"   💾 Tables saved to: {tables_dir}")
        
        return results
    
    def intensity_analysis(self, contingency_results: Dict = None) -> Dict:
        """
        Perform Pontius Intensity Analysis on three levels.
        
        Parameters:
        -----------
        contingency_results : Dict, optional
            Results from contingency_table(), if None will generate
            
        Returns:
        --------
        Dict with intensity analysis results
        """
        if contingency_results is None:
            contingency_results = self.contingency_table()
        
        print("\\n🔍 PERFORMING INTENSITY ANALYSIS")
        print("=" * 35)
        
        results = {
            'interval_level': {},
            'category_level': {},
            'transition_level': {},
            'uniform_intensity': None
        }
        
        # Level 1: Interval Analysis
        print("   📊 Level 1: Interval Analysis")
        
        interval_data = []
        total_domain = sum(list(contingency_results['totalArea'][self.years[0]].values()))
        
        for transition, table in contingency_results['lulc_Multistep'].items():
            year1, year2 = transition.split('-')
            time_interval = int(year2) - int(year1)
            
            # Calculate change area
            total_pixels = table.sum().sum()
            stable_pixels = np.diag(table).sum()
            change_pixels = total_pixels - stable_pixels
            
            # Annual rate of change
            annual_change = (change_pixels / total_pixels) / time_interval * 100
            
            interval_data.append({
                'transition': transition,
                'time_interval': time_interval,
                'change_pixels': change_pixels,
                'total_pixels': total_pixels,
                'annual_change_%': annual_change
            })
        
        results['interval_level'] = pd.DataFrame(interval_data)
        
        # Uniform intensity (average across all intervals)
        results['uniform_intensity'] = results['interval_level']['annual_change_%'].mean()
        
        print(f"      ✅ Uniform intensity: {results['uniform_intensity']:.2f}% per year")
        
        # Level 2: Category Analysis  
        print("   📊 Level 2: Category Analysis")
        
        category_data = []
        for transition, table in contingency_results['lulc_Multistep'].items():
            year1, year2 = transition.split('-')
            time_interval = int(year2) - int(year1)
            
            for class_val in table.index:
                # Loss analysis
                gross_loss = table.loc[class_val, :].sum() - table.loc[class_val, class_val]
                total_t1 = table.loc[class_val, :].sum()
                
                if total_t1 > 0:
                    annual_loss = (gross_loss / total_t1) / time_interval * 100
                else:
                    annual_loss = 0
                
                # Gain analysis  
                gross_gain = table.loc[:, class_val].sum() - table.loc[class_val, class_val]
                total_t2 = table.loc[:, class_val].sum()
                
                if total_t2 > 0:
                    annual_gain = (gross_gain / total_t2) / time_interval * 100
                else:
                    annual_gain = 0
                
                category_data.append({
                    'transition': transition,
                    'class': int(class_val),
                    'class_name': self.class_names.get(int(class_val), f'Class_{class_val}'),
                    'annual_loss_%': annual_loss,
                    'annual_gain_%': annual_gain,
                    'net_change_%': annual_gain - annual_loss
                })
        
        results['category_level'] = pd.DataFrame(category_data)
        
        # Level 3: Transition Analysis
        print("   📊 Level 3: Transition Analysis")
        
        transition_data = []
        for transition, table in contingency_results['lulc_Multistep'].items():
            year1, year2 = transition.split('-')
            time_interval = int(year2) - int(year1)
            
            for from_class in table.index:
                for to_class in table.columns:
                    if from_class != to_class:  # Only actual transitions
                        transition_pixels = table.loc[from_class, to_class]
                        total_from = table.loc[from_class, :].sum()
                        
                        if total_from > 0 and transition_pixels > 0:
                            annual_transition = (transition_pixels / total_from) / time_interval * 100
                            
                            transition_data.append({
                                'period': transition,
                                'from_class': int(from_class),
                                'to_class': int(to_class),
                                'from_name': self.class_names.get(int(from_class), f'Class_{from_class}'),
                                'to_name': self.class_names.get(int(to_class), f'Class_{to_class}'),
                                'transition_pixels': transition_pixels,
                                'annual_transition_%': annual_transition
                            })
        
        results['transition_level'] = pd.DataFrame(transition_data)
        
        self.intensity_results = results
        
        # Save intensity analysis results
        intensity_dir = self.output_dir / "intensity_analysis"
        intensity_dir.mkdir(exist_ok=True)
        
        results['interval_level'].to_csv(intensity_dir / "interval_analysis.csv", index=False)
        results['category_level'].to_csv(intensity_dir / "category_analysis.csv", index=False)
        results['transition_level'].to_csv(intensity_dir / "transition_analysis.csv", index=False)
        
        print(f"   💾 Results saved to: {intensity_dir}")
        
        return results
    
    def generate_change_maps(self, save_tiff: bool = True) -> Dict:
        """
        Generate comprehensive change maps including persistence and transition maps.
        
        Parameters:
        -----------
        save_tiff : bool
            Whether to save maps as GeoTIFF files
            
        Returns:
        --------
        Dict containing all generated maps
        """
        print("\\n🗺️ GENERATING CHANGE MAPS")
        print("=" * 30)
        
        results = {
            'change_maps': {},
            'persistence_maps': {},
            'cumulative_change': None,
            'first_to_last_change': None
        }
        
        # Generate consecutive change maps
        print("   🔄 Consecutive change maps")
        for i in range(len(self.years) - 1):
            year1, year2 = self.years[i], self.years[i + 1]
            
            change_map = self.change_mapping.create_change_map(year1, year2)
            results['change_maps'][f"{year1}-{year2}"] = change_map
            
            if save_tiff:
                self._save_change_map_tiff(change_map, f"change_map_{year1}_{year2}")
                
            print(f"      ✅ {year1} → {year2}")
        
        # Generate persistence maps
        print("   📍 Persistence maps")
        persistence_maps = self.persistence_analysis.generate_persistence_maps()
        results['persistence_maps'] = persistence_maps
        
        if save_tiff:
            for period, pmap in persistence_maps.items():
                self._save_map_tiff(pmap, f"persistence_map_{period}")
            
        # Cumulative change map (all years)
        print("   📈 Cumulative change map")
        cumulative_change = self.change_mapping.create_cumulative_change_map()
        results['cumulative_change'] = cumulative_change
        
        if save_tiff:
            self._save_map_tiff(cumulative_change, "cumulative_change_map")
        
        # First to last change map  
        print("   🎯 First-to-last change map")
        first_to_last = self.change_mapping.create_change_map(self.years[0], self.years[-1])
        results['first_to_last_change'] = first_to_last
        
        if save_tiff:
            self._save_change_map_tiff(first_to_last, f"change_map_{self.years[0]}_{self.years[-1]}")
        
        self.change_maps = results
        
        print(f"   💾 Maps saved to: {self.output_dir / 'maps'}")
        
        return results
    
    def _save_map_tiff(self, map_array: np.ndarray, filename: str):
        """Save a map array as GeoTIFF."""
        maps_dir = self.output_dir / "maps" 
        maps_dir.mkdir(exist_ok=True)
        
        # Get reference raster for geospatial info
        ref_processor = self.raster_stack.get_processor(self.years[0])
        
        output_path = maps_dir / f"{filename}.tiff"
        
        with rasterio.open(
            output_path,
            'w',
            driver='GTiff',
            height=map_array.shape[0],
            width=map_array.shape[1], 
            count=1,
            dtype=map_array.dtype,
            crs=ref_processor.metadata.get('crs', 'EPSG:4326'),
            transform=ref_processor.metadata.get('transform', from_origin(0, 0, 1, 1)),
            compress='lzw',
            tiled=True,
            blockxsize=256,
            blockysize=256
        ) as dst:
            dst.write(map_array, 1)
        
        print(f"      💾 Saved: {output_path}")
    
    def _save_change_map_tiff(self, change_map: np.ndarray, filename: str):
        """Save binary change map as GeoTIFF."""
        # Convert boolean to uint8 for better compatibility
        change_map_uint8 = change_map.astype(np.uint8)
        self._save_map_tiff(change_map_uint8, filename)
    
    def sankey_land(self, contingency_results: Dict = None, 
                   step_type: str = 'multi',
                   **kwargs) -> str:
        """
        Create Sankey diagrams (OpenLand-style function).
        
        This function provides OpenLand-compatible API while using the 
        optimized Sankey implementation from visualization module.
        
        Parameters:
        -----------
        contingency_results : Dict, optional
            Pre-computed contingency tables
        step_type : str
            Type of Sankey ('multi' for multistep, 'single' for onestep)
        **kwargs
            Additional arguments passed to plot_sankey
            
        Returns:
        --------
        str: Path to saved Sankey diagram
        """
        
        # Import the optimized Sankey function
        from ..visualization.plots.sankey_plots import plot_sankey
        
        print(f"\\n🌊 CREATING SANKEY DIAGRAM ({step_type.upper()})")
        print("=" * 45)
        
        # Use existing contingency tables or compute them
        if contingency_results is None:
            contingency_results = self.contingency_tables or self.contingency_table()
        
        # Set up output directory
        sankey_dir = self.output_dir / "sankey_diagrams" 
        sankey_dir.mkdir(exist_ok=True)
        
        # Convert step_type for compatibility
        plot_step_type = 'multi' if step_type == 'multistep' else 'single'
        
        # Use the optimized plot_sankey function from visualization module
        try:
            result_path = plot_sankey(
                data=contingency_results,
                step_type=plot_step_type,
                output_dir=str(sankey_dir),
                period=f"{self.years[0]}-{self.years[-1]}",
                **kwargs
            )
            
            if result_path:
                print(f"   ✅ Sankey diagram created successfully")
                print(f"   💾 Saved to: {result_path}")
                return str(result_path)
            else:
                print("   ⚠️ Using fallback Sankey implementation")
                return self._create_simple_sankey_fallback(contingency_results, sankey_dir, step_type)
            
        except Exception as e:
            print(f"   ⚠️ Optimized Sankey failed: {str(e)}")
            print("   🔄 Using fallback implementation...")
            return self._create_simple_sankey_fallback(contingency_results, sankey_dir, step_type)
    
    def _create_simple_sankey_fallback(self, contingency_results: Dict, output_dir: Path, step_type: str) -> str:
        """
        Simple fallback Sankey implementation.
        
        Used when the optimized visualization module fails.
        """
        
        import plotly.graph_objects as go
        
        try:
            # Use first table for simple fallback
            table_key = list(contingency_results.keys())[0]
            table = contingency_results[table_key]
            
            if isinstance(table, dict):
                # Convert dict to DataFrame if needed
                data = []
                for from_class, transitions in table.items():
                    if isinstance(transitions, dict):
                        for to_class, area in transitions.items():
                            if area > 0:
                                data.append({
                                    'From': from_class,
                                    'To': to_class,
                                    'Area': area
                                })
                table = pd.DataFrame(data)
            
            # Get unique classes
            all_classes = sorted(set(table['From'].unique()) | set(table['To'].unique()))
            
            # Create node labels
            node_labels = [f"Class {cls}" for cls in all_classes]
            
            # Create links
            sources, targets, values = [], [], []
            
            for _, row in table.iterrows():
                if row['Area'] > 0.1:  # Minimum threshold
                    from_idx = all_classes.index(row['From'])
                    to_idx = all_classes.index(row['To'])
                    
                    sources.append(from_idx)
                    targets.append(to_idx)
                    values.append(row['Area'])
            
            # Create Sankey diagram
            fig = go.Figure(data=[go.Sankey(
                node=dict(
                    pad=15,
                    thickness=20,
                    line=dict(color="black", width=0.5),
                    label=node_labels
                ),
                link=dict(
                    source=sources,
                    target=targets,
                    value=values
                )
            )])
            
            fig.update_layout(
                title_text=f"Land Use Transitions ({step_type})",
                font_size=10
            )
            
            # Save fallback diagram
            output_file = output_dir / f"sankey_fallback_{step_type}.html"
            fig.write_html(str(output_file))
            
            print(f"   ✅ Fallback Sankey saved: {output_file}")
            return str(output_file)
            
        except Exception as e:
            print(f"   ❌ Fallback Sankey also failed: {str(e)}")
            return ""
        """Create multi-step Sankey diagram."""
        
        # Build comprehensive node list for all years
        all_node_labels = []
        all_node_colors = []
        
        class_colors = {
            1: '#FF4444', 2: '#FFD700', 3: '#228B22', 
            4: '#4169E1', 5: '#FFA500', 6: '#9932CC'
        }
        
        # Get all unique classes
        all_classes = set()
        for table in contingency_results['lulc_Multistep'].values():
            all_classes.update(table.index)
            all_classes.update(table.columns)
        
        all_classes = sorted(list(all_classes))
        
        # Create nodes for each year-class combination
        for year in self.years:
            for cls in all_classes:
                class_name = self.class_names.get(int(cls), f'Class {cls}')
                all_node_labels.append(f"{class_name}\\n{year}")
                all_node_colors.append(class_colors.get(int(cls), '#888888'))
        
        # Build links for all transitions
        all_source_indices = []
        all_target_indices = []
        all_values = []
        all_link_colors = []
        
        nodes_per_year = len(all_classes)
        
        transitions = sorted(contingency_results['lulc_Multistep'].keys())
        for year_idx, transition in enumerate(transitions):
            table = contingency_results['lulc_Multistep'][transition]
            
            for i, source_cls in enumerate(all_classes):
                for j, target_cls in enumerate(all_classes):
                    if source_cls in table.index and target_cls in table.columns:
                        value = table.loc[source_cls, target_cls]
                        
                        if value > 50:  # Threshold for showing flows
                            source_node_idx = year_idx * nodes_per_year + i
                            target_node_idx = (year_idx + 1) * nodes_per_year + j
                            
                            all_source_indices.append(source_node_idx)
                            all_target_indices.append(target_node_idx)
                            all_values.append(value)
                            
                            # Color based on source class
                            color_hex = class_colors.get(int(source_cls), '#888888')
                            r, g, b = int(color_hex[1:3], 16), int(color_hex[3:5], 16), int(color_hex[5:7], 16)
                            all_link_colors.append(f"rgba({r},{g},{b},0.6)")
        
        # Create Sankey diagram
        fig = go.Figure(data=[go.Sankey(
            node=dict(
                pad=15,
                thickness=20, 
                line=dict(color="black", width=0.5),
                label=all_node_labels,
                color=all_node_colors,
                x=[i // nodes_per_year * 0.2 for i in range(len(all_node_labels))],
                y=[(i % nodes_per_year) * 0.15 + 0.1 for i in range(len(all_node_labels))]
            ),
            link=dict(
                source=all_source_indices,
                target=all_target_indices,
                value=all_values,
                color=all_link_colors
            )
        )])
        
        fig.update_layout(
            title_text=f"Multi-Step Land Use Transitions ({self.years[0]}-{self.years[-1]})",
            font_size=12,
            width=1400,
            height=900
        )
        
        output_file = output_dir / "sankey_multistep.html"
        fig.write_html(output_file)
        
        print(f"   ✅ Multi-step Sankey saved: {output_file}")
        return str(output_file)
    
    def bar_plot_land(self, contingency_results: Dict = None) -> str:
        """
        Create bar plots showing area evolution (OpenLand-style function).
        
        Parameters:
        -----------
        contingency_results : Dict, optional
            Results from contingency_table()
            
        Returns:
        --------
        str: Path to saved plot
        """
        if contingency_results is None:
            contingency_results = self.contingency_table()
        
        print("\\n📊 CREATING AREA EVOLUTION PLOTS")
        print("=" * 35)
        
        # Prepare data for plotting
        area_data = []
        for year in self.years:
            areas = contingency_results['totalArea'][year]
            for class_val, area_km2 in areas.items():
                area_data.append({
                    'Year': year,
                    'Class': int(class_val),
                    'Class_Name': self.class_names.get(int(class_val), f'Class_{class_val}'),
                    'Area_km2': area_km2
                })
        
        area_df = pd.DataFrame(area_data)
        
        # Create plots
        plots_dir = self.output_dir / "plots"
        plots_dir.mkdir(exist_ok=True)
        
        # 1. Line plot
        fig, ax = plt.subplots(figsize=(12, 8))
        
        for class_name in area_df['Class_Name'].unique():
            class_data = area_df[area_df['Class_Name'] == class_name]
            ax.plot(class_data['Year'], class_data['Area_km2'], 
                   marker='o', linewidth=2.5, markersize=8, label=class_name)
        
        ax.set_title('Land Use Area Evolution', fontsize=16, fontweight='bold')
        ax.set_xlabel('Year', fontsize=14)
        ax.set_ylabel('Area (km²)', fontsize=14)
        ax.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
        ax.grid(True, alpha=0.3)
        plt.tight_layout()
        
        line_plot = plots_dir / "area_evolution_line.png"
        plt.savefig(line_plot, dpi=300, bbox_inches='tight')
        plt.close()
        
        # 2. Stacked bar plot
        pivot_df = area_df.pivot(index='Year', columns='Class_Name', values='Area_km2')
        
        fig, ax = plt.subplots(figsize=(12, 8))
        pivot_df.plot(kind='bar', stacked=True, ax=ax, width=0.7)
        
        ax.set_title('Land Use Composition by Year', fontsize=16, fontweight='bold')
        ax.set_xlabel('Year', fontsize=14)
        ax.set_ylabel('Area (km²)', fontsize=14)
        ax.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
        plt.xticks(rotation=0)
        plt.tight_layout()
        
        stacked_plot = plots_dir / "area_evolution_stacked.png"
        plt.savefig(stacked_plot, dpi=300, bbox_inches='tight')
        plt.close()
        
        print(f"   ✅ Line plot saved: {line_plot}")
        print(f"   ✅ Stacked plot saved: {stacked_plot}")
        
        return str(line_plot)
    
    def run_complete_analysis(self, save_tiff: bool = True) -> Dict:
        """
        Run the complete LULC analysis workflow.
        
        This is the main function that orchestrates all analysis steps,
        similar to a complete OpenLand workflow.
        
        Parameters:
        -----------
        save_tiff : bool
            Whether to save maps as GeoTIFF files
            
        Returns:
        --------
        Dict containing all analysis results
        """
        print("🚀 RUNNING COMPLETE LULC ANALYSIS")
        print("=" * 50)
        
        results = {}
        
        # Step 1: Generate contingency tables
        print("\\n[1/6] Contingency Tables...")
        contingency_results = self.contingency_table()
        results['contingency'] = contingency_results
        
        # Step 2: Intensity analysis
        print("\\n[2/6] Intensity Analysis...")
        intensity_results = self.intensity_analysis(contingency_results)
        results['intensity'] = intensity_results
        
        # Step 3: Generate change maps
        print("\\n[3/6] Change Maps...")
        change_maps = self.generate_change_maps(save_tiff=save_tiff)
        results['maps'] = change_maps
        
        # Step 4: Create Sankey diagrams
        print("\\n[4/6] Sankey Diagrams...")
        sankey_multistep = self.sankey_land(contingency_results, 'multistep')
        sankey_onestep = self.sankey_land(contingency_results, 'onestep') 
        results['sankey'] = {
            'multistep': sankey_multistep,
            'onestep': sankey_onestep
        }
        
        # Step 5: Create area evolution plots
        print("\\n[5/6] Area Evolution Plots...")
        area_plots = self.bar_plot_land(contingency_results)
        results['plots'] = area_plots
        
        # Step 6: Generate summary report
        print("\\n[6/6] Summary Report...")
        report_path = self._generate_summary_report(results)
        results['report'] = report_path
        
        print("\\n🎉 COMPLETE ANALYSIS FINISHED!")
        print("=" * 50)
        print(f"📁 All results saved in: {self.output_dir}")
        print("\\n📋 Key outputs:")
        print(f"   📊 Contingency tables: {len(contingency_results['lulc_Multistep'])} periods")
        print(f"   🔍 Intensity analysis: 3 levels completed")
        print(f"   🗺️ Change maps: {len(change_maps['change_maps'])} maps + persistence + cumulative")
        print(f"   🌊 Sankey diagrams: Multi-step + One-step")
        print(f"   📈 Area evolution plots: Line + Stacked bar")
        print(f"   📝 Summary report: {report_path}")
        
        return results
    
    def _generate_summary_report(self, results: Dict) -> str:
        """Generate comprehensive summary report."""
        
        report_file = self.output_dir / "LULC_ANALYSIS_REPORT.md"
        
        with open(report_file, 'w', encoding='utf-8') as f:
            f.write("# 🌍 LULC Analysis Comprehensive Report\\n\\n")
            f.write(f"**Analysis Date:** {pd.Timestamp.now().strftime('%Y-%m-%d %H:%M:%S')}\\n")
            f.write(f"**Dataset:** {len(self.years)} years of LULC data ({self.years[0]}-{self.years[-1]})\\n")
            f.write(f"**Package:** landuse-intensity-analysis\\n\\n")
            
            f.write("## 📊 Dataset Overview\\n\\n")
            f.write(f"- **Years Analyzed:** {self.years}\\n")
            f.write(f"- **Land Use Classes:** {len(self.class_names)}\\n")
            f.write(f"- **Analysis Periods:** {len(self.years)-1} consecutive transitions\\n\\n")
            
            f.write("### Land Use Classes\\n\\n")
            for class_val, name in self.class_names.items():
                f.write(f"- **{class_val}:** {name}\\n")
            
            f.write("\\n## 🔍 Intensity Analysis Summary\\n\\n")
            if 'intensity' in results:
                uniform_intensity = results['intensity']['uniform_intensity']
                f.write(f"- **Uniform Annual Change Rate:** {uniform_intensity:.2f}% per year\\n")
                
                # Category level summary
                category_df = results['intensity']['category_level']
                f.write("\\n### Most Dynamic Classes\\n\\n")
                
                # Get average change rates by class
                avg_changes = category_df.groupby('class_name')['net_change_%'].mean().abs().sort_values(ascending=False)
                
                for class_name, change_rate in avg_changes.head(3).items():
                    f.write(f"- **{class_name}:** {change_rate:.2f}% net change per year\\n")
            
            f.write("\\n## 📁 Generated Files\\n\\n")
            f.write("### 📊 Data Files\\n")
            f.write("- Contingency tables for all periods\\n")
            f.write("- Intensity analysis results (3 levels)\\n")
            f.write("- Area statistics by year and class\\n\\n")
            
            f.write("### 🗺️ Maps (GeoTIFF format)\\n")
            f.write("- Change maps for consecutive periods\\n")
            f.write("- Persistence maps\\n")  
            f.write("- Cumulative change map\\n")
            f.write("- First-to-last period change map\\n\\n")
            
            f.write("### 📈 Visualizations\\n")
            f.write("- Multi-step Sankey diagram\\n")
            f.write("- One-step Sankey diagram\\n")
            f.write("- Area evolution line plots\\n")
            f.write("- Stacked area composition plots\\n\\n")
            
            f.write("---\\n\\n")
            f.write("*Generated by landuse-intensity-analysis package*\\n")
        
        print(f"   ✅ Report saved: {report_file}")
        return str(report_file)