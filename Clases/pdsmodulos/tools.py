# -*- coding: utf-8 -*-
"""
Created on Sun Sep  2 15:24:27 2018

@author: Francisco
"""

from scipy.fftpack import fft
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

def spectrum_analyzer(x, fs, N, plot = True):
    """ 
    
    brief:  Analizador de espectro
    
    x:      Señal en el dominio del tiempo
    fs:     Frecuencia de muestreo
    N:      Cantidad de muestras de la señal
    plot = True -> Se genera una figure con el espectro
    plot = False -> No se genera ningun plot
    
    como resultado la señal devuelve:
    
    y:      Parte real e imaginaria del espectro 
    ff:     Base de frecuencias
    """ 

    df = fs/N
    ff = np.linspace(0, int((N-1)*df), int(N))
    
    y = fft(x)
    
    if plot == True:
        plt.figure()
        plt.xlabel('f')
        plt.title('Espectro en frecuencia')
        plt.plot(ff[0:(N//2+1)], 2.0/N * np.abs(y[0:(N//2+1)]))
        plt.xlabel('Frecuencia [Hz]')
        plt.ylabel('Magnitud [V]')
        plt.grid()
    
    return ff, y