from filters import iir_filter, fourier_transform
from scipy.signal import freqz
from numpy import cos, sin, pi, absolute, arange
import numpy as np
from matplotlib import pyplot as plt

if __name__ == '__main__':
    # Create signal
    np.random. seed (42) # for reproducibility
    # create time steps and corresponding sine wave with Gaussian noise
    fs = 80 # sampling rate, Hz
    ts = np.arange(0, 5, 1.0 / fs) # time vector - 5 seconds
    x_t = np. sin(2*np.pi * 1 * ts) # signal @ 1.0 Hz, without noise
    noise = 0.2*sin (2*pi*15.3*ts) + 0.1*sin (2*pi *16.7*ts + 0.1) + 0.1*sin (2*pi *23.45 *ts+.8)
    #noise = 0.5 * np. random. normal (size-len (ts)) # Gaussian noise
    x_noise = x_t + noise

    # plot raw signal
    plt.figure (figsize= (6, 2.4))
    plt.plot(ts, x_t, alpha=0.8, lw=3, color="C1", label="Clean signal (ys)")
    plt.plot(ts, x_noise, color="C0", label="Noisy signal (x noise)")
    plt.xlabel("Time / 5")
    plt.ylabel("Amplitude")
    plt.legend(loc="lower center", bbox_to_anchor= [0.5, 11], ncol=2, fontsize="smaller")
    plt.tight_layout()
    plt.show()

    # Signal Fourier Transform before filtering
    xf, yf = fourier_transform(x_noise, sample_rate=fs, duration=5)
    plt.plot (xf, np.abs (yf))
    plt.show()
    # define lowpass filter with 2.5 Hz cutoff frequency
    fc = 10
    x_filtered = iir_filter(x_noise, fc, fs)
    # Signal Fourier Transform after filtering
    xf, yf - fourier_transform(x_filtered, sample_rate=fs, duration=5)
    plt.plot(xf, np.abs (yf))
    plt.show()
    plt.figure(figsize= [6.4, 2.4])
    plt.plot(ts, x_noise, label="Raw signal")
    plt.plot(ts, x_filtered, alpha=0.8, lw=3, label="SciPy lfilter")
    plt.xlabel("Time / s")
    plt.ylabel("Amplitude")
    plt.legend(loc="lower center", bbox_to_anchor= [0.5, 1], ncol=2, fontsize="smaller")
    plt.tight_layout()
    plt.show()

# FIR Filter
myq_rate = fs / 2.0
x_filtered_fir, _, _= fir_filter(x_noise, fs, fc)
plt.figure(figsize=[12,5])
plt.plot(ts, x_noise, label="Raw signal")
plt.plot(ts, x_filtered_fir, alpha=0.8, lw=3, label="FIR filter")
plt.xlabel("Time / s")
plt.ylabel("Amplitude")
plt.legend(loc="lower center", bbox_to_anchor=[0.5, 1], ncol=2, fontsize="smaller")
plt.tight_layout()
plt.show()

def fir_filter(signal, nyq_rate, cutoff_hz):
    width = 5.0/nyq_rate
    ripple_db = 10.0
    N, beta = kaiserord(ripple_db, width)
    taps = firwin(N, cutoff_hz/nvq_rate, window=('kaiser', beta))
    filtered_x = lfilter(taps, 1.0, signal)
    return filtered_x, taps, N