# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 09:53:32 2024

@author: etudiant17
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 08:05:34 2024

@author: etudiant17
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.special import fresnel

def Intensity(x,y,z, wl=500*10**(-9),a=0.01,b=0.01): 
    k=2*np.pi/wl
    psi=x/(np.sqrt(wl*z))
    xi=y/(np.sqrt(wl*z))
    NF=a**2/((4*wl*z))
    NFb=b**2/((4*wl*z))
    alpha_1=-np.sqrt(2)*(np.sqrt(NF)+psi)
    alpha_2=np.sqrt(2)*(np.sqrt(NF)-psi)
    beta_1=-np.sqrt(2)*(np.sqrt(NFb)+xi)
    beta_2=-np.sqrt(2)*(np.sqrt(NFb)+xi)

    amp=1/2*np.exp(1j*k*z)((fresnel(alpha_2)[1]-fresnel(alpha_1)[1])+1j*(fresnel(alpha_2)[0]-fresnel(alpha_1)[0])*(fresnel(beta_2)[1]-fresnel(beta_1)[1])+1j*(fresnel(beta_2)[0]-fresnel(beta_1)[0]))
    I=np.abs(amp**np.conj(amp))
    return I
a=0.00028023
b=0.00028023
N=1000
x=np.linspace(-0.1,0.1,N)
y=np.linspace(-0.1,0.1,N)
X,Y=np.meshgrid(x,y)

z=300
plt.figure(12)  
plt.clf()  
plt.xlabel(r"X")
plt.ylabel(r"intensité")
plt.plot(x,Intensity(X,Y,z),label="fresnel")
plt.show()
xf = np.zeros_like(x)
spx= (x[-1]-x[0])/N
xa=a//spx
xf[int(N/2-xa/2):int(N/2+xa/2)]=1
amp=np.fft.fft(xf)
plt.figure(132)   
plt.xlabel(r"X")
plt.ylabel(r"intensité")
plt.plot(x,np.fft.fftshift(abs(amp)**2)/np.max(np.fft.fftshift(abs(amp)**2)),label="fraunhofer")
plt.legend()
plt.show()