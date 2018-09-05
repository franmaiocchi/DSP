# -*- coding: utf-8 -*-
"""
Created on Sat Aug 25 15:22:59 2018

@author: Francisco
"""

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

def generador_ruido (fs, N, mean, variance):
    """ 
    
    brief:  Generador de ruido, con argumentos
    
    fs:     frecuencia de muestreo de la señal [Hz]
    N:      cantidad de muestras de la señal a generar
    u:      media
    v:      varianza
    
    como resultado la señal devuelve:
    
    signal: ruido con valor medio u y varianza v 
    tt:     base de tiempo de la señal
    """
    # vector de tiempos
    tt = np.linspace(0, (N-1)/fs, N)
    signal = np.random.normal(mean, np.sqrt(variance), N)  #normal recibe el desvio, no la varianza
    
    return tt, signal     

def generador_cuadrada (a0, N, d):
    
    signal = np.concatenate((a0*np.ones(int(np.round(N*d))),-a0*np.ones(int(np.round(N*(1-d))))))
    return signal

def generador_triangular (amin, amax, N, d, fs):
    
    tt = np.linspace(0, (N-1)/fs, N)
    Nsim = int(np.round(N*d))
    
    a = amin + (amax - amin)*tt[0:Nsim]/tt[Nsim]
    b = (amin-amax)*tt[Nsim:N]/(tt[N-1] - tt[Nsim]) + amax - (amin-amax)*tt[Nsim]/(tt[N-1] - tt[Nsim])
    
    signal = np.concatenate((a,b))
    return tt, signal
             
    
    
    signal = np.concatenate((a0*np.ones(int(np.round(N*d))),-a0*np.ones(int(np.round(N*(1-d))))))
    return signaldef generador_senoidal (fs, f0, N, a0=1, p0=0):
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

def generador_ruido (fs, N, mean, variance):
    """ 
    
    brief:  Generador de ruido, con argumentos
    
    fs:     frecuencia de muestreo de la señal [Hz]
    N:      cantidad de muestras de la señal a generar
    u:      media
    v:      varianza
    
    como resultado la señal devuelve:
    
    signal: ruido con valor medio u y varianza v 
    tt:     base de tiempo de la señal
    """
    # vector de tiempos
    tt = np.linspace(0, (N-1)/fs, N)
    signal = np.random.normal(mean, np.sqrt(variance), N)  #normal recibe el desvio, no la varianza
    
    return tt, signal     

def generador_cuadrada (a0, N, d):
    
    signal = np.concatenate((a0*np.ones(int(np.round(N*d))),-a0*np.ones(int(np.round(N*(1-d))))))
    return signal

def generador_triangular (amin, amax, N, d, fs):
    
    tt = np.linspace(0, (N-1)/fs, N)
    Nsim = int(np.round(N*d))
    
    a = amin + (amax - amin)*tt[0:Nsim]/tt[Nsim]
    b = (amin-amax)*tt[Nsim:N]/(tt[N-1] - tt[Nsim]) + amax - (amin-amax)*tt[Nsim]/(tt[N-1] - tt[Nsim])
    
    signal = np.concatenate((a,b))
    return tt, signal
             
    
    
    signal = np.concatenate((a0*np.ones(int(np.round(N*d))),-a0*np.ones(int(np.round(N*(1-d))))))
    return signal