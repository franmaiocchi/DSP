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
    i = np.where(np.abs(signal) > rango/2)
    signal[i] = np.sign(signal[i])*rango/2
    
    print(i)
    
    Q = pow(2, b - 1) -1
    cuentas = np.round(signal*Q/(rango/2))
    signal_q = cuentas*((rango/2)/Q)
    
    return signal_q

def quantizer_2(x, b):
    
    signal = np.copy(x)
    signal = signal / np.max(np.abs(signal))
    
    s_real = signal*(pow(2, b-1)-1)
    s_q = np.round(s_real)
    
    return s_q, s_real

def energy(x, domain = 'frequency'):
    
    """ 
    
    brief:  Calcula la energia de la señal
    
    x:          Señal 
    
    como resultado la señal devuelve:
    
    energy:   Energia de la señal
    """ 
    energy = 0
    N = np.shape(x)[0]
    if domain == 'frequency':
        for bin in x[0:int(N//2+1)]:
            energy = energy + pow(2.0/N * np.abs(bin), 2)/2
    if domain == 'time':
        for s in x:
            energy = energy + pow(s, 2)/N

    return energy

def rms(x):
    return np.sqrt(np.mean(np.square(x)))
    
    