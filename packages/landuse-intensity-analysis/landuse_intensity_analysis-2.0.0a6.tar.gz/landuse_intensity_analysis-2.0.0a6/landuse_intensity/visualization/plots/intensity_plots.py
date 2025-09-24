"""
Intensity analysis plotting functions for land use transition analysis.

This module provides functions for creating transition intensity analysis
plots based on Pontius methodology and change intensity metrics.
Updated with comprehensive Pontius-Aldwaik three-level framework.
"""

from typing import Dict, List, Optional, Union, Tuple, Any
from pathlib import Path
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import seaborn as sns
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots

from .plot_utils import (
    ensure_output_dir, save_plot_files, validate_contingency_data,
    extract_data_for_plot, create_category_labels
)

# Academic color palette for intensity analysis (colorblind-safe)
INTENSITY_COLORS = {
    'gain': '#2E8B57',          # Sea Green - gains/positive changes
    'loss': '#CD5C5C',          # Indian Red - losses/negative changes  
    'stable': '#4682B4',        # Steel Blue - stable/persistence
    'active': '#FF6347',        # Tomato - active categories (above uniform)
    'dormant': '#708090',       # Slate Gray - dormant categories (below uniform)
    'targeted': '#FF4500',      # Orange Red - targeted transitions
    'avoided': '#9370DB',       # Medium Purple - avoided transitions
    'uniform': '#000080'        # Navy Blue - uniform reference line
}


def plot_interval_analysis(intensity_results: Dict, 
                         output_dir: str = "outputs/",
                         save_png: bool = True,
                         save_html: bool = True) -> Dict[str, str]:
    """
    Create interval-level intensity analysis plots.
    
    Shows annual change size and intensity for each time interval compared 
    to uniform change rate across the entire study period.
    
    Parameters
    ----------
    intensity_results : Dict
        Results from LULCAnalysis.intensity_analysis()
    output_dir : str
        Output directory for plots
    save_png : bool
        Save PNG version
    save_html : bool
        Save interactive HTML version
        
    Returns
    -------
    Dict[str, str]
        Paths to generated plot files
    """
    
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)
    
    interval_data = intensity_results['interval_level']
    uniform_intensity = intensity_results['uniform_intensity']
    
    # Create subplot with two panels
    fig = make_subplots(
        rows=1, cols=2,
        subplot_titles=('Annual Change Size', 'Annual Change Intensity'),
        specs=[[{'secondary_y': False}, {'secondary_y': False}]]
    )
    
    # Left plot: Annual change size (% of domain)
    fig.add_trace(
        go.Bar(
            x=interval_data['transition'],
            y=interval_data['change_pixels'] / interval_data['total_pixels'] * 100,
            name='Annual Change Size',
            marker_color=INTENSITY_COLORS['stable'],
            text=[f"{val:.2f}%" for val in interval_data['change_pixels'] / interval_data['total_pixels'] * 100],
            textposition='auto'
        ),
        row=1, col=1
    )
    
    # Right plot: Annual change intensity 
    fig.add_trace(
        go.Bar(
            x=interval_data['transition'],
            y=interval_data['annual_change_%'],
            name='Annual Change Intensity',
            marker_color=[INTENSITY_COLORS['active'] if val > uniform_intensity 
                         else INTENSITY_COLORS['dormant'] 
                         for val in interval_data['annual_change_%']],
            text=[f"{val:.2f}%" for val in interval_data['annual_change_%']],
            textposition='auto'
        ),
        row=1, col=2
    )
    
    # Add uniform intensity reference line
    fig.add_hline(
        y=uniform_intensity,
        col=2,
        line_dash="dash",
        line_color=INTENSITY_COLORS['uniform'],
        annotation_text=f"Uniform Intensity ({uniform_intensity:.2f}%)"
    )
    
    # Update layout
    fig.update_layout(
        title_text="Interval-Level Intensity Analysis<br><sub>Pontius-Aldwaik Methodology</sub>",
        height=500,
        showlegend=False,
        font=dict(size=12),
        annotations=[
            dict(text="Fast intervals above uniform line", 
                 xref="paper", yref="paper", x=0.75, y=-0.1, showarrow=False),
            dict(text="Slow intervals below uniform line", 
                 xref="paper", yref="paper", x=0.75, y=-0.15, showarrow=False)
        ]
    )
    
    # Update axes
    fig.update_xaxes(title_text="Time Interval", row=1, col=1)
    fig.update_xaxes(title_text="Time Interval", row=1, col=2)
    fig.update_yaxes(title_text="Annual Change Size (% of domain)", row=1, col=1)
    fig.update_yaxes(title_text="Annual Change Intensity (%)", row=1, col=2)
    
    # Save files
    output_files = {}
    
    if save_html:
        html_path = output_path / "interval_analysis.html"
        fig.write_html(str(html_path))
        output_files['html'] = str(html_path)
        print(f"   📊 Interval analysis HTML saved: {html_path}")
    
    if save_png:
        png_path = output_path / "interval_analysis.png"
        fig.write_image(str(png_path), width=1000, height=500, scale=2)
        output_files['png'] = str(png_path)
        print(f"   📊 Interval analysis PNG saved: {png_path}")
    
    return output_files


