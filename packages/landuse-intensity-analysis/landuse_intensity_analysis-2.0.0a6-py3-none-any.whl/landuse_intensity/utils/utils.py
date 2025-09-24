"""
Essential utility functions for land use intensity analysis.

Simplified and modernized utility functions focusing on core functionality.
"""

import numpy as np
import pandas as pd
import re
import os
from typing import Union, Dict, List, Tuple


def demo_landscape(size: int = 100, 
                   classes: List[int] = None, 
                   fractions: List[float] = None) -> np.ndarray:
    """
    Generate demo landscape data for testing and examples.
    
    Parameters
    ----------
    size : int, default 100
        Size of the square landscape (size x size)
    classes : list of int, optional
        Land use classes to use (default: [1, 2, 3, 4])
    fractions : list of float, optional
        Fractions for each class (default: [0.4, 0.3, 0.2, 0.1])
    
    Returns
    -------
    np.ndarray
        Generated landscape array
    """
    if classes is None:
        classes = [1, 2, 3, 4]
    if fractions is None:
        fractions = [0.4, 0.3, 0.2, 0.1]
    
    # Ensure fractions sum to 1
    fractions = np.array(fractions)
    fractions = fractions / fractions.sum()
    
    # Generate landscape
    landscape = np.random.choice(classes, size=(size, size), p=fractions)
    
    return landscape


def load_data(file_path: Union[str, os.PathLike], **kwargs) -> Union[np.ndarray, pd.DataFrame]:
    """
    Load data from various file formats.
    
    Parameters
    ----------
    file_path : str or PathLike
        Path to data file
    **kwargs
        Additional arguments passed to loading functions
        
    Returns
    -------
    np.ndarray or pd.DataFrame
        Loaded data
        
    Raises
    ------
    ValueError
        If file format is not supported
    FileNotFoundError
        If file does not exist
    """
    file_path = str(file_path)
    
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    
    # Determine file format from extension
    ext = os.path.splitext(file_path)[1].lower()
    
    if ext in ['.csv']:
        return pd.read_csv(file_path, **kwargs)
    elif ext in ['.xlsx', '.xls']:
        return pd.read_excel(file_path, **kwargs)
    elif ext in ['.npy']:
        return np.load(file_path, **kwargs)
    elif ext in ['.npz']:
        data = np.load(file_path, **kwargs)
        # Return first array if multiple arrays
        if len(data.files) == 1:
            return data[data.files[0]]
        else:
            return dict(data)
    elif ext in ['.tif', '.tiff']:
        # Import here to avoid circular imports
        from ..processing.raster import read_raster
        data, _ = read_raster(file_path)
        return data
    else:
        raise ValueError(f"Unsupported file format: {ext}")


def save_data(data: Union[np.ndarray, pd.DataFrame], 
              file_path: Union[str, os.PathLike], **kwargs) -> None:
    """
    Save data to various file formats.
    
    Parameters
    ----------
    data : np.ndarray or pd.DataFrame
        Data to save
    file_path : str or PathLike
        Output file path
    **kwargs
        Additional arguments passed to saving functions
    """
    file_path = str(file_path)
    
    # Create directory if it doesn't exist
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    
    # Determine file format from extension
    ext = os.path.splitext(file_path)[1].lower()
    
    if isinstance(data, pd.DataFrame):
        if ext == '.csv':
            data.to_csv(file_path, **kwargs)
        elif ext in ['.xlsx', '.xls']:
            data.to_excel(file_path, **kwargs)
        else:
            raise ValueError(f"Unsupported format for DataFrame: {ext}")
    
    elif isinstance(data, np.ndarray):
        if ext == '.npy':
            np.save(file_path, data, **kwargs)
        elif ext == '.npz':
            np.savez(file_path, data=data, **kwargs)
        elif ext == '.csv':
            np.savetxt(file_path, data, delimiter=',', **kwargs)
        else:
            raise ValueError(f"Unsupported format for numpy array: {ext}")
    
    else:
        raise ValueError(f"Unsupported data type: {type(data)}")


def create_output_directory(base_path: Union[str, os.PathLike], 
                           timestamp: bool = True) -> str:
    """
    Create output directory with optional timestamp.
    
    Parameters
    ----------
    base_path : str or PathLike
        Base path for output directory
    timestamp : bool
        Whether to add timestamp to directory name
        
    Returns
    -------
    str
        Path to created directory
    """
    if timestamp:
        import datetime
        timestamp_str = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        output_dir = os.path.join(base_path, f"output_{timestamp_str}")
    else:
        output_dir = str(base_path)
    
    os.makedirs(output_dir, exist_ok=True)
    return output_dir


def get_class_names(classes: List[int], 
                    class_mapping: Dict[int, str] = None) -> List[str]:
    """
    Get class names from class values.
    
    Parameters
    ----------
    classes : list of int
        Class values
    class_mapping : dict, optional
        Mapping from class values to names
        
    Returns
    -------
    list of str
        Class names
    """
    if class_mapping is None:
        # Default LULC class mapping
        class_mapping = {
            1: 'Urban',
            2: 'Agriculture', 
            3: 'Forest',
            4: 'Water',
            5: 'Grassland',
            6: 'Barren',
            11: 'Water',
            21: 'Developed',
            22: 'Developed_Low',
            23: 'Developed_Med',
            24: 'Developed_High',
            31: 'Barren',
            41: 'Forest_Deciduous',
            42: 'Forest_Evergreen',
            43: 'Forest_Mixed',
            71: 'Grassland',
            81: 'Pasture',
            82: 'Cultivated',
            90: 'Wetland_Woody',
            95: 'Wetland_Herbaceous'
        }
    
    return [class_mapping.get(cls, f'Class_{cls}') for cls in classes]





def validate_data(data: Union[np.ndarray, pd.DataFrame]) -> bool:
    """
    Validate contingency table or raster data.
    
    Parameters
    ----------
    data : array-like
        Data to validate
        
    Returns
    -------
    bool
        True if data is valid, False otherwise
    """
    if data is None:
        return False
    
    if isinstance(data, pd.DataFrame):
        data_array = data.values
    else:
        data_array = np.asarray(data)
    
    # Check for negative values
    if (data_array < 0).any():
        return False
    
    # Check for NaN or infinite values
    if not np.isfinite(data_array).all():
        return False
    
    return True
