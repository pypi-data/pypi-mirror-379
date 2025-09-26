import os
import numpy as np
from collections import Counter

def ensure_folder(path):
    os.makedirs(path, exist_ok=True)

def export_normalized(export_folder, normalized):
    ensure_folder(export_folder)
    for name, arr in normalized.items():
        np.savetxt(os.path.join(export_folder, f"{name}_normalized.txt"), arr, fmt="%.6f")

def export_binary(export_folder, binary_streams):
    ensure_folder(export_folder)
    for name, bits in binary_streams.items():
        np.savetxt(os.path.join(export_folder, f"{name}_binary_stream.txt"), bits, fmt="%d")

def export_bit_dist(export_folder, binary_streams):
    ensure_folder(export_folder)
    for name, bits in binary_streams.items():
        zeros = int(np.sum(bits == 0))
        ones  = int(np.sum(bits == 1))
        with open(os.path.join(export_folder, f"{name}_bit_distribution.txt"), "w") as f:
            f.write("bit count\n")
            f.write(f"0 {zeros}\n")
            f.write(f"1 {ones}\n")

def export_byte_dist(export_folder, binary_streams):
    ensure_folder(export_folder)
    for name, bits in binary_streams.items():
        byte_array = np.packbits(np.asarray(bits, dtype=np.uint8))
        counts = Counter(byte_array)
        out = sorted(counts.items())
        np.savetxt(os.path.join(export_folder, f"{name}_byte_distribution.txt"),
                   np.array(out, dtype=int), fmt='%d', header='byte count', comments='')