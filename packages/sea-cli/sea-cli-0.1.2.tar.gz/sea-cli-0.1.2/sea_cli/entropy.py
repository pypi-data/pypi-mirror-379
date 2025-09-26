import numpy as np
from collections import Counter
import math
from scipy.stats import chi2

def shannon_entropy(bitstream):
    counts = Counter(bitstream)
    total = len(bitstream)
    return -sum((c / total) * math.log2(c / total) for c in counts.values())

def min_entropy(bitstream):
    counts = Counter(bitstream)
    max_p = max(counts.values()) / len(bitstream)
    return -math.log2(max_p)

def bit_balance(bitstream):
    ones = int(np.sum(bitstream))
    zeros = int(len(bitstream) - ones)
    return {"zeros": zeros, "ones": ones, "frac_zero": zeros/len(bitstream), "frac_one": ones/len(bitstream)}

def runs_test(bitstream):
    n = len(bitstream)
    runs = 1
    for i in range(1, n):
        if bitstream[i] != bitstream[i-1]:
            runs += 1
    # expected runs and sigma (Wald–Wolfowitz approx)
    zeros = int(np.sum(bitstream == 0))
    ones = int(np.sum(bitstream == 1))
    expected = (2*zeros*ones)/n + 1
    # variance formula (approx)
    var = (2*zeros*ones*(2*zeros*ones - n)) / (n**2 * (n-1)) if n > 1 else 0
    sigma = np.sqrt(var) if var > 0 else 0.0
    z = (runs - expected) / sigma if sigma > 0 else 0.0
    return {"runs": runs, "expected": expected, "sigma": sigma, "z": z}

def serial_correlation(bitstream):
    b = np.asarray(bitstream, dtype=float)
    mu = b.mean()
    num = ((b[:-1] - mu)*(b[1:] - mu)).sum()
    denom = ((b - mu)**2).sum()
    return num/denom if denom != 0 else 0.0

def chi_square_test(bitstream):
    byte_array = np.packbits(np.asarray(bitstream, dtype=np.uint8))
    counts = Counter(byte_array)
    total = len(byte_array)
    expected = total/256.0
    chi_sq = sum((counts.get(i,0) - expected)**2/expected for i in range(256))
    p_val = 1 - chi2.cdf(chi_sq, df=255)
    return {"chi_sq": chi_sq, "p_value": p_val}