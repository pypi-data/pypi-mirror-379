"""
🔬 LANDUSE INTENSITY ANALYSIS MODULE
===================================

Consolidated analysis functions following OpenLand/Pontius patterns:

📊 Main Analysis Classes:
- LULCAnalysis: Main consolidated analysis following contingencyTable() → intensityAnalysis() workflow
- ChangeMapping: Specialized change detection and mapping functions  
- PersistenceAnalysis: Persistence pattern analysis and stability identification
- TransitionAnalysis: Transition flow analysis and probability matrices

🗺️ TIFF Map Generation:
All classes support saving analysis results as GeoTIFF maps for:
- Persistence maps (by class and duration)
- Change maps (binary, cumulative, transition)
- Hotspot maps (transition concentration areas)
- Summary maps (overall change patterns)

📈 Analysis Workflow:
1. Initialize RasterStack with LULC data
2. Create analysis instances (LULCAnalysis, ChangeMapping, etc.)
3. Run specific analyses or use run_complete_analysis()
4. Generate TIFF maps and CSV reports
5. Export results for GIS visualization

Author: LULC Package Development Team
"""

from .lulc_analysis import LULCAnalysis
from .change_mapping import ChangeMapping
from .persistence_analysis import PersistenceAnalysis
from .transition_analysis import TransitionAnalysis

__all__ = [
    'LULCAnalysis',
    'ChangeMapping', 
    'PersistenceAnalysis',
    'TransitionAnalysis'
]

# Version info for the analysis module
__version__ = "1.0.0"
__author__ = "LULC Package Development Team"

# Analysis workflow constants
ANALYSIS_WORKFLOW = [
    "contingency_table",
    "intensity_analysis", 
    "change_mapping",
    "persistence_analysis",
    "transition_analysis",
    "generate_maps"
]

# Supported map types for TIFF export
SUPPORTED_MAP_TYPES = [
    "binary_change",
    "transition", 
    "cumulative_change",
    "persistence_by_class",
    "persistence_duration", 
    "stability_zones",
    "transition_hotspots",
    "dominant_transitions"
]

__all__ = [
    'LULCAnalysis',
    'ChangeMapping', 
    'TransitionAnalysis',
    'PersistenceAnalysis'
]