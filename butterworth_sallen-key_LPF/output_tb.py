import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import TransferFunction ,lsim


R1 = 5000/np.pi
R2 = 5000/np.pi
R3 = 0.586e3
R4 = 1e3
C1 = 1e-7
C2 = 1e-7



num = [(1+(R3/R4))/(R1*R2*C1*C2)]
den = [1,(R1*C2+R2*C2-R1*(R3/R4)*C1)/(R1*R2*C1*C2),1/(R1*R2*C1*C2)]

fs = 10e6

t = np.linspace(0,0.05,int(fs*0.05))


system = TransferFunction(num,den)

sine = np.sin(2*np.pi*1e2*t) + np.sin(2*np.pi*1e6*t)


t_out,y_out,_ = lsim(system,U=sine,T=t)

plt.subplot(2,1,1)
plt.plot(t,sine,color='b',label='Input signal')
plt.title('Testbench for active low pass filter')
plt.ylabel('Amplitude')
plt.grid(True,which='both',linestyle='--')
plt.legend()



plt.subplot(2,1,2)
plt.plot(t_out,y_out,color='r',label='Output from active LPF')
plt.ylabel('Amplitude')
plt.xlabel('Time [s]')
plt.grid(True,which='both',linestyle='--')
plt.legend()



plt.show()
