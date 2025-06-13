import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import freqs


R1 = 5000/np.pi
R2 = 5000/np.pi
R3 = 0.586e3
R4 = 1e3
C1 = 1e-7
C2 = 1e-7



b = [(1+(R3/R4))/(R1*R2*C1*C2)]
a = [1,(R1*C2+R2*C2-R1*(R3/R4)*C1)/(R1*R2*C1*C2),1/(R1*R2*C1*C2)]


w=np.logspace(-2,8,100000)

w , h = freqs(b,a,w)

dc_gain_db = 20 * np.log10(abs(h[0]))


plt.subplot(2,1,1)
plt.semilogx(w,20*np.log10(abs(h)))
plt.axhline(dc_gain_db - 3.01, color='gray', linestyle='--', label='–3.01 dB from DC gain')
plt.title("Frequency and phase response of second order active low pass filter (Sallen-key)")
plt.ylabel('Magnitude (dB)')
plt.grid(True,which='both',linestyle='--')


plt.subplot(2,1,2)
plt.semilogx(w,np.angle(h,deg=True))
plt.ylabel('Phase (degrees)')
plt.xlabel('Frequency (rad/s)')
plt.grid(True,which='both',linestyle='--')

plt.show()
