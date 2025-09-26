import os
from .io import load_feature
from .features import normalize_minmax, quantize_to_int, to_bitstream
from .entropy import (shannon_entropy, min_entropy, bit_balance, runs_test,
                      serial_correlation, chi_square_test)
from .export import export_normalized, export_binary, export_bit_dist, export_byte_dist

def run_pipeline(config: dict):
    """
    config: dict with keys:
      'input': {'rmsd': 'rmsd.txt', 'rg': 'rg.txt', 'rmsf': 'rmsf.txt'}
      'bits': 8
      'export_folder': 'Exported_Data'
    """
    inputs = config.get('input', {})
    bits = int(config.get('bits', 8))
    export_folder = config.get('export_folder', 'Exported_Data')

    # load features
    features = {}
    for key, path in inputs.items():
        features[key] = load_feature(path)

    # normalize
    normalized = {k: normalize_minmax(v) for k,v in features.items()}

    # quantize + bitstreams
    ints = {k: quantize_to_int(v, bits=bits) for k,v in normalized.items()}
    bitstreams = {k: to_bitstream(arr, bits=bits) for k,arr in ints.items()}

    # compute metrics
    results = {}
    for name, bits_arr in bitstreams.items():
        results[name] = {
            "shannon": shannon_entropy(bits_arr),
            "min": min_entropy(bits_arr),
            "bit_balance": bit_balance(bits_arr),
            "runs": runs_test(bits_arr),
            "serial_corr": serial_correlation(bits_arr),
            "chi_square": chi_square_test(bits_arr)
        }

    # export
    export_normalized(export_folder, normalized)
    export_binary(export_folder, bitstreams)
    export_bit_dist(export_folder, bitstreams)
    export_byte_dist(export_folder, bitstreams)

    return {"normalized": normalized, "bitstreams": bitstreams, "results": results}