import numpy as np

def pad_tensor(
        tensor: np.ndarray, 
        padding_offset: int, 
        padding_fill_value: float = 0.0) -> np.ndarray:
    """Pad a 2D or 3D tensor with a given value."""
    # CASE 1: 2D matrix
    if tensor.ndim == 2:
        return np.pad(tensor, ((padding_offset, padding_offset), (padding_offset, padding_offset)), mode='constant', constant_values=padding_fill_value)
    # CASE 2: 3D matrix
    else:
        return np.pad(tensor, ((padding_offset, padding_offset), (padding_offset, padding_offset), (padding_offset, padding_offset)), mode='constant', constant_values=padding_fill_value)