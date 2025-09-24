"""
Sankey diagram plotting functions for land use transition analysis.

This module provides unified Sankey plotting functionality supporting both
legacy dict format and modern ContingencyTable objects with step_type parameter.

Unified API:
- plot_sankey(): Main function with step_type parameter ('single', 'multi', 'complete')
"""

from typing import Dict, List, Optional, Union, Any, Tuple
from pathlib import Path
import pandas as pd
import numpy as np
import warnings

from .plot_utils import (
    HAS_PLOTLY, ensure_output_dir, create_category_labels,
    save_plot_files, validate_contingency_data, extract_data_for_plot,
    CATEGORY_COLORS, TRANSITION_COLORS
)

def _get_academic_colors():
    """
    Generate colorblind-safe colors following remote sensing publication standards.

    Returns standardized colors that are intuitive for land use categories
    and accessible for colorblind readers, as required by academic journals.
    Following WCAG 2.2 AA standards for high contrast and accessibility.
    """
    # Academic color palette for land use - intuitive and colorblind-safe
    # Following remote sensing visualization best practices and WCAG 2.2 AA
    # Using RGB format for Plotly compatibility and opacity control
    academic_palette = [
        'rgb(34, 139, 34)',    # Forest Green - vegetation/forest (high contrast)
        'rgb(30, 144, 255)',   # Dodger Blue - water bodies (accessible)
        'rgb(255, 215, 0)',    # Gold - agriculture/cropland (distinct)
        'rgb(139, 69, 19)',    # Saddle Brown - bare soil/urban (natural)
        'rgb(255, 20, 147)',   # Deep Pink - developed areas (warning)
        'rgb(255, 140, 0)',    # Dark Orange - grassland/pasture (distinct)
        'rgb(75, 0, 130)',     # Indigo - wetlands (unique)
        'rgb(220, 20, 60)',    # Crimson - alternative class (high contrast)
        'rgb(0, 128, 128)',    # Teal - water/aquaculture (accessible)
        'rgb(128, 0, 128)',    # Purple - mixed use (distinct)
        'rgb(255, 69, 0)',     # Red Orange - disturbed areas (warning)
        'rgb(46, 139, 87)',    # Sea Green - secondary vegetation (natural)
        'rgb(218, 165, 32)',   # Goldenrod - arid areas (distinct)
        'rgb(70, 130, 180)',   # Steel Blue - permanent water (accessible)
        'rgb(154, 205, 50)'    # Yellow Green - restored areas (positive)
    ]

    return academic_palette


if HAS_PLOTLY:
    import plotly.graph_objects as go
    from plotly.subplots import make_subplots


def _calculate_border_to_center_positions(node_values_by_column):
    """
    Calculate border-to-center node positioning for Sankey diagrams.
    Larger/more important nodes are positioned towards edges, smaller ones in center.
    
    Parameters
    ----------
    node_values_by_column : dict
        Dictionary with column index as key and list of (node_index, value) tuples
        
    Returns
    -------
    tuple
        (node_x, node_y) lists for manual node positioning
    """
    node_x = []
    node_y = []
    
    for col_idx, nodes_and_values in node_values_by_column.items():
        # Sort nodes by value (descending - largest first)
        sorted_nodes = sorted(nodes_and_values, key=lambda x: x[1], reverse=True)
        num_nodes = len(sorted_nodes)
        
        if num_nodes == 1:
            # Single node goes in center
            positions = [0.5]
        elif num_nodes == 2:
            # Two nodes: edges
            positions = [0.1, 0.9]
        else:
            # Multiple nodes: border-to-center arrangement
            positions = []
            for i in range(num_nodes):
                if i == 0:
                    # Largest to top edge
                    pos = 0.05
                elif i == 1 and num_nodes > 2:
                    # Second largest to bottom edge
                    pos = 0.95
                else:
                    # Remaining nodes distributed in center
                    center_nodes = num_nodes - 2
                    center_idx = i - 2
                    if center_nodes == 1:
                        pos = 0.5
                    else:
                        # Distribute in middle space (0.2 to 0.8)
                        pos = 0.25 + (center_idx * 0.5 / (center_nodes - 1))
                positions.append(pos)
        
        # Calculate x position for this column
        x_pos = col_idx / max(1, len(node_values_by_column) - 1) if len(node_values_by_column) > 1 else 0.5
        
        # Assign positions to nodes
        for (node_idx, _), y_pos in zip(sorted_nodes, positions):
            node_x.append(x_pos)
            node_y.append(y_pos)
    
    return node_x, node_y


