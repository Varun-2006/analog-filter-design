import numpy as np
import matplotlib.pyplot as plt


fs = 10e6

t=np.linspace(0,0.05,int(fs*0.05),endpoint=False)

x = np.sin(2*np.pi*1e2*t) + np.sin(2*np.pi*1e6*t)

X = np.fft.fft(x)

freqs =np.fft.fftfreq(len(X),1/fs)


plt.semilogx(freqs[:len(freqs)//2],20*np.log10(np.abs(X[:len(freqs)//2])))
plt.title('Input signal is frequency domain')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude (dB)')
plt.grid(True)
plt.show()


