#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on ...

@author: Francisco Maiocchi

Descripción
-----------

En este módulo podrías incluir las funciones más generales que quieras usar desde todos los TP's.

"""
import numpy as np

def generador_senoidal (fs, f0, N, a0=1, p0=0):
    """   
    brief:  Generador de señales senoidal, con argumentos
    
    fs:     frecuencia de muestreo de la señal [Hz]
    N:      cantidad de muestras de la señal a generar
    f0:     frecuencia de la senoidal [Hz]
    a0:     amplitud pico de la señal [V]
    p0:     fase de la señal sinusoidal [rad]
    
    como resultado la señal devuelve:
    
    signal: senoidal evaluada en cada instante 
    tt:     base de tiempo de la señal
    """    
    
    # vector de tiempos
    tt = np.linspace(0, (N-1)/fs, N)
    signal = a0*np.sin(2*np.pi*f0*tt + p0)
    
    return tt, signal

def generador_ruido (fs, N, mean = 0, variance = 0, high = 0, low = 0, left = -1, right = 1, peak = 0,  distribution = 'Normal'):
    """ 
    
    brief:  Generador de ruido, con argumentos
    
    fs:     frecuencia de muestreo de la señal [Hz]
    N:      cantidad de muestras de la señal a generar
    distribucion == 'Normal'
        mean: media
        variance: varianza
    distribuccion == 'Uniform'
        low: valor minimo
        high: valor maximo
    distribucion == 'Triangular'
        left: valor minimo
        peak: valor del pico
        right: valor maximo
    
    como resultado la señal devuelve:
    
    signal: ruido con valor medio u y varianza v 
    tt:     base de tiempo de la señal
    """
    # vector de tiempos
    tt = np.linspace(0, (N-1)/fs, N)
    if distribution == 'Normal':
        signal = np.random.normal(mean, np.sqrt(variance), N)  #normal recibe el desvio, no la varianza
    if distribution == 'Uniform':
        signal = np.random.uniform(low, high, N)
    if distribution == 'Triangular':
        signal = np.random.triangular(left, peak, right, N)
    
    return tt, signal      

def generador_cuadrada (a0, f0 , fs, N, d):
    
    tt = np.linspace(0, (N-1)/fs, N)
    
    periodos = int(f0*N/fs)
    
    signal = np.array([], dtype=np.float).reshape(0,1)
    
    for i in range(periodos):
        
        aux = np.concatenate((a0*np.ones(int(np.round(N/periodos*d))),-a0*np.ones(int(np.round(N/periodos*(1-d))))))
        signal = np.vstack([signal, aux.reshape(int(N/periodos),1)])
        
    return signal.reshape(N,)

def generador_triangular (amin, amax, N, d, fs):
    
    tt = np.linspace(0, (N-1)/fs, N)
    Nsim = int(np.round(N*d))
    
    a = amin + (amax - amin)*tt[0:Nsim]/tt[Nsim]
    b = (amin-amax)*tt[Nsim:N]/(tt[N-1] - tt[Nsim]) + amax - (amin-amax)*tt[Nsim]/(tt[N-1] - tt[Nsim])
    
    signal = np.concatenate((a,b))
    return tt, signal
             
    
    
    signal = np.concatenate((a0*np.ones(int(np.round(N*d))),-a0*np.ones(int(np.round(N*(1-d))))))
    return signal