def _convert_contingency_table_to_legacy_format(contingency_table) -> Dict[str, pd.DataFrame]:
    """
    Convert modern ContingencyTable object to legacy dict format.
    
    Parameters
    ----------
    contingency_table : ContingencyTable
        Modern ContingencyTable object
        
    Returns
    -------
    Dict[str, pd.DataFrame]
        Legacy format dict with 'lulc_SingleStep', 'lulc_MultiStep', 'tb_legend'
    """
    try:
        # Access the results from the ContingencyTable
        results = contingency_table.results
        contingency_df = results.contingency_table
        
        # Create legend from unique classes in the data
        unique_classes_from = contingency_df['class_from'].unique()
        unique_classes_to = contingency_df['class_to'].unique()
        all_classes = list(set(list(unique_classes_from) + list(unique_classes_to)))
        
        tb_legend = pd.DataFrame({
            'Class': all_classes,
            'ClassName': [f'Class {c}' for c in all_classes]
        })
        
        # Process contingency table to extract transitions
        legacy_format = {
            'tb_legend': tb_legend
        }
        
        if contingency_df is not None and not contingency_df.empty:
            # For single-step: get transitions between first two time periods
            unique_times = sorted(contingency_df['time_from'].unique())
            if len(unique_times) >= 2:
                first_period = contingency_df[
                    (contingency_df['time_from'] == unique_times[0]) & 
                    (contingency_df['time_to'] == unique_times[1])
                ].copy()
                
                if not first_period.empty:
                    # Convert to legacy format: From, To, km2
                    single_step_data = pd.DataFrame({
                        'From': first_period['class_from'],
                        'To': first_period['class_to'],
                        'km2': first_period['count'] * 0.01  # Convert pixel count to km2 (assuming 100m pixels)
                    })
                    legacy_format['lulc_SingleStep'] = single_step_data
                else:
                    legacy_format['lulc_SingleStep'] = pd.DataFrame(columns=['From', 'To', 'km2'])
            else:
                legacy_format['lulc_SingleStep'] = pd.DataFrame(columns=['From', 'To', 'km2'])
            
            # For multi-step: aggregate ALL transitions by class (ignore time)
            # This creates a simple two-column Sankey: Origin → Destination
            multi_step_data = contingency_df.groupby(['class_from', 'class_to'])['count'].sum().reset_index()
            multi_step_data['km2'] = multi_step_data['count'] * 0.01  # Convert pixel count to km2
            
            # Rename columns to match legacy format
            multi_step_data = multi_step_data.rename(columns={'class_from': 'From', 'class_to': 'To'})
            multi_step_data = multi_step_data[['From', 'To', 'km2']]  # Reorder columns
            
            legacy_format['lulc_MultiStep'] = multi_step_data
        
        return legacy_format
        
    except Exception as e:
        warnings.warn(f"Failed to convert ContingencyTable to legacy format: {e}")
        return {
            'lulc_SingleStep': pd.DataFrame(columns=['From', 'To', 'km2']),
            'lulc_MultiStep': pd.DataFrame(columns=['From', 'To', 'km2']),
            'tb_legend': pd.DataFrame(columns=['Class', 'ClassName'])
        }


