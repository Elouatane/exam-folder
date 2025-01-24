import numpy as np
import matplotlib.pyplot as plt

def ouverture(N,D,B):
    x=np.linspace(-N//2,N//2,N)
    y=np.linspace(-N//2,N//2,N)
    X,Y=np.meshgrid(x,y)
    r1=np.sqrt((Y-B/2)**2+(X)**2)
    r2=np.sqrt((Y+B/2)**2+(X)**2)
    pupd1= r1<=D//2
    pupd2= r2<=D//2
    return pupd1,pupd2

npix=30
N=1000
D0=50 #Taille de l'ouverture en pixel pour wl0 \lamda/Dr equivalante N/Dp
M=100 #Dépend de la résolution (100 longueur d'onde)
wll= np.linspace(250,300,M)*10**-9
wl0=np.mean(wll)
P=2*10**-6
interfero=np.zeros((N,N+M))
i=0
interferoN=np.zeros((N,N+M))
for wl in wll:
    D=wl0/wl*D0#Mettre la tache d'airy en dépendence de la longueur d'onde 
    B=3*D
    amp=1
    
    pupill,pupill2=ouverture(N,D,B)
    onde1=pupill*amp*np.exp(1j*pupill*0)
    onde2=pupill2*amp*np.exp(2j*pupill2*np.pi/wl*P)
    ampx=np.fft.fftshift(np.fft.fft2(onde1+onde2))
    ampxN=np.fft.fftshift(np.fft.fft2(onde1))
    
    Int=np.abs(ampx)**2
    IntN=np.abs(ampxN)**2
    #Int=Int/np.max(Int)
    #IntN=IntN/np.max(IntN)
    
    interfero[:,i:N+i]+=Int
    interferoN[:,i:N+i]+=IntN
    i+=1
    





interfero=interfero/(interferoN[N//2,:])[None,:]
interfero = np.nan_to_num(interfero)
InterferoF = np.zeros_like(interfero)
InterferoF[N//2-50:N//2+50,(N+M)//2-M//2:(N+M)//2+M//2] = interfero[N//2-50:N//2+50,(N+M)//2-M//2:(N+M)//2+M//2] 
Pics = np.fft.fft2(InterferoF)

    
plt.figure(1)  
plt.clf()  
plt.imshow(((interfero[N//2-50:N//2+50,(N+M)//2-M//2:(N+M)//2+M//2])))
plt.pause(0.002)
plt.figure(2)  
plt.clf()  
plt.imshow(np.sqrt(np.abs(np.fft.fftshift(Pics.real))))
plt.pause(0.002)
plt.show()
plt.show()

    
    
    


    
    