def plot_category_analysis(intensity_results: Dict,
                         time_interval: str = None,
                         output_dir: str = "outputs/",
                         save_png: bool = True,
                         save_html: bool = True) -> Dict[str, str]:
    """
    Create category-level intensity analysis plots.
    
    Shows annual gain and loss size/intensity for each land use category
    compared to uniform change rate.
    
    Parameters
    ----------
    intensity_results : Dict
        Results from LULCAnalysis.intensity_analysis()
    time_interval : str, optional
        Specific interval to plot, if None plots all intervals
    output_dir : str
        Output directory for plots
    save_png : bool
        Save PNG version
    save_html : bool  
        Save interactive HTML version
        
    Returns
    -------
    Dict[str, str]
        Paths to generated plot files
    """
    
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)
    
    category_data = intensity_results['category_level']
    uniform_intensity = intensity_results['uniform_intensity']
    
    # Filter by time interval if specified
    if time_interval:
        category_data = category_data[category_data['transition'] == time_interval]
        title_suffix = f" - {time_interval}"
        file_suffix = f"_{time_interval.replace('-', '_')}"
    else:
        title_suffix = " - All Intervals"
        file_suffix = "_all_intervals"
    
    if category_data.empty:
        print(f"❌ No data for interval: {time_interval}")
        return {}
    
    # Get unique intervals for subplot layout
    intervals = category_data['transition'].unique()
    n_intervals = len(intervals)
    
    if n_intervals == 1:
        fig = make_subplots(
            rows=1, cols=2,
            subplot_titles=('Annual Change Size', 'Annual Change Intensity'),
            specs=[[{'secondary_y': False}, {'secondary_y': False}]]
        )
        
        interval_data = category_data[category_data['transition'] == intervals[0]]
        
        # Left plot: Annual change size (gain vs loss)
        fig.add_trace(
            go.Bar(
                x=interval_data['class_name'],
                y=-interval_data['annual_loss_%'],  # Negative for losses
                name='Annual Loss',
                marker_color=INTENSITY_COLORS['loss'],
                text=[f"{val:.1f}%" for val in interval_data['annual_loss_%']],
                textposition='auto'
            ),
            row=1, col=1
        )
        
        fig.add_trace(
            go.Bar(
                x=interval_data['class_name'],
                y=interval_data['annual_gain_%'],
                name='Annual Gain',
                marker_color=INTENSITY_COLORS['gain'],
                text=[f"{val:.1f}%" for val in interval_data['annual_gain_%']],
                textposition='auto'
            ),
            row=1, col=1
        )
        
        # Right plot: Annual change intensity (with uniform line)
        fig.add_trace(
            go.Bar(
                x=interval_data['class_name'],
                y=-interval_data['annual_loss_%'],  # Negative for losses
                name='Loss Intensity',
                marker_color=[INTENSITY_COLORS['active'] if abs(val) > uniform_intensity 
                             else INTENSITY_COLORS['dormant'] 
                             for val in interval_data['annual_loss_%']],
                text=[f"{val:.1f}%" for val in interval_data['annual_loss_%']],
                textposition='auto',
                showlegend=False
            ),
            row=1, col=2
        )
        
        fig.add_trace(
            go.Bar(
                x=interval_data['class_name'],
                y=interval_data['annual_gain_%'],
                name='Gain Intensity',
                marker_color=[INTENSITY_COLORS['active'] if val > uniform_intensity 
                             else INTENSITY_COLORS['dormant'] 
                             for val in interval_data['annual_gain_%']],
                text=[f"{val:.1f}%" for val in interval_data['annual_gain_%']],
                textposition='auto',
                showlegend=False
            ),
            row=1, col=2
        )
        
        # Add uniform intensity reference lines
        fig.add_hline(y=uniform_intensity, col=2, line_dash="dash", 
                     line_color=INTENSITY_COLORS['uniform'])
        fig.add_hline(y=-uniform_intensity, col=2, line_dash="dash", 
                     line_color=INTENSITY_COLORS['uniform'])
        
        # Update layout
        fig.update_layout(
            title_text=f"Category-Level Intensity Analysis{title_suffix}<br><sub>Active categories above uniform line</sub>",
            height=600,
            font=dict(size=10)
        )
        
        # Update axes
        fig.update_xaxes(title_text="Land Use Category", row=1, col=1)
        fig.update_xaxes(title_text="Land Use Category", row=1, col=2)
        fig.update_yaxes(title_text="Annual Change Size (%)", row=1, col=1)
        fig.update_yaxes(title_text="Annual Change Intensity (%)", row=1, col=2)
        
    else:
        # Multi-interval layout (not implemented in this version)
        print("⚠️ Multi-interval category plots not implemented yet")
        return {}
    
    # Save files
    output_files = {}
    
    if save_html:
        html_path = output_path / f"category_analysis{file_suffix}.html"
        fig.write_html(str(html_path))
        output_files['html'] = str(html_path)
        print(f"   📊 Category analysis HTML saved: {html_path}")
    
    if save_png:
        png_path = output_path / f"category_analysis{file_suffix}.png"
        fig.write_image(str(png_path), width=1200, height=600, scale=2)
        output_files['png'] = str(png_path)
        print(f"   📊 Category analysis PNG saved: {png_path}")
    
    return output_files


