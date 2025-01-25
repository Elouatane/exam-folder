# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 07:43:28 2024

@author: etudiant17
"""

import numpy as np
import matplotlib.pyplot as plt
import soapy.atmosphere as atm

#from scipy.special import fresnel
def pupil(N,D,x_0=0,y_0=0,c=0.05):
    x=np.linspace(-N//2,N//2,N)

    y=np.linspace(-N//2,N//2,N)
    X,Y=np.meshgrid(x,y)
    r=np.sqrt((X-x_0)**2+(Y-y_0)**2)
    
    pupd= r<=D//2
    OC= r>= c*D/2
    pup0c=pupd*OC
    return pup0c


npix=4

wl=500*10**-9
R=2
amp=1
epsilon=1*np.pi/(3600*180)
r0=(0.98*wl/epsilon)

spx=wl*206265/(2*R*npix)
D=int(1/spx)
N=D*npix
print(spx,r0,epsilon)
pupill=pupil(N,D,c=0)
filtre=np.fft.fftshift(pupil(N,D/2,c=0))
for i in range(30):
    phase=atm.makePhaseScreens(nScrns=10, r0=r0, N=N, 
                               pxlScale=spx, L0=25, l0=0.1)


    onde=pupill*amp*np.exp(1j*pupill*phase[i])
    ampx=filtre*np.fft.fft2(onde)
    pupille2=np.fft.ifft2(ampx)
    ampx2=np.fft.fft2(pupille2)
    Int=np.abs(ampx2)**2
    plt.figure(1)  
    plt.clf()  
    plt.imshow((np.fft.fftshift(Int)))
    plt.pause(0.002)
plt.show()


    