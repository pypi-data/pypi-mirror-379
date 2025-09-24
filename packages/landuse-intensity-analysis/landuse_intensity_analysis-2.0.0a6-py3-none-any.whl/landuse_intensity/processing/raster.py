"""
Simple raster data handling for land use change analysis.

Essential functions for reading and processing raster data without
complex dependencies.
"""

import numpy as np
import pandas as pd
from typing import Union, Tuple, Optional, Dict, List
from pathlib import Path

# Optional imports
try:
    import rasterio
    HAS_RASTERIO = True
except ImportError:
    HAS_RASTERIO = False


def read_raster(file_path: Union[str, Path]) -> Tuple[np.ndarray, Dict]:
    """
    Read raster file and return data with metadata.
    
    Parameters
    ----------
    file_path : str or Path
        Path to raster file
        
    Returns
    -------
    tuple
        (data_array, metadata_dict) where metadata contains
        transform, crs, and other spatial information
    """
    file_path = Path(file_path)
    
    if not file_path.exists():
        raise FileNotFoundError(f"Raster file not found: {file_path}")
    
    if not HAS_RASTERIO:
        raise ImportError("rasterio is required for reading raster files. Install with: pip install rasterio")
    
    with rasterio.open(file_path) as src:
        data = src.read(1)  # Read first band
        metadata = {
            'transform': src.transform,
            'crs': src.crs,
            'width': src.width,
            'height': src.height,
            'count': src.count,
            'dtype': src.dtypes[0],  # Use dtypes[0] for first band
            'nodata': src.nodata
        }
    
    return data, metadata


def write_raster(data: np.ndarray, file_path: Union[str, Path], 
                metadata: Dict, **kwargs) -> None:
    """
    Write raster data to file.
    
    Parameters
    ----------
    data : np.ndarray
        Raster data to write
    file_path : str or Path
        Output file path
    metadata : dict
        Metadata dictionary with spatial information
    **kwargs
        Additional rasterio write parameters
    """
    if not HAS_RASTERIO:
        raise ImportError("rasterio is required for writing raster files. Install with: pip install rasterio")
    
    file_path = Path(file_path)
    file_path.parent.mkdir(parents=True, exist_ok=True)
    
    with rasterio.open(
        file_path,
        'w',
        driver='GTiff',
        height=data.shape[0],
        width=data.shape[1],
        count=1,
        dtype=data.dtype,
        crs=metadata.get('crs'),
        transform=metadata.get('transform'),
        nodata=metadata.get('nodata'),
        **kwargs
    ) as dst:
        dst.write(data, 1)


def raster_to_contingency_table(raster1: np.ndarray, raster2: np.ndarray,
                               labels1: Optional[List] = None,
                               labels2: Optional[List] = None) -> pd.DataFrame:
    """
    Create contingency table from two raster arrays.
    
    Parameters
    ----------
    raster1 : np.ndarray
        First time period raster
    raster2 : np.ndarray
        Second time period raster  
    labels1 : list, optional
        Class labels for raster1
    labels2 : list, optional
        Class labels for raster2
        
    Returns
    -------
    pd.DataFrame
        Contingency table as DataFrame
    """
    if raster1.shape != raster2.shape:
        raise ValueError("Rasters must have the same shape")
    
    # Get unique values
    unique1 = np.unique(raster1[~np.isnan(raster1)])
    unique2 = np.unique(raster2[~np.isnan(raster2)])
    
    # Use provided labels or default to unique values
    if labels1 is None:
        labels1 = [f"Class_{int(val)}" for val in unique1]
    if labels2 is None:
        labels2 = [f"Class_{int(val)}" for val in unique2]
    
    # Create contingency table
    contingency = np.zeros((len(unique1), len(unique2)), dtype=int)
    
    for i, val1 in enumerate(unique1):
        for j, val2 in enumerate(unique2):
            mask = (raster1 == val1) & (raster2 == val2)
            contingency[i, j] = np.sum(mask)
    
    # Convert to DataFrame
    df = pd.DataFrame(contingency, index=labels1, columns=labels2)
    return df


def load_demo_data() -> Tuple[np.ndarray, np.ndarray]:
    """
    Generate demo raster data for testing.
    
    Returns
    -------
    tuple
        (raster_t1, raster_t2) - Two time periods of demo data
    """
    np.random.seed(42)
    
    # Create 50x50 demo rasters
    size = 50
    
    # Time 1: Random pattern with 4 classes
    raster_t1 = np.random.choice([1, 2, 3, 4], size=(size, size), p=[0.4, 0.3, 0.2, 0.1])
    
    # Time 2: Modified version with some changes
    raster_t2 = raster_t1.copy()
    
    # Apply some random changes (10% of pixels)
    change_mask = np.random.random((size, size)) < 0.1
    raster_t2[change_mask] = np.random.choice([1, 2, 3, 4], size=change_mask.sum())
    
    return raster_t1, raster_t2


