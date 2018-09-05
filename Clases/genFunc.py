# -*- coding: utf-8 -*-
"""
Created on Wed Aug 22 19:58:09 2018

@author: Francisco
"""

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

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
    
    # fin de la función
    
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
        


def testbench ():
    
    N  = 1000 # muestras
    fs = 1000 # Hz
    
#    ##################
#    # a.1) Senoidal #
#    #################
#    
#    a0 = 1 # Volts
#    p0 = 0 # radianes
#    f0 = 10  # Hz
#
#    tiempo, señal = generador_senoidal(fs, f0, N, a0, p0)
#    grafico = plt.plot(tiempo, señal, label = str(f0) + " Hz" )
#    plt.title('Señal: senoidal')
#    plt.xlabel('Tiempo [segundos]')
#    plt.ylabel('Amplitud [V]')
#    axes_hdl = plt.gca()    # Tomo el objeto axes (Lugar donde se grafica)
#    axes_hdl.legend(loc='upper right')

# Prueba sin interpolar los puntos    
#    a0 = 1 # Volts
#    p0 = 0 # radianes
#    f0 = 600   # Hz    
#    
#    tiempo, señal = generador_senoidal(fs, f0, N, a0, p0)
#    grafico = plt.plot(tiempo, señal, 'r+', label = str(f0) + " Hz" )
#    plt.title('Señal: senoidal')
#    plt.xlabel('Tiempo [segundos]')
#    plt.ylabel('Amplitud [V]')
#    axes_hdl = plt.gca()    # Tomo el objeto axes (Lugar donde se grafica)
#    axes_hdl.legend(loc='upper right')
    
    ##################
    # a.2) Senoidal #
    #################
    
#    a0 = 1 # Volts
#    p0 = 0 # radianes
#    f0 = fs/2   # Hz
#    
#    tiempo, señal = generador_senoidal(fs, f0, N, a0, p0)
#    plt.plot(tiempo, señal, label = str(f0) + " Hz" )
    
#    ##################
#    # a.3) Senoidal #
#    #################
#    
#    a0 = 1       # Volts
#    p0 = np.pi/2 # radianes
#    f0 = fs/2    # Hz
#
#    tiempo, señal = generador_senoidal(fs, f0, N, a0, p0)
#    plt.plot(tiempo, señal, label = str(f0) + " Hz" )
    
    # Escribo la leyenda
#    axes_hdl = plt.gca()    # Tomo el objeto axes (Lugar donde se grafica)
#    axes_hdl.legend(loc='upper right')
#    plt.ylim((-1,1))
    
    tt, señal = generador_ruido(1000, 1000, distribution = 'Uniform', low = -1, high = 1)
    plt.subplot(3,1,1)
    plt.plot(tt,señal)
    tt, señal = generador_ruido(1000, 1000, variance = 1)
    plt.subplot(3,1,2)
    plt.plot(tt, señal)
    tt, señal = generador_ruido(1000, 1000, distribution = 'Triangular')
    plt.subplot(3,1,3)
    plt.plot(tt, señal)

testbench()
