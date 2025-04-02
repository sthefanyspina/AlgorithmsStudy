#The Fast Fourier Transform (FFT) is a powerful algorithm used to compute the Discrete Fourier Transform (DFT) of a sequence efficiently. The DFT itself is a way to analyze the frequency content of a signal, and the FFT is an optimized method for calculating it.

#Overview of Fourier Transform
#The Fourier Transform converts a signal from the time domain into the frequency domain. This transformation helps in understanding the frequency components of a signal. For a discrete sequence of data, we use the Discrete Fourier Transform (DFT): X(k)= N−1∑ n=0 x(n)e - 2πi /N kn
#Where: X(k) is the Fourier transform of x(n).
#N is the number of points in the signal.
#i is the imaginary unit.

#Calculating DFT directly can be computationally expensive, with a time complexity of O(N^2). The Fast Fourier Transform (FFT) reduces this complexity to  O(NlogN), making it much faster, especially for large datasets.

#FFT in Python
#In Python, the numpy library provides an efficient implementation of FFT through the numpy.fft module. Here's a step-by-step explanation of how to use FFT in Python:

#1. Importing Necessary Libraries
#You'll need the numpy library to perform the FFT.

import numpy as np
import matplotlib.pyplot as plt

#2. Creating a Sample Signal
#Let's create a sample signal that we will analyze using FFT. We'll create a combination of two sine waves with different frequencies.

# Sample rate and time vector
fs = 1000  # Sampling frequency (samples per second)
t = np.arange(0, 1, 1/fs)  # Time vector from 0 to 1 second with step 1/fs

# Create a signal with two frequencies: 50 Hz and 150 Hz
f1, f2 = 50, 150  # Frequencies in Hz
signal = np.sin(2 * np.pi * f1 * t) + np.sin(2 * np.pi * f2 * t)

#3. Applying the FFT
#Now, we can apply the FFT to the signal. The np.fft.fft() function computes the FFT of the signal.

# Perform the FFT
fft_signal = np.fft.fft(signal)

# Calculate the corresponding frequencies for the FFT output
frequencies = np.fft.fftfreq(len(t), 1/fs)

#4. Magnitude of the FFT
#The FFT result is a complex number. To analyze the frequency components, we usually look at the magnitude (the absolute value) of the FFT result.

# Magnitude of the FFT
magnitude = np.abs(fft_signal)

# Only keep the positive frequencies (the FFT is symmetric)
positive_freqs = frequencies[:len(frequencies)//2]
positive_magnitude = magnitude[:len(magnitude)//2]

#5. Plotting the Signal and its Frequency Spectrum
#Let's plot both the original signal and its frequency spectrum (magnitude of FFT) to see how the signal is distributed in the frequency domain.

# Plot the original signal in the time domain
plt.figure(figsize=(12, 6))

# Time domain plot
plt.subplot(2, 1, 1)
plt.plot(t, signal)
plt.title("Time Domain Signal")
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")

# Frequency domain plot (magnitude of FFT)
plt.subplot(2, 1, 2)
plt.plot(positive_freqs, positive_magnitude)
plt.title("Frequency Domain (FFT)")
plt.xlabel("Frequency [Hz]")
plt.ylabel("Magnitude")
plt.tight_layout()

plt.show()

#Explanation of the Code:
# 1 - Signal Creation: We created a signal consisting of two sine waves with frequencies of 50 Hz and 150 Hz.
# 2 - FFT: np.fft.fft() is used to compute the FFT of the signal. This returns a complex array where each value corresponds to a frequency component of the signal.
# 3 - Magnitude: np.abs() is used to compute the magnitude of each FFT result, as we are interested in the strength of the frequency components.
# 4 - Frequency Axis: np.fft.fftfreq() generates the corresponding frequency axis for the FFT result. The frequency range goes from −fs/2 to  fs/2, but we only keep the positive frequencies for visualization.
# 5 - Plotting: The time-domain plot shows how the signal behaves over time, while the frequency-domain plot reveals the frequency components present in the signal.

#Output:
#The time-domain plot shows the signal as a combination of two sine waves. The frequency-domain plot shows two peaks at 50 Hz and 150 Hz, which correspond to the two sine waves present in the signal.

#Key Points:
# 1 - The FFT is an efficient algorithm for calculating the DFT of a sequence.
# 2 - numpy.fft.fft() is the function used to compute the FFT in Python.
# 3 - The result of the FFT is complex, and the magnitude (np.abs()) of the FFT gives the frequency strength.
# 4 - The frequency axis for FFT output can be generated using np.fft.fftfreq().
