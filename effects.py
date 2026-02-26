import numpy as np

def eco(samples, sample_rate, delay_ms=200, decay=0.5):
    delay_samples = int(sample_rate * delay_ms / 1000)
    echo_signal = np.zeros(len(samples) + delay_samples)
    echo_signal[:len(samples)] += samples
    echo_signal[delay_samples:] += samples * decay
    return echo_signal