def plot_sankey(
    data: Union[Dict, Any],
    step_type: str = 'single',
    output_dir: str = "outputs/",
    period: str = "",
    title: Optional[str] = None,
    custom_labels: Optional[Dict[Union[int, str], str]] = None,
    min_area_km2: float = 0.1,
    save_png: bool = True,
    save_html: bool = True,
    show_plot: bool = False,
    time_from: Optional[Union[str, int]] = None,
    time_to: Optional[Union[str, int]] = None,
    **kwargs
) -> Optional[Union[str, go.Figure]]:
    """
    Create Sankey diagrams with unified interface.
    
    This is the main function for creating all types of Sankey diagrams.
    It supports both legacy dict format and modern ContingencyTable objects.
    
    Parameters
    ----------
    data : dict or ContingencyTable
        Data for creating the Sankey diagram. Can be:
        - Dict with 'lulc_SingleStep'/'lulc_MultiStep' and 'tb_legend' keys (legacy format)
        - ContingencyTable object (modern format)
    step_type : str, default 'single'
        Type of Sankey diagram to create:
        - 'single': Single-step transitions (primeiro → último ano, ex: 2000 → 2004)
        - 'multi': Multi-step temporal transitions (ano a ano: 2000→2001→2002→2003→2004)
    output_dir : str, default "outputs/"
        Directory to save output files
    period : str, default ""
        Period description for the plot title
    title : str, optional
        Custom title for the plot. If None, auto-generated
    custom_labels : dict, optional
        Custom labels for land use categories {class_id: label}
    min_area_km2 : float, default 0.1
        Minimum area threshold to include transitions (km²)
    save_png : bool, default True
        Whether to save PNG version
    save_html : bool, default True
        Whether to save HTML version
    show_plot : bool, default False
        Whether to display the plot
    time_from : str or int, optional
        Starting year for transition (for single-step)
    time_to : str or int, optional
        Ending year for transition (for single-step)
    **kwargs
        Additional arguments passed to plotting functions
        
    Returns
    -------
    str or None
        Path to saved HTML file if successful, None if creation failed
        
    Examples
    --------
    >>> # Single-step Sankey (primeiro → último ano)
    >>> plot_sankey(contingency_table, step_type='single')
    
    >>> # Multi-step Sankey temporal (ano a ano)
    >>> plot_sankey(contingency_table, step_type='multi')
    """
    
    if not HAS_PLOTLY:
        print("⚠️ Plotly not available. Sankey diagrams require plotly.")
        return None
    
    # Handle different input types
    if hasattr(data, 'results') and hasattr(data.results, 'contingency_table'):
        # Modern ContingencyTable object
        contingency_df = data.results.contingency_table
    elif isinstance(data, dict):
        # Legacy dict format - extract data
        if step_type == 'single':
            legacy_data = data.get('lulc_SingleStep')
        else:
            legacy_data = data.get('lulc_MultiStep')
        
        if legacy_data is None or legacy_data.empty:
            print(f"❌ No data available for {step_type}-step Sankey")
            return None
            
        # Convert legacy to modern format for processing
        contingency_df = pd.DataFrame({
            'class_from': legacy_data['From'],
            'class_to': legacy_data['To'],
            'count': legacy_data['km2'] * 100,  # Convert back to pixel count
            'time_from': 2000,  # Default values
            'time_to': 2005
        })
    elif isinstance(data, pd.DataFrame):
        # Direct DataFrame input (common for tests and direct API usage)
        required_columns = ['class_from', 'class_to', 'km2', 'time_from', 'time_to']
        if all(col in data.columns for col in required_columns):
            contingency_df = data.copy()
            contingency_df['count'] = contingency_df['km2'] * 100  # Convert km2 to pixel count
            print(f"✅ DataFrame input accepted with {len(contingency_df)} transitions")
        else:
            print(f"❌ DataFrame missing required columns: {required_columns}")
            print(f"   Available columns: {list(data.columns)}")
            return None
    else:
        print("❌ Invalid contingency data format")
        print(f"   Expected: ContingencyTable object, dict with legacy format, or pandas DataFrame")
        print(f"   Received: {type(data)}")
        return None
    
    if contingency_df is None or contingency_df.empty:
        print("❌ No data available for Sankey")
        return None
    
    # Create labels
    if custom_labels:
        label_map = custom_labels
    else:
        # Create simple labels
        unique_classes = list(set(contingency_df['class_from'].tolist() + contingency_df['class_to'].tolist()))
        label_map = {cls: f"Class {cls}" for cls in unique_classes}
    
    # Filter data by minimum area threshold
    contingency_df = contingency_df.copy()
    contingency_df['km2'] = contingency_df['count'] * 0.01
    filtered_data = contingency_df[contingency_df['km2'] >= min_area_km2].copy()
    
    if filtered_data.empty:
        print("❌ No significant transitions found")
        return None
    
    print(f"📊 Filtered data: {len(filtered_data)} transitions")
    print(filtered_data[['class_from', 'class_to', 'km2', 'time_from', 'time_to']].head())
    
    if step_type == 'single':
        return _create_single_step_sankey(filtered_data, label_map, output_dir, title, save_png, save_html, show_plot)
    elif step_type == 'multi':
        return _create_multi_step_sankey(filtered_data, label_map, output_dir, title, save_png, save_html, show_plot)
    else:
        raise ValueError(f"Invalid step_type: {step_type}. Must be 'single' or 'multi'")


