# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 07:10:02 2024

@author: etudiant17
"""

import numpy as np
import matplotlib.pylab as plt
from scipy.special import fresnel
def cosf(x):
    return(np.cos(np.pi*x**2/2))
def sinf(x):
    return(np.sin(np.pi*x**2/2))
#X=(0,10)
N=1000000
Inc,Ins=0,0
x=np.linspace(-10,10,N)
pas=(x[1]-x[0])
for i in x:
    Inc+=sinf(i+pas/2)*pas
    Ins+=cosf(i+pas/2)*pas
print(Inc,Ins)
#print()
s,c=fresnel(10)
print(s,c)
erc=np.abs((c-Inc)/c)*100
ers=np.abs((s-Ins)/s)*100
#print
print(f"""l'erreur relatif est de l'ordre de :erc {erc:0.3f} et ers {ers:0.10f}""")
 
plt.figure("c") 
plt.clf()
plt.title(r'$s(\alpha)$ et $c(\alpha)$',fontsize=18)
plt.plot(x,fresnel(x)[0],label=r'$s(\alpha)$')
plt.plot(x,fresnel(x)[1],label=r'$c(\alpha)$')
plt.xlabel(r"x")
plt.ylabel(r"y")
plt.legend()
plt.grid()
plt.show()

plt.figure("les courbes de corniel") 
plt.clf()
plt.title("les courbes de corniel",fontsize=18)
plt.plot(fresnel(x)[0],fresnel(x)[1],label=r'$s(\alpha)$')

plt.xlabel(r'$c(\alpha)$')
plt.ylabel(r'$s(\alpha)$') 
plt.legend()
plt.grid()
plt.show()
