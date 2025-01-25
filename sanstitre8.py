import numpy as np 
import matplotlib.pylab as plt 
import sopy.atmosphere as atm 
def pupl (N,D,C=0.5,x0=0,y0=0):
    x=np.linspace(-N/2,N/2,N)
    y=np.linspace(-N/2,N/2,N)
    X,Y=np.meshgrid(x,y)
    
    r=np.sqrt((x-x0)**2 + (y-y0)**2)
     pupld=r=D/2 
     oc=r=C*D/2 
     pulld0=pupld*C 
     return(pulld0)
 npxi=30 
 landa=500*10**-9 
 amp=1 
 e=1*np.pi/(180*3600 )
 spx=(0)
 D=int(1/npxi )
 
 