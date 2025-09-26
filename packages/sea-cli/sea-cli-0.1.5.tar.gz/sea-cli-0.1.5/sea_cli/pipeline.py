from .io import load_feature
from pathlib import Path
from .features import normalize_minmax, quantize_to_int, to_bitstream
from .entropy import (shannon_entropy, min_entropy, bit_balance, runs_test,
                      serial_correlation, chi_square_test)
from .export import (
    export_normalized, export_binary,
    export_bit_dist,
    export_byte_dist
)
from .plotting import (
    plot_binary_heatmap,
    plot_bit_distribution,
    plot_byte_distribution,
    plot_entropy_summary,
    plot_randomness_statistics,
    plot_entropy_fingerprint,
    plot_normalized_features
)


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
    should_plot = config.get('plot', False)
    # load features
    features = {}
    for key, path in inputs.items():
        features[key] = load_feature(path)

    # normalize
    normalized = {k: normalize_minmax(v) for k, v in features.items()}

    # quantize + bitstreams
    ints = {k: quantize_to_int(v, bits=bits) for k, v in normalized.items()}
    bitstreams = {k: to_bitstream(arr, bits=bits) for k, arr in ints.items()}

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

    # plot

    # Create base savepath string once
    base_savepath = Path(export_folder) / "visualization" / "{}.png"

    # Dictionary mapping plot functions to their file names
    plot_config = {
        plot_normalized_features: ("normalized", normalized),
        plot_binary_heatmap: ("binary_heatmap", bitstreams),
        plot_bit_distribution: ("bit_distribution", bitstreams),
        plot_byte_distribution: ("byte_distribution", bitstreams),
        plot_entropy_summary: ("entropy_summary", results),
        plot_entropy_fingerprint: ("entropy_fingerprint", results),
        plot_randomness_statistics: ("randomness_statistics", results),
    }

    # Create visualization directory if it doesn't exist
    base_savepath.parent.mkdir(parents=True, exist_ok=True)

    # Generate all plots in a loop
    for plot_func, (filename, data) in plot_config.items():
        plot_func(data, show=should_plot,
                  savepath=str(base_savepath).format(filename))
    return {"normalized": normalized, "bitstreams": bitstreams, "results": results}