def _create_single_step_sankey(filtered_data, label_map, output_dir, title, save_png, save_html, show_plot):
    """Create simple single-step Sankey: category → category with professional styling and clear two-column layout
    
    Para single-step, mostra apenas primeiro e último ano (ex: 2000 → 2004)
    """
    
    # Para single-step, pegar apenas primeiro e último ano
    unique_years = sorted(filtered_data['time_from'].unique())
    if len(unique_years) > 1:
        first_year = min(unique_years)
        last_year = max(unique_years)
        
        # Filtrar para mostrar apenas primeiro → último ano
        first_to_last = filtered_data[
            (filtered_data['time_from'] == first_year) & 
            (filtered_data['time_to'] == last_year)
        ].copy()
        
        if first_to_last.empty:
            print(f"⚠️ Nenhuma transição direta encontrada entre {first_year} → {last_year}")
            # Se não há transição direta, agregar tudo
            aggregated = filtered_data.groupby(['class_from', 'class_to'])['km2'].sum().reset_index()
        else:
            aggregated = first_to_last.groupby(['class_from', 'class_to'])['km2'].sum().reset_index()
            print(f"📈 Single-step: {first_year} → {last_year} ({len(aggregated)} transições)")
    else:
        # Fallback: agregar por classe apenas
        aggregated = filtered_data.groupby(['class_from', 'class_to'])['km2'].sum().reset_index()
        print(f"📈 Single-step agregado: {len(aggregated)} transições únicas")
    
    # Create separate source and target nodes for clear two-column layout
    # This prevents confusion when same category appears as both source and target
    unique_sources = sorted(aggregated['class_from'].unique())
    unique_targets = sorted(aggregated['class_to'].unique())
    
    # Create node labels with clear source/target distinction (clean names without years)
    source_labels = [f"{label_map.get(cls, f'Class {cls}')}" for cls in unique_sources]
    target_labels = [f"{label_map.get(cls, f'Class {cls}')}" for cls in unique_targets]
    
    # Combine all labels (sources first, then targets)
    all_labels = source_labels + target_labels
    
    # Create mapping for indices
    source_to_index = {cls: i for i, cls in enumerate(unique_sources)}
    target_to_index = {cls: i + len(unique_sources) for i, cls in enumerate(unique_targets)}
    
    # Prepare data for Sankey with clear source→target mapping
    sources = [source_to_index[row['class_from']] for _, row in aggregated.iterrows()]
    targets = [target_to_index[row['class_to']] for _, row in aggregated.iterrows()]
    values = aggregated['km2'].tolist()
    
    print(f"📊 Two-column layout: {len(source_labels)} sources → {len(target_labels)} targets")
    print(f"   Source nodes: {source_labels[:3]}...")
    print(f"   Target nodes: {target_labels[:3]}...")
    
    # Professional color scheme with transparency
    # Create colors for all unique categories (not nodes)
    all_unique_classes = sorted(set(unique_sources + unique_targets))
    base_colors = _get_academic_colors()
    class_color_map = {cls: color for cls, color in zip(all_unique_classes, base_colors)}
    
    opacity = 0.8
    
    # Convert base colors to rgba format for nodes
    node_colors = []
    
    # Colors for source nodes
    for cls in unique_sources:
        color = class_color_map[cls]
        if color.startswith('#'):
            hex_color = color.lstrip('#')
            rgb = tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
            rgba_color = f'rgba({rgb[0]},{rgb[1]},{rgb[2]},{opacity})'
        else:
            rgba_color = color.replace('rgb(', 'rgba(').replace(')', f',{opacity})')
        node_colors.append(rgba_color)
    
    # Colors for target nodes (same logic)
    for cls in unique_targets:
        color = class_color_map[cls]
        if color.startswith('#'):
            hex_color = color.lstrip('#')
            rgb = tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
            rgba_color = f'rgba({rgb[0]},{rgb[1]},{rgb[2]},{opacity})'
        else:
            rgba_color = color.replace('rgb(', 'rgba(').replace(')', f',{opacity})')
        node_colors.append(rgba_color)
    
    # Create link colors based on source node colors with transparency
    link_opacity = 0.4
    link_colors = []
    for source_idx in sources:
        source_color = node_colors[source_idx]
        # Extract RGB from RGBA and create new RGBA with link opacity
        if source_color.startswith('rgba('):
            # Extract RGB values from rgba(R,G,B,A) format
            rgb_part = source_color.replace('rgba(', '').replace(')', '').split(',')
            r, g, b = rgb_part[0], rgb_part[1], rgb_part[2]
            link_color = f'rgba({r},{g},{b},{link_opacity})'
        else:
            # Fallback for other formats
            link_color = source_color.replace('rgb(', 'rgba(').replace(')', f',{link_opacity})')
        link_colors.append(link_color)
    
    # Create standard Sankey diagram (simplified like example)
    fig = go.Figure(data=[go.Sankey(
        valueformat=".0f",
        valuesuffix=" km²",
        # Academic node styling
        node=dict(
            pad=15,  # Standard padding
            thickness=15,  # Standard thickness
            line=dict(color="black", width=0.5),  # Standard borders
            label=all_labels,  # Use clean labels
            color=node_colors
        ),
        # Academic link styling
        link=dict(
            source=sources,
            target=targets,
            value=values,
            color=link_colors
        )
    )])
    
    # Extract year range for title
    years = sorted(set(filtered_data['time_from'].tolist() + filtered_data['time_to'].tolist()))
    year_range = f"{min(years)} → {max(years)}" if len(years) > 1 else str(years[0])
    
    # Academic publication layout styling (simplified)
    fig_title = title or f"Single-step Land Use Transitions ({year_range})"
    fig.update_layout(
        title=dict(
            text=fig_title,
            x=0.5,
            xanchor='center',
            font=dict(
                family="Times New Roman, serif",
                size=14,
                color="black"
            )
        ),
        # Academic font styling
        font=dict(
            family="Times New Roman, serif",
            size=10,
            color="black"
        ),
        # Standard dimensions
        height=600,
        width=800,
        # Standard margins
        margin=dict(l=80, r=80, t=100, b=80),
        # Clean academic background
        paper_bgcolor='white',
        plot_bgcolor='white',
        # Remove default plotly branding
        showlegend=False
    )
    
    # Save files
    output_path = ensure_output_dir(output_dir)
    filename = "sankey_single_step"
    saved_path = save_plot_files(fig, output_path, filename, save_png, save_html, is_plotly=True)
    
    # Show plot if requested
    if show_plot and HAS_PLOTLY:
        fig.show()
    
    return saved_path


