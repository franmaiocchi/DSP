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
        plt.stem(ff[0:int(N//2+1)], 2.0/N * np.abs(y[0:int(N//2+1)]))
        plt.xlabel('Frecuencia [Hz]')
        plt.ylabel('Magnitud [V]')
        plt.grid()
    
    return y

def quantizer(x, b, rango):
    """ 
    
    brief:  Cuantizador de b bits
    
    signal:     Señal en el dominio del tiempo
    b:          Cantidad de bits de cuantizador
    rango:      Rango de tensiones de entrada (-rango/2:rango/2)
    
    como resultado la señal devuelve:
    
    signal_q:   Señal cuantizada
    """ 
    # Saturacion
    signal = np.copy(x) # Sin esto, se modifica la señal pasada por parametro
    i = np.where(np.abs(signal) >= rango/2)
    signal[i] = np.round(signal[i])*rango/2
    
    k = pow(2, b - 1) -1
    cuentas = np.round(signal*k/(rango/2))
    signal_q = cuentas*((rango/2)/k)
    
    return signal_q

def energy(x, domain = 'frequency'):

    """ 
    
    brief:  Calcula la energia de la señal
    
    x:          Señal 
    
    como resultado la señal devuelve:
    
    energy:   Energia de la señal
    """ 
    if domain == 'frequency':
        energy = 0
        N = np.shape(x)[0] 
        for bin in x[0:int(N//2+1)]:
            energy = energy + pow(2.0/N * np.abs(bin),2)

    
    return energy
    