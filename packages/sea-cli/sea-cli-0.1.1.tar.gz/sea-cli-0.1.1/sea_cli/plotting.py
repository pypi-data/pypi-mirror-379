import matplotlib.pyplot as plt
import numpy as np
from collections import Counter

def plot_normalized_features(normalized, show=True, savepath=None):
    plt.figure(figsize=(8,5))
    for name, data in normalized.items():
        plt.plot(data, label=name.upper())
    plt.legend()
    plt.xlabel('Frame')
    plt.ylabel('Normalized')
    plt.title('Normalized Features')
    plt.grid(True)
    if savepath:
        plt.savefig(savepath, dpi=200)
    if show:
        plt.show()

def plot_binary_heatmap(binary_streams):
    fig, axes = plt.subplots(len(binary_streams), 1, figsize=(10, 6))
    for ax, (name, stream) in zip(axes, binary_streams.items()):
        stream_matrix = stream.reshape(-1, 8)  # 8 bits per byte
        ax.imshow(stream_matrix, cmap="gray_r", aspect="auto", interpolation="nearest")
        ax.set_title(name.upper())
        ax.axis('off')
    plt.suptitle("Figure 4: Binary Streams from Normalized Features")
    plt.tight_layout()
    plt.show()

def plot_bit_distribution(binary_streams):
    fig, axes = plt.subplots(1, len(binary_streams), figsize=(12, 4))
    for ax, (name, stream) in zip(axes, binary_streams.items()):
        ones = np.sum(stream)
        zeros = len(stream) - ones
        ax.bar([0, 1], [zeros, ones], tick_label=["0", "1"])
        ax.set_title(name.upper())
        ax.set_ylabel("Count")
        ax.grid()
    plt.suptitle("Figure 5: Bit Distribution of Binary Encoded Features")
    plt.tight_layout()
    plt.show()

def plot_byte_distribution(binary_streams):
    fig, axes = plt.subplots(1, len(binary_streams), figsize=(15, 5))
    for ax, (name, stream) in zip(axes, binary_streams.items()):
        byte_array = np.packbits(stream)
        counts = Counter(byte_array)
        sorted_vals = sorted(counts.items())
        labels = [f"{x[0]:02X}" for x in sorted_vals]
        values = [x[1] for x in sorted_vals]
        ax.bar(labels, values)
        ax.set_title(name.upper())
        ax.set_ylabel("Frequency")
        ax.set_xticks(range(0, 256, 16))
        ax.set_xticklabels([f"{x:02X}" for x in range(0, 256, 16)], rotation=90)
        ax.grid()
    plt.suptitle("Figure 6: Byte Value Frequency Distribution")
    plt.tight_layout()
    plt.show()

def plot_entropy_summary(entropies):
    features = list(entropies.keys())
    shannon = [e['shannon'] for e in entropies.values()]
    minent = [e['min'] for e in entropies.values()]

    x = np.arange(len(features))
    width = 0.35

    fig, ax = plt.subplots(figsize=(8, 5))
    ax.bar(x - width/2, shannon, width, label='Shannon Entropy')
    ax.bar(x + width/2, minent, width, label='Min-Entropy')
    ax.set_xticks(x)
    ax.set_xticklabels([f.upper() for f in features])
    ax.set_title("Figure 7: Shannon and Min Entropy per Feature")
    ax.legend()
    plt.tight_layout()
    plt.show()

def plot_randomness_statistics(randomness_stats):
    features = list(randomness_stats.keys())

    runs_actual = [r['runs_actual'] for r in randomness_stats.values()]
    runs_expected = [r['runs_expected'] for r in randomness_stats.values()]
    chi_sqs = [r['chi_sq'] for r in randomness_stats.values()]
    serial_corrs = [r['serial_corr'] for r in randomness_stats.values()]

    fig, axs = plt.subplots(3, 1, figsize=(10, 12))

    axs[0].bar(features, runs_actual, label="Actual Runs")
    axs[0].bar(features, runs_expected, alpha=0.5, label="Expected Runs")
    axs[0].set_title("Runs Test")
    axs[0].legend()
    axs[0].grid()

    axs[1].bar(features, chi_sqs, color='orange')
    axs[1].set_title("Chi-Square Statistic")
    axs[1].grid()

    axs[2].bar(features, serial_corrs, color='green')
    axs[2].set_title("Serial Correlation")
    axs[2].grid()

    plt.suptitle("Figure 8: Randomness Evaluation Statistics")
    plt.tight_layout()
    plt.show()

def plot_entropy_fingerprint(entropies):
    labels = ['Shannon', 'Min']
    angles = np.linspace(0, 2 * np.pi, len(labels), endpoint=False).tolist()
    angles += angles[:1]

    fig, ax = plt.subplots(figsize=(6,6), subplot_kw=dict(polar=True))

    for feature, entropy_vals in entropies.items():
        values = [entropy_vals['shannon'], entropy_vals['min']]
        values += values[:1]
        ax.plot(angles, values, label=feature.upper())
        ax.fill(angles, values, alpha=0.25)

    ax.set_thetagrids(np.degrees(angles[:-1]), labels)
    ax.set_title("Figure 9: Entropy Signatures Across Structural Features")
    ax.legend(loc='upper right', bbox_to_anchor=(1.2, 1.1))
    plt.tight_layout()
    plt.show()