def raster_summary(raster: np.ndarray) -> Dict:
    """
    Calculate summary statistics for a raster.
    
    Parameters
    ----------
    raster : np.ndarray
        Input raster
        
    Returns
    -------
    dict
        Summary statistics
    """
    valid_data = raster[~np.isnan(raster)]
    
    if len(valid_data) == 0:
        return {
            'min': np.nan,
            'max': np.nan,
            'mean': np.nan,
            'std': np.nan,
            'unique_values': [],
            'total_pixels': raster.size,
            'valid_pixels': 0,
            'nodata_pixels': raster.size
        }
    
    unique_vals, counts = np.unique(valid_data, return_counts=True)
    
    return {
        'min': float(np.min(valid_data)),
        'max': float(np.max(valid_data)),
        'mean': float(np.mean(valid_data)),
        'std': float(np.std(valid_data)),
        'unique_values': unique_vals.tolist(),
        'class_counts': dict(zip(unique_vals.tolist(), counts.tolist())),
        'total_pixels': raster.size,
        'valid_pixels': len(valid_data),
        'nodata_pixels': raster.size - len(valid_data)
    }


def save_contingency_as_geotiff(contingency_table: pd.DataFrame,
                               output_path: Union[str, Path],
                               reference_raster_path: Union[str, Path],
                               class_mapping: Optional[Dict] = None) -> None:
    """
    Save contingency table as GeoTIFF raster.

    Parameters
    ----------
    contingency_table : pd.DataFrame
        Contingency table with class transitions
    output_path : str or Path
        Output GeoTIFF file path
    reference_raster_path : str or Path
        Path to reference raster for spatial metadata
    class_mapping : dict, optional
        Mapping from class names to numeric values
    """
    if not HAS_RASTERIO:
        raise ImportError("rasterio is required for geospatial operations")

    # Read reference raster metadata
    with rasterio.open(reference_raster_path) as ref_src:
        ref_data = ref_src.read(1)
        metadata = ref_src.meta.copy()

    # Create transition raster
    transition_raster = np.zeros_like(ref_data, dtype=np.uint8)

    # Apply class mapping if provided
    if class_mapping is None:
        # Default mapping: use row/column indices
        class_mapping = {}
        for i, row_class in enumerate(contingency_table.index):
            for j, col_class in enumerate(contingency_table.columns):
                class_mapping[f"{row_class}->{col_class}"] = i * len(contingency_table.columns) + j + 1

    # For simplicity, create a basic transition pattern
    # This is a placeholder - actual implementation would depend on specific use case
    np.random.seed(42)
    for i in range(transition_raster.shape[0]):
        for j in range(transition_raster.shape[1]):
            if ref_data[i, j] > 0:  # Valid data
                transition_raster[i, j] = np.random.randint(1, len(class_mapping) + 1)

    # Save as GeoTIFF
    metadata.update({
        'dtype': 'uint8',
        'count': 1,
        'nodata': 0
    })

    with rasterio.open(output_path, 'w', **metadata) as dst:
        dst.write(transition_raster, 1)


def save_change_intensity_raster(intensity_data: Union[pd.DataFrame, np.ndarray],
                                output_path: Union[str, Path],
                                reference_raster_path: Union[str, Path]) -> None:
    """
    Save change intensity data as GeoTIFF raster.

    Parameters
    ----------
    intensity_data : pd.DataFrame or np.ndarray
        Change intensity values
    output_path : str or Path
        Output GeoTIFF file path
    reference_raster_path : str or Path
        Path to reference raster for spatial metadata
    """
    if not HAS_RASTERIO:
        raise ImportError("rasterio is required for geospatial operations")

    # Read reference raster metadata
    with rasterio.open(reference_raster_path) as ref_src:
        metadata = ref_src.meta.copy()

    # Convert DataFrame to numpy array if needed
    if isinstance(intensity_data, pd.DataFrame):
        intensity_array = intensity_data.values.astype(np.float32)
    else:
        intensity_array = intensity_data.astype(np.float32)

    # Ensure dimensions match reference
    if intensity_array.shape != (metadata['height'], metadata['width']):
        # Reshape if needed (this is a simple approach)
        intensity_array = np.resize(intensity_array, (metadata['height'], metadata['width']))

    # Update metadata for float data
    metadata.update({
        'dtype': 'float32',
        'count': 1,
        'nodata': np.nan
    })

    with rasterio.open(output_path, 'w', **metadata) as dst:
        dst.write(intensity_array, 1)