def plot_transition_matrix_heatmap(contingency_results: Dict,
                                 time_interval: str = None,
                                 class_names: Dict[int, str] = None,
                                 output_dir: str = "outputs/",
                                 save_png: bool = True,
                                 save_html: bool = True) -> Dict[str, str]:
    """
    Create transition matrix heatmaps showing magnitude of category-to-category transitions.
    
    Parameters
    ----------
    contingency_results : Dict
        Results from LULCAnalysis.contingency_table()
    time_interval : str, optional
        Specific interval to plot
    class_names : Dict[int, str], optional
        Class names mapping
    output_dir : str
        Output directory for plots
    save_png : bool
        Save PNG version
    save_html : bool
        Save interactive HTML version
        
    Returns
    -------
    Dict[str, str]
        Paths to generated plot files
    """
    
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)
    
    # Get appropriate contingency table
    if time_interval and time_interval in contingency_results.get('lulc_Multistep', {}):
        table = contingency_results['lulc_Multistep'][time_interval]
        title_suffix = f" - {time_interval}"
        file_suffix = f"_{time_interval.replace('-', '_')}"
    else:
        # Use one-step if available
        if 'lulc_Onestep' in contingency_results:
            table = contingency_results['lulc_Onestep']
            title_suffix = " - Overall Change"
            file_suffix = "_onestep"
        else:
            print("❌ No suitable contingency table found")
            return {}
    
    # Prepare labels
    if class_names:
        labels = [class_names.get(int(cls), f'Class {cls}') for cls in table.index]
    else:
        labels = [f'Class {cls}' for cls in table.index]
    
    # Create heatmap
    fig = go.Figure(data=go.Heatmap(
        z=table.values,
        x=labels,
        y=labels,
        colorscale='Viridis',
        colorbar=dict(title="Pixels"),
        text=table.values,
        texttemplate="%{text}",
        textfont={"size": 10},
        hoverongaps=False
    ))
    
    # Update layout
    fig.update_layout(
        title=f"Transition Matrix Heatmap{title_suffix}<br><sub>Rows: From classes, Columns: To classes</sub>",
        xaxis_title="To Class",
        yaxis_title="From Class",
        width=700,
        height=700,
        font=dict(size=12)
    )
    
    # Save files
    output_files = {}
    
    if save_html:
        html_path = output_path / f"transition_matrix_heatmap{file_suffix}.html"
        fig.write_html(str(html_path))
        output_files['html'] = str(html_path)
        print(f"   📊 Transition matrix HTML saved: {html_path}")
    
    if save_png:
        png_path = output_path / f"transition_matrix_heatmap{file_suffix}.png"
        fig.write_image(str(png_path), width=700, height=700, scale=2)
        output_files['png'] = str(png_path)
        print(f"   📊 Transition matrix PNG saved: {png_path}")
    
    return output_files


