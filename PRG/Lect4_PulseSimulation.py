import datetime
print('Hi! What\'s up? \nToday is ', datetime.datetime.today(), ' in UTC \n')

# Simulates wave form pulsar pulse profile with random noise-like 
# amplitudes and random phases
# Adds a scattering tale 
# Deconvolves with different scattering models
# Learn subplots

import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
from numpy import pi as PI
from numpy import exp as EXP

N = 1000
dt=0.5 #ms
#step = [x/10 for x in range(N)] 
Time = [x*dt for x in range(N)]

#data = [gauss for x in range(N)]

noise = np.random.normal(0, 0.2, N)
Phi = np.random.rand(N)*2*np.pi
G = signal.gaussian(N, std=N/80)

Pulse = noise+G

Signal = Pulse*EXP(-1j*2*PI*Phi)

Signal_sp = np.fft.fft(Signal)

tau = N/100
#Scat = [EXP(-x/tau) for x in range(int(N/2))]
Scat = [0]*int(N/2)+[EXP(-x/tau) for x in range(int(N/2))]

Pulse_scat = np.convolve(Signal, Scat) 

fig, axs = plt.subplots(3, 1)
axs[0].plot(Time, Pulse)
#axs[0].set_xlim(0, Time(N))
axs[0].set_xlabel('time')
axs[0].set_ylabel('amplitude')
axs[0].grid(True)

axs[1].plot(Scat)
#axs[1].set_xlim(0, int(N/2))
axs[1].set_xlabel('time')
axs[1].set_ylabel('amplitude')
axs[1].grid(True)

axs[2].plot(Pulse_scat)
#axs[2].set_xlim(0, Time(N))
axs[2].set_xlabel('time')
axs[2].set_ylabel('amplitude')
axs[2].grid(True)

plt.savefig('ModelPulse.jpg', dpi=100)

"""
mpl.figure(2)
mpl.plot(Pulse_scat)
mpl.xlabel('time')
mpl.ylabel('power')
mpl.title('Simulated pulse')
"""