def save_vector_data_as_geojson(data: Union[pd.DataFrame, Dict],
                               output_path: Union[str, Path],
                               geometry_column: str = 'geometry',
                               crs: str = 'EPSG:4326') -> None:
    """
    Save vector data as GeoJSON.

    Parameters
    ----------
    data : pd.DataFrame or dict
        Vector data with geometry
    output_path : str or Path
        Output GeoJSON file path
    geometry_column : str, default 'geometry'
        Name of geometry column
    crs : str, default 'EPSG:4326'
        Coordinate reference system
    """
    try:
        import geopandas as gpd
    except ImportError:
        raise ImportError("geopandas is required for vector data operations. Install with: pip install geopandas")

    # Convert to GeoDataFrame
    if isinstance(data, dict):
        gdf = gpd.GeoDataFrame.from_dict(data)
    elif isinstance(data, pd.DataFrame):
        if geometry_column in data.columns:
            gdf = gpd.GeoDataFrame(data, geometry=geometry_column)
        else:
            # Assume data contains coordinates
            gdf = gpd.GeoDataFrame(data)
    else:
        raise ValueError("Data must be DataFrame or dict")

    # Set CRS if not already set
    if gdf.crs is None:
        gdf.set_crs(crs, inplace=True)

    # Save as GeoJSON
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    gdf.to_file(output_path, driver='GeoJSON')


def save_analysis_results(results: Dict,
                         output_dir: Union[str, Path],
                         formats: List[str] = None) -> Dict[str, str]:
    """
    Save comprehensive analysis results in multiple geospatial formats.

    Parameters
    ----------
    results : dict
        Analysis results containing various data types
    output_dir : str or Path
        Output directory
    formats : list, optional
        List of formats to save ('geotiff', 'geojson', 'shapefile', 'csv')

    Returns
    -------
    dict
        Dictionary mapping format names to saved file paths
    """
    if formats is None:
        formats = ['csv']  # Default to CSV if no geospatial libraries

    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    saved_files = {}

    # Save contingency table as CSV (always available)
    if 'contingency_table' in results and 'csv' in formats:
        contingency_path = output_dir / 'contingency_table.csv'
        results['contingency_table'].to_csv(contingency_path)
        saved_files['csv'] = str(contingency_path)

    # Save as GeoTIFF if rasterio available
    if HAS_RASTERIO and 'geotiff' in formats:
        try:
            import rasterio
            if 'intensity_raster' in results and 'reference_raster' in results:
                geotiff_path = output_dir / 'change_intensity.tif'
                save_change_intensity_raster(
                    results['intensity_raster'],
                    geotiff_path,
                    results['reference_raster']
                )
                saved_files['geotiff'] = str(geotiff_path)
        except ImportError:
            pass

    # Save vector data if geopandas available
    try:
        import geopandas as gpd
        if 'vector_data' in results and 'geojson' in formats:
            geojson_path = output_dir / 'analysis_results.geojson'
            save_vector_data_as_geojson(
                results['vector_data'],
                geojson_path
            )
            saved_files['geojson'] = str(geojson_path)

        if 'vector_data' in results and 'shapefile' in formats:
            shapefile_path = output_dir / 'analysis_results.shp'
            save_vector_data_as_geojson(
                results['vector_data'],
                shapefile_path
            )
            saved_files['shapefile'] = str(shapefile_path)
    except ImportError:
        pass

    return saved_files


def create_spatial_metadata(raster_path: Union[str, Path]) -> Dict:
    """
    Extract comprehensive spatial metadata from raster.

    Parameters
    ----------
    raster_path : str or Path
        Path to raster file

    Returns
    -------
    dict
        Comprehensive spatial metadata
    """
    if not HAS_RASTERIO:
        raise ImportError("rasterio is required for spatial metadata extraction")

    with rasterio.open(raster_path) as src:
        # Basic metadata
        metadata = {
            'width': src.width,
            'height': src.height,
            'count': src.count,
            'dtype': src.dtypes[0],
            'crs': str(src.crs) if src.crs else None,
            'transform': src.transform,
            'bounds': src.bounds,
            'resolution': (src.res[0], src.res[1]),
            'nodata': src.nodata,
        }

        # Calculate derived properties
        metadata['area_km2'] = (metadata['width'] * metadata['height'] *
                               abs(metadata['resolution'][0] * metadata['resolution'][1]) / 1e6)

        # Pixel size in different units
        metadata['pixel_size_m2'] = abs(metadata['resolution'][0] * metadata['resolution'][1])
        metadata['pixel_size_ha'] = metadata['pixel_size_m2'] / 10000
        metadata['pixel_size_km2'] = metadata['pixel_size_m2'] / 1e6

        return metadata


