import numpy as np
import os

def load_feature(path):
    """
    Load a 1D numeric feature file. Tries to skip header lines if present.
    """
    if not os.path.isfile(path):
        raise FileNotFoundError(path)
    try:
        data = np.loadtxt(path)
    except Exception:
        # try skipping first line (header)
        data = np.loadtxt(path, skiprows=1)
    data = np.asarray(data).flatten()
    return data

def save_array(path, arr, fmt="%.6f"):
    np.savetxt(path, arr, fmt=fmt)