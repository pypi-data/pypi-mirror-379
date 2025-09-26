import numpy as np

def normalize_minmax(arr):
    arr = np.asarray(arr, dtype=float)
    mn = np.nanmin(arr)
    mx = np.nanmax(arr)
    if mx == mn:
        return np.zeros_like(arr)
    return (arr - mn) / (mx - mn)

def quantize_to_int(arr, bits=8):
    """Convert normalized [0,1] array to integers 0..2^bits-1"""
    arr = np.clip(arr, 0.0, 1.0)
    maxv = 2**bits - 1
    return (arr * maxv).astype(np.uint8)

def to_bitstream(int_array, bits=8):
    """Return flat array of bits (0/1) corresponding to the ints (MSB first)."""
    ints = np.asarray(int_array, dtype=np.uint8).flatten()
    # unpackbits returns big-endian bit order for each byte; returns shape (n,8)
    bits_matrix = np.unpackbits(ints.reshape(-1,1), axis=1)
    return bits_matrix.flatten()