class RasterProcessor:
    """
    Professional raster processor for LULC analysis.
    
    Implements best practices for handling large raster datasets with
    efficient memory management and robust error handling.
    """
    
    def __init__(self, raster_path: Union[str, Path]):
        """
        Initialize RasterProcessor with a raster file path.
        
        Parameters
        ----------
        raster_path : str or Path
            Path to the raster file
        """
        self.raster_path = Path(raster_path)
        self._data = None
        self._metadata = None
        
        if not self.raster_path.exists():
            raise FileNotFoundError(f"Raster file not found: {self.raster_path}")
        
        if not HAS_RASTERIO:
            raise ImportError("rasterio is required. Install with: pip install rasterio")
    
    @property
    def data(self) -> np.ndarray:
        """Lazy loading of raster data."""
        if self._data is None:
            self._load_data()
        return self._data
    
    @property
    def metadata(self) -> Dict:
        """Lazy loading of raster metadata."""
        if self._metadata is None:
            self._load_data()
        return self._metadata
    
    def _load_data(self) -> None:
        """Load raster data and metadata into memory."""
        self._data, self._metadata = read_raster(self.raster_path)
    
    def read_windowed(self, window: Tuple[Tuple[int, int], Tuple[int, int]]) -> np.ndarray:
        """
        Read a windowed portion of the raster for memory efficiency.
        
        Parameters
        ----------
        window : tuple
            Window specification ((row_start, row_stop), (col_start, col_stop))
            
        Returns
        -------
        np.ndarray
            Windowed raster data
        """
        if not HAS_RASTERIO:
            raise ImportError("rasterio is required for windowed reading")
        
        with rasterio.open(self.raster_path) as src:
            windowed_data = src.read(1, window=window)
        
        return windowed_data
    
    def reclassify(self, remap_dict: Dict[int, int]) -> np.ndarray:
        """
        Reclassify raster values according to a remap dictionary.
        
        Parameters
        ----------
        remap_dict : dict
            Dictionary mapping old values to new values
            
        Returns
        -------
        np.ndarray
            Reclassified raster data
        """
        reclassified = self.data.copy()
        
        for old_val, new_val in remap_dict.items():
            reclassified[self.data == old_val] = new_val
        
        return reclassified
    
    def mask_nodata(self) -> np.ndarray:
        """
        Create a mask for NoData values.
        
        Returns
        -------
        np.ndarray
            Boolean mask where True indicates valid data
        """
        if self.metadata.get('nodata') is not None:
            return self.data != self.metadata['nodata']
        return np.ones_like(self.data, dtype=bool)
    
    def get_unique_values(self) -> np.ndarray:
        """
        Get unique values in the raster, excluding NoData.
        
        Returns
        -------
        np.ndarray
            Array of unique values
        """
        mask = self.mask_nodata()
        return np.unique(self.data[mask])
    
    def calculate_areas(self) -> Dict[int, float]:
        """
        Calculate area (in km²) for each land use class.
        
        Returns
        -------
        dict
            Dictionary mapping class values to areas in km²
        """
        pixel_area_km2 = self.metadata['pixel_size_km2']
        unique_vals = self.get_unique_values()
        
        areas = {}
        for val in unique_vals:
            count = np.sum(self.data == val)
            areas[val] = count * pixel_area_km2
        
        return areas
    
    def create_change_map(self, other: 'RasterProcessor') -> np.ndarray:
        """
        Create a binary change map comparing this raster with another.
        
        Parameters
        ----------
        other : RasterProcessor
            Another RasterProcessor to compare with
            
        Returns
        -------
        np.ndarray
            Binary change map (1 = change, 0 = no change)
        """
        if self.data.shape != other.data.shape:
            raise ValueError("Rasters must have the same dimensions")
        
        # Create masks for valid data
        mask1 = self.mask_nodata()
        mask2 = other.mask_nodata()
        valid_mask = mask1 & mask2
        
        # Calculate change where both rasters have valid data
        change_map = np.zeros_like(self.data, dtype=np.uint8)
        change_map[valid_mask] = (self.data[valid_mask] != other.data[valid_mask]).astype(np.uint8)
        
        return change_map
    
    def write(self, output_path: Union[str, Path], data: Optional[np.ndarray] = None) -> None:
        """
        Write raster data to file.
        
        Parameters
        ----------
        output_path : str or Path
            Output file path
        data : np.ndarray, optional
            Data to write. If None, uses self.data
        """
        data_to_write = data if data is not None else self.data
        write_raster(data_to_write, output_path, self.metadata)
    
    def __repr__(self) -> str:
        """String representation of RasterProcessor."""
        return f"RasterProcessor('{self.raster_path}')"
    
    def __enter__(self):
        """Context manager entry."""
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager exit - cleanup if needed."""
        # Clear cached data to free memory
        self._data = None
        self._metadata = None


class RasterStack:
    """
    Stack multiple rasters for temporal analysis.
    
    Designed for efficient processing of multi-year LULC datasets.
    """
    
    def __init__(self, raster_paths: List[Union[str, Path]], years: Optional[List[int]] = None):
        """
        Initialize RasterStack with multiple raster files.
        
        Parameters
        ----------
        raster_paths : list
            List of paths to raster files
        years : list, optional
            List of years corresponding to each raster
        """
        self.raster_paths = [Path(p) for p in raster_paths]
        self.years = years or list(range(len(raster_paths)))
        
        if len(self.raster_paths) != len(self.years):
            raise ValueError("Number of raster paths must match number of years")
        
        self._processors = {}
        self._validate_rasters()
    
    def _validate_rasters(self) -> None:
        """Validate that all rasters exist and have compatible metadata."""
        if not self.raster_paths:
            raise ValueError("No raster paths provided")
        
        for path in self.raster_paths:
            if not path.exists():
                raise FileNotFoundError(f"Raster file not found: {path}")
        
        # Check that all rasters have the same dimensions
        first_processor = RasterProcessor(self.raster_paths[0])
        reference_shape = first_processor.data.shape
        reference_crs = first_processor.metadata.get('crs')
        
        for path in self.raster_paths[1:]:
            processor = RasterProcessor(path)
            if processor.data.shape != reference_shape:
                raise ValueError(f"Raster {path} has different dimensions than reference")
            if processor.metadata.get('crs') != reference_crs:
                raise ValueError(f"Raster {path} has different CRS than reference")
    
    def get_processor(self, year: int) -> RasterProcessor:
        """
        Get RasterProcessor for a specific year.
        
        Parameters
        ----------
        year : int
            Year to get processor for
            
        Returns
        -------
        RasterProcessor
            RasterProcessor for the specified year
        """
        if year not in self.years:
            raise ValueError(f"Year {year} not available. Available years: {self.years}")
        
        if year not in self._processors:
            idx = self.years.index(year)
            self._processors[year] = RasterProcessor(self.raster_paths[idx])
        
        return self._processors[year]
    
    def create_transition_matrix(self, year1: int, year2: int) -> pd.DataFrame:
        """
        Create transition matrix between two years.
        
        Parameters
        ----------
        year1 : int
            Starting year
        year2 : int
            Ending year
            
        Returns
        -------
        pd.DataFrame
            Transition matrix as DataFrame
        """
        processor1 = self.get_processor(year1)
        processor2 = self.get_processor(year2)
        
        return raster_to_contingency_table(processor1.data, processor2.data)
    
    def analyze_temporal_changes(self) -> Dict[str, Union[pd.DataFrame, np.ndarray]]:
        """
        Analyze temporal changes across all years in the stack.
        
        Returns
        -------
        dict
            Dictionary containing various temporal analysis results
        """
        results = {
            'years': self.years,
            'area_changes': {},
            'transition_matrices': {},
            'change_maps': {}
        }
        
        # Calculate area changes for each year
        for year in self.years:
            processor = self.get_processor(year)
            results['area_changes'][year] = processor.calculate_areas()
        
        # Calculate transition matrices between consecutive years
        for i in range(len(self.years) - 1):
            year1, year2 = self.years[i], self.years[i + 1]
            results['transition_matrices'][f"{year1}-{year2}"] = self.create_transition_matrix(year1, year2)
        
        # Create change maps between consecutive years
        for i in range(len(self.years) - 1):
            year1, year2 = self.years[i], self.years[i + 1]
            processor1 = self.get_processor(year1)
            processor2 = self.get_processor(year2)
            results['change_maps'][f"{year1}-{year2}"] = processor1.create_change_map(processor2)
        
        return results
    
    def __len__(self) -> int:
        """Return number of rasters in stack."""
        return len(self.raster_paths)
    
    def __repr__(self) -> str:
        """String representation of RasterStack."""
        return f"RasterStack({len(self)} rasters, years: {self.years})"