def plot_temporal_gain_loss_analysis(intensity_results: Dict,
                                    category: str = None,
                                    output_dir: str = "outputs/",
                                    save_png: bool = True,
                                    save_html: bool = True) -> Dict[str, str]:
    """
    Create temporal gain/loss analysis plots for specific category showing patterns over time.
    
    Parameters
    ----------
    intensity_results : Dict
        Results from LULCAnalysis.intensity_analysis()
    category : str, optional
        Specific category to analyze
    output_dir : str
        Output directory for plots
    save_png : bool
        Save PNG version
    save_html : bool
        Save interactive HTML version
        
    Returns
    -------
    Dict[str, str]
        Paths to generated plot files
    """
    
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)
    
    category_data = intensity_results['category_level']
    uniform_intensity = intensity_results['uniform_intensity']
    
    # Filter by category if specified
    if category:
        category_data = category_data[category_data['class_name'] == category]
        title_suffix = f" - {category}"
        file_suffix = f"_{category.replace(' ', '_').lower()}"
    else:
        title_suffix = " - All Categories"
        file_suffix = "_all_categories"
    
    if category_data.empty:
        print(f"❌ No data for category: {category}")
        return {}
    
    # Create temporal plot
    fig = go.Figure()
    
    # Add gain line
    fig.add_trace(go.Scatter(
        x=category_data['transition'],
        y=category_data['annual_gain_%'],
        mode='lines+markers',
        name='Annual Gain',
        line=dict(color=INTENSITY_COLORS['gain'], width=3),
        marker=dict(size=8)
    ))
    
    # Add loss line (as positive values for visibility)
    fig.add_trace(go.Scatter(
        x=category_data['transition'],
        y=category_data['annual_loss_%'],
        mode='lines+markers', 
        name='Annual Loss',
        line=dict(color=INTENSITY_COLORS['loss'], width=3),
        marker=dict(size=8)
    ))
    
    # Add net change line
    fig.add_trace(go.Scatter(
        x=category_data['transition'],
        y=category_data['net_change_%'],
        mode='lines+markers',
        name='Net Change',
        line=dict(color=INTENSITY_COLORS['stable'], width=2, dash='dash'),
        marker=dict(size=6)
    ))
    
    # Add uniform intensity reference line
    fig.add_hline(
        y=uniform_intensity,
        line_dash="dash",
        line_color=INTENSITY_COLORS['uniform'],
        annotation_text=f"Uniform Intensity ({uniform_intensity:.2f}%)"
    )
    
    # Update layout
    fig.update_layout(
        title=f"Temporal Gain/Loss Analysis{title_suffix}<br><sub>Temporal patterns of land use change</sub>",
        xaxis_title="Time Interval",
        yaxis_title="Annual Change Intensity (%)",
        height=500,
        font=dict(size=12),
        hovermode='x unified'
    )
    
    # Save files  
    output_files = {}
    
    if save_html:
        html_path = output_path / f"temporal_gain_loss_analysis{file_suffix}.html"
        fig.write_html(str(html_path))
        output_files['html'] = str(html_path)
        print(f"   📊 Temporal Gain/Loss analysis HTML saved: {html_path}")
    
    if save_png:
        png_path = output_path / f"temporal_gain_loss_analysis{file_suffix}.png"
        fig.write_image(str(png_path), width=1000, height=500, scale=2)
        output_files['png'] = str(png_path)
        print(f"   📊 Temporal Gain/Loss analysis PNG saved: {png_path}")
    
    return output_files


