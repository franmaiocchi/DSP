# -*- coding: utf-8 -*-
"""
Created on Mon Oct 22 15:51:46 2018

@author: Francisco
"""

import matplotlib as mpl
import matplotlib.pyplot as plt
import pdsmodulos.generador as gen
import numpy as np
import pdsmodulos.tools as tools
from scipy import signal
from scipy.fftpack import fft

def barlett(N):
    
    k = np.linspace(0, (N-1), N)
    w = (2/(N-1))*((N-1)/2 - np.abs(k-(N-1)/2))
    return w

def periodogram(x, N):
    
    y = fft(x)
    psd = pow((1/N)*np.abs(y),2)
    
    return psd

def avg_periodogram(x, N):
    
    y = fft(x, axis = 0)
    psd = pow((1/N)*np.abs(y), 2)
    avg = np.average(psd, axis = 1)
    
    return avg

def window_avg_periodogram(x, window, N):
    
    y = fft(x*window, axis = 0)
    psd = pow((1/N)*np.abs(y), 2)
    avg = np.average(psd, axis = 1)
    
    return avg
    
def testbench():

    fs = 1024   # Frecuencia de muestreo
    N = 1024    # Cantidad de muestras por realizacion
    L = 200     # Cantidad de realizaciones
    
    # Vector de tiempos
    tt = np.linspace(0, (N-1)/fs, N)
    
    # Vector de frecuencias
    df = fs/N
    ff = np.linspace(0, ((N-1)*df), int(N))
    
    # Parametros del ruido blanco gaussiano
    mean = 0
    variance = 2
#%% 
    noises = np.random.normal(mean, np.sqrt(variance), (N, L))
    ruido = noises.reshape(N*L)
    
    psd = periodogram(ruido, N*L)
#    plt.plot(ff[0:int(N//2+1)], psd[0:int(N//2+1)])
    print("Periodograma de " + str(N*L) + " muestras: " + str(np.sum(psd)))
    
    psd = avg_periodogram(noises, N)
    print("Periodograma de " + str(N) + " muestras y " + str(L) + " realizaciones: " + str(np.sum(psd)))
    plt.plot(ff[0:int(N//2+1)], psd[0:int(N//2+1)])
#    noises = np.random.normal(mean, np.sqrt(variance), N*L)
#    ruido = noises.reshape((N,L), order = 'F')
    window = barlett(N)
    window = np.broadcast_to(window, (L, N))
    window = np.transpose(window)
    
    psd = window_avg_periodogram(noises, window, N)
    print("Periodograma de " + str(N) + " muestras y " + str(L) + " realizaciones con ventana: " + str(np.sum(psd)))
    

#%%
testbench()
    