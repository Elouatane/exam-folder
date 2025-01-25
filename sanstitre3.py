# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 08:05:34 2024

@author: etudiant17
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.special import fresnel

def Intensity(x,z, wl=500*10**(-9),a=0.01): 
    psi=x/(np.sqrt(wl*z))
    
    NF=a**2/((4*wl*z))
    alpha_1=-np.sqrt(2)*(np.sqrt(NF)+psi)
    alpha_2=np.sqrt(2)*(np.sqrt(NF)-psi)

    I=1/2*((fresnel(alpha_2)[1]-fresnel(alpha_1)[1])**2+(fresnel(alpha_2)[0]-fresnel(alpha_1)[0])**2)
    return I
a=0.00028023
N=10000
x=np.linspace(-0.1,0.1,N)

z=300
plt.figure(12)  
plt.clf()  
plt.xlabel(r"X")
plt.ylabel(r"intensité")
plt.plot(x,Intensity(x,z)/np.max(Intensity(x, z)),label="fresnel")
plt.show()
xf = np.zeros_like(x)
spx= (x[-1]-x[0])/N
xa=a//spx
xf[int(N//2-xa//2):int(N//2+xa//2)]=1
amp=np.fft.fft(xf)
plt.figure(12)   
plt.xlabel(r"X")
plt.ylabel(r"intensité")
plt.plot(x,np.fft.fftshift(abs(amp)**2)/np.max(np.fft.fftshift(abs(amp)**2)),label="fraunhofer")
plt.legend()
plt.show()