def create_intensity_summary_report(intensity_results: Dict,
                                  contingency_results: Dict = None,
                                  output_dir: str = "outputs/") -> str:
    """
    Create comprehensive intensity analysis summary report with all plots.
    
    Parameters
    ----------
    intensity_results : Dict
        Results from LULCAnalysis.intensity_analysis()
    contingency_results : Dict, optional
        Results from LULCAnalysis.contingency_table()
    output_dir : str
        Output directory for report
        
    Returns
    -------
    str
        Path to generated summary report
    """
    
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)
    
    print("📊 Generating comprehensive intensity analysis plots...")
    
    # Generate all plots
    plot_files = {}
    
    # Interval analysis
    plot_files['interval'] = plot_interval_analysis(
        intensity_results, output_dir, save_png=True, save_html=False
    )
    
    # Category analysis for each interval
    intervals = intensity_results['interval_level']['transition'].unique()
    for interval in intervals:
        plot_files[f'category_{interval}'] = plot_category_analysis(
            intensity_results, interval, output_dir, save_png=True, save_html=False
        )
    
    # Transition matrix heatmaps
    if contingency_results:
        for interval in intervals:
            plot_files[f'heatmap_{interval}'] = plot_transition_matrix_heatmap(
                contingency_results, interval, None, output_dir, save_png=True, save_html=False
            )
    
    # Create summary report
    summary_path = output_path / "intensity_analysis_summary.md"
    
    with open(summary_path, 'w', encoding='utf-8') as f:
        f.write("# Intensity Analysis Summary Report\n\n")
        f.write("## Pontius-Aldwaik Three-Level Framework\n\n")
        
        # Level 1 summary
        f.write("### Level 1: Interval Analysis\n\n")
        uniform = intensity_results['uniform_intensity']
        f.write(f"**Uniform Intensity**: {uniform:.3f}% per year\n\n")
        
        interval_data = intensity_results['interval_level']
        f.write("| Interval | Annual Change (%) | Classification |\n")
        f.write("|----------|-------------------|----------------|\n")
        
        for _, row in interval_data.iterrows():
            classification = "Fast" if row['annual_change_%'] > uniform else "Slow"
            f.write(f"| {row['transition']} | {row['annual_change_%']:.3f} | {classification} |\n")
        
        # Level 2 summary
        f.write("\n### Level 2: Category Analysis\n\n")
        category_data = intensity_results['category_level']
        
        f.write("| Category | Interval | Gain (%) | Loss (%) | Net Change (%) | Status |\n")
        f.write("|----------|----------|----------|----------|----------------|--------|\n")
        
        for _, row in category_data.iterrows():
            gain_status = "Active" if row['annual_gain_%'] > uniform else "Dormant"
            loss_status = "Active" if row['annual_loss_%'] > uniform else "Dormant"
            status = f"G:{gain_status}, L:{loss_status}"
            
            f.write(f"| {row['class_name']} | {row['transition']} | ")
            f.write(f"{row['annual_gain_%']:.3f} | {row['annual_loss_%']:.3f} | ")
            f.write(f"{row['net_change_%']:.3f} | {status} |\n")
        
        f.write("\n### Generated Visualizations\n\n")
        for plot_type, files in plot_files.items():
            if files and 'png' in files:
                f.write(f"- **{plot_type.replace('_', ' ').title()}**: `{files['png']}`\n")
        
        f.write("\n---\n")
        f.write("*Report generated by landuse-intensity-analysis package*\n")
    
    print(f"   📋 Intensity analysis summary saved: {summary_path}")
    return str(summary_path)
