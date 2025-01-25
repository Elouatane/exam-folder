# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 07:18:14 2024

@author: etudiant17
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.special import fresnel

def Intensity(x,z, wl):
    wl=500*10**(-9)
    al=x*np.sqrt(2/(wl*z))
    k=2*np.pi/wl
    amx=(1j+1)/(2j)*np.exp(1j*k*z)*(0.5+fresnel(al)[1]+1j*(0.5+fresnel(al)[0]))
    #NF=a**2/(4*wl*z))
    I=np.abs(amx**np.conj(amx))
    return amx
x=np.linspace(0, 1,10000)
z=0.3
plt.Figure()    
plt.xlabel(r"X")
plt.ylabel(r"intensité")

    