def _create_multi_step_sankey(filtered_data, label_map, output_dir, title, save_png, save_html, show_plot):
    """Create temporal multi-step Sankey: year-to-year flow diagram
    
    Para multi-step, cria um fluxo temporal onde cada ano é uma coluna
    e as categorias fluem entre anos (como o exemplo de energia do Plotly)
    """
    
    # Verificar se há dados temporais válidos
    unique_times_from = sorted(filtered_data['time_from'].unique())
    unique_times_to = sorted(filtered_data['time_to'].unique())
    all_years = sorted(set(unique_times_from + unique_times_to))
    
    print(f"📅 Anos encontrados: {all_years}")
    print(f"📈 Multi-step temporal: fluxo ano a ano (como diagrama de energia)")
    
    # Criar nós temporais organizados por ano e categoria
    # Formato: cada ano terá suas categorias como nós separados
    node_labels = []
    node_colors = []
    node_x = []  # Posição temporal (ano)
    node_y = []  # Posição vertical (categoria)
    
    # Mapear nós para índices
    node_to_index = {}
    node_index = 0
    
    # Obter todas as categorias únicas
    all_categories = sorted(set(filtered_data['class_from'].tolist() + filtered_data['class_to'].tolist()))
    
    # Configurar cores por categoria
    base_colors = _get_academic_colors()
    category_color_map = {}
    for i, cat in enumerate(all_categories):
        color = base_colors[i % len(base_colors)]
        category_color_map[cat] = color
    
    # Criar nós para cada ano e categoria
    for year_idx, year in enumerate(all_years):
        # Calcular posição X temporal
        if len(all_years) > 1:
            x_pos = year_idx / (len(all_years) - 1)
        else:
            x_pos = 0.5
        
        # Criar nós para categorias presentes neste ano
        categories_in_year = set()
        
        # Categorias que aparecem como source neste ano
        if year in unique_times_from:
            year_sources = filtered_data[filtered_data['time_from'] == year]['class_from'].unique()
            categories_in_year.update(year_sources)
        
        # Categorias que aparecem como target neste ano  
        if year in unique_times_to:
            year_targets = filtered_data[filtered_data['time_to'] == year]['class_to'].unique()
            categories_in_year.update(year_targets)
        
        categories_in_year = sorted(list(categories_in_year))
        
        # Posicionar categorias verticalmente
        for cat_idx, category in enumerate(categories_in_year):
            # Criar nome do nó
            node_name = f"{label_map.get(category, f'Class {category}')}_{year}"
            
            # Adicionar ao mapeamento
            node_to_index[node_name] = node_index
            node_index += 1
            
            # Label sem ano (mais limpo)
            node_labels.append(label_map.get(category, f'Class {category}'))
            
            # Posição
            node_x.append(x_pos)
            if len(categories_in_year) > 1:
                y_pos = cat_idx / (len(categories_in_year) - 1)
            else:
                y_pos = 0.5
            node_y.append(y_pos)
            
            # Cor baseada na categoria
            color = category_color_map[category]
            opacity = 0.8
            if color.startswith('#'):
                hex_color = color.lstrip('#')
                rgb = tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
                rgba_color = f'rgba({rgb[0]},{rgb[1]},{rgb[2]},{opacity})'
            else:
                rgba_color = color.replace('rgb(', 'rgba(').replace(')', f',{opacity})')
            node_colors.append(rgba_color)
    
    print(f"📍 Nós criados: {len(node_labels)} nós em {len(all_years)} anos")
    print(f"   Exemplo de nós: {list(node_to_index.keys())[:5]}...")
    
    # Preparar dados para links (transições)
    sources = []
    targets = []
    values = []
    
    for _, row in filtered_data.iterrows():
        # Criar nomes dos nós source e target
        source_name = f"{label_map.get(row['class_from'], f'Class {row['class_from']}')}_{row['time_from']}"
        target_name = f"{label_map.get(row['class_to'], f'Class {row['class_to']}')}_{row['time_to']}"
        
        # Verificar se os nós existem
        if source_name in node_to_index and target_name in node_to_index:
            sources.append(node_to_index[source_name])
            targets.append(node_to_index[target_name])
            values.append(row['km2'])
    
    print(f"🔗 Links criados: {len(sources)} transições")
    
    # Cores dos links baseadas no nó fonte
    link_opacity = 0.4
    link_colors = []
    for source_idx in sources:
        source_color = node_colors[source_idx]
        if source_color.startswith('rgba('):
            rgb_part = source_color.replace('rgba(', '').replace(')', '').split(',')
            r, g, b = rgb_part[0], rgb_part[1], rgb_part[2]
            link_color = f'rgba({r},{g},{b},{link_opacity})'
        else:
            link_color = source_color.replace('rgb(', 'rgba(').replace(')', f',{link_opacity})')
        link_colors.append(link_color)
    
    # Criar diagrama Sankey temporal (como exemplo do Plotly)
    fig = go.Figure(data=[go.Sankey(
        arrangement="snap",  # Permitir posicionamento manual
        valueformat=".0f",
        valuesuffix=" km²",
        # Configuração dos nós com posicionamento temporal
        node=dict(
            pad=10,
            thickness=15,
            line=dict(color="black", width=0.5),
            label=node_labels,
            color=node_colors,
            x=node_x,  # Posicionamento temporal (ano)
            y=node_y   # Posicionamento vertical (categoria)
        ),
        # Configuração dos links
        link=dict(
            source=sources,
            target=targets,
            value=values,
            color=link_colors
        )
    )])
    
    # Aplicar formato temporal aos dados (criar nós temporais: "Class_Year")
    filtered_data['source_node'] = filtered_data.apply(
        lambda row: f"{label_map[row['class_from']]}_{row['time_from']}", axis=1
    )
    filtered_data['target_node'] = filtered_data.apply(
        lambda row: f"{label_map[row['class_to']]}_{row['time_to']}", axis=1
    )
    
    print(f"� Nós temporais criados:")
    print(f"   Sources: {filtered_data['source_node'].nunique()} únicos")
    print(f"   Targets: {filtered_data['target_node'].nunique()} únicos")
    
    # Criar lista única de todos os nós
    all_temporal_nodes = list(set(filtered_data['source_node'].tolist() + filtered_data['target_node'].tolist()))
    all_temporal_nodes.sort()  # Ordenar para consistência
    
    # Criar mapeamento de nó para índice
    node_to_index = {node: i for i, node in enumerate(all_temporal_nodes)}
    
    # Extrair categoria base para cores (remove o sufixo _YEAR)
    def extract_base_category(temporal_node):
        return temporal_node.rsplit('_', 1)[0]  # Remove último _YEAR
    
    # Extrair ano do nó temporal
    def extract_year(temporal_node):
        try:
            return int(temporal_node.split('_')[-1])
        except:
            return 2000  # fallback
    
    # Criar esquema de cores por categoria base
    base_categories = list(set([extract_base_category(node) for node in all_temporal_nodes]))
    base_colors = _get_academic_colors()
    
    category_color_map = {}
    for i, cat in enumerate(base_categories):
        color = base_colors[i % len(base_colors)]
        category_color_map[cat] = color
    
    # Criar posicionamento temporal manual dos nós
    years_in_data = list(set([extract_year(node) for node in all_temporal_nodes]))
    years_in_data.sort()
    
    node_x = []  # Posição X (temporal)
    node_y = []  # Posição Y (categoria)
    node_colors = []
    
    # Criar labels limpos (sem ano para display)
    clean_labels = []
    
    # Organizar nós por ano e categoria
    nodes_by_year = {}
    for node in all_temporal_nodes:
        year = extract_year(node)
        if year not in nodes_by_year:
            nodes_by_year[year] = []
        nodes_by_year[year].append(node)
    
    # Posicionar nós
    for node in all_temporal_nodes:
        year = extract_year(node)
        base_cat = extract_base_category(node)
        
        # Posição X baseada no ano (temporal) - com melhor espaçamento
        if len(years_in_data) > 1:
            # Adicionar margem nas bordas e espaçamento uniforme
            margin = 0.1
            available_width = 1.0 - 2 * margin
            x_pos = margin + ((year - min(years_in_data)) / (max(years_in_data) - min(years_in_data))) * available_width
        else:
            x_pos = 0.5
        
        # Posição Y baseada na categoria (distribuir categorias verticalmente)
        nodes_in_year = sorted(nodes_by_year[year])
        node_index_in_year = nodes_in_year.index(node)
        y_pos = (node_index_in_year + 1) / (len(nodes_in_year) + 1)
        
        node_x.append(x_pos)
        node_y.append(y_pos)
        
        # Cor baseada na categoria
        color = category_color_map[base_cat]
        opacity = 0.8
        if color.startswith('#'):
            hex_color = color.lstrip('#')
            rgb = tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
            rgba_color = f'rgba({rgb[0]},{rgb[1]},{rgb[2]},{opacity})'
        else:
            rgba_color = color.replace('rgb(', 'rgba(').replace(')', f',{opacity})')
        node_colors.append(rgba_color)
        
        # Label limpo (sem ano)
        clean_labels.append(base_cat)
    
    print(f"📍 Posicionamento temporal: {len(years_in_data)} anos, {len(base_categories)} categorias")
    
    # Preparar dados para Sankey
    sources = [node_to_index[row['source_node']] for _, row in filtered_data.iterrows()]
    targets = [node_to_index[row['target_node']] for _, row in filtered_data.iterrows()]
    values = filtered_data['km2'].tolist()
    
    # Cores dos links baseadas no nó fonte
    link_opacity = 0.4
    link_colors = []
    for source_idx in sources:
        source_color = node_colors[source_idx]
        if source_color.startswith('rgba('):
            rgb_part = source_color.replace('rgba(', '').replace(')', '').split(',')
            r, g, b = rgb_part[0], rgb_part[1], rgb_part[2]
            link_color = f'rgba({r},{g},{b},{link_opacity})'
        else:
            link_color = source_color.replace('rgb(', 'rgba(').replace(')', f',{link_opacity})')
        link_colors.append(link_color)
    
    # Criar diagrama Sankey com posicionamento temporal
    fig = go.Figure(data=[go.Sankey(
        valueformat=".0f",
        valuesuffix=" km²",
        # Configuração dos nós com posicionamento temporal
        node=dict(
            pad=15,
            thickness=15,
            line=dict(color="black", width=0.5),
            label=clean_labels,
            color=node_colors,
            x=node_x,  # Posicionamento temporal
            y=node_y   # Posicionamento por categoria
        ),
        # Configuração dos links
        link=dict(
            source=sources,
            target=targets,
            value=values,
            color=link_colors
        )
    )])
    
    # Extract year range for title
    years = sorted(set(filtered_data['time_from'].tolist() + filtered_data['time_to'].tolist()))
    year_range = f"{min(years)} → {max(years)}"
    
    # Configurar título com anos
    if title is None:
        fig_title = f"Mudanças do Uso da Terra ({year_range})"
    else:
        fig_title = title
    
    # Academic publication layout styling para multi-step temporal
    fig.update_layout(
        title=dict(
            text=fig_title,
            x=0.5,
            xanchor='center',
            font=dict(
                family="Times New Roman, serif",
                size=16,
                color="black"
            )
        ),
        # Academic font styling
        font=dict(
            family="Times New Roman, serif",
            size=10,
            color="black"
        ),
        # Standard dimensions
        height=600,
        width=1200,
        # Standard margins
        margin=dict(l=80, r=80, t=80, b=80),
        # Clean academic background
        paper_bgcolor='white',
        plot_bgcolor='white',
        # Remove default plotly branding
        showlegend=False
    )
    
    # Adicionar anos como rótulos abaixo do diagrama
    for i, year in enumerate(years_in_data):
        # Calcular posição X com mesmo espaçamento do diagrama
        if len(years_in_data) > 1:
            margin = 0.1
            available_width = 1.0 - 2 * margin
            x_pos = margin + (i / (len(years_in_data) - 1)) * available_width
        else:
            x_pos = 0.5
            
        fig.add_annotation(
            x=x_pos,
            y=-0.05,  # Posicionar abaixo do diagrama
            text=f"<b>{year}</b>",
            showarrow=False,
            font=dict(
                family="Times New Roman, serif",
                size=14,
                color="black"
            ),
            xref="paper",
            yref="paper"
        )
    
    # Save files
    output_path = ensure_output_dir(output_dir)
    filename = "sankey_multi_step"
    saved_path = save_plot_files(fig, output_path, filename, save_png, save_html, is_plotly=True)
    
    # Show plot if requested
    if show_plot and HAS_PLOTLY:
        fig.show()
    
    return saved_path


# Export only the main unified function
__all__ = [
    'plot_sankey',  # Main unified function
]
