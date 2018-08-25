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

def generador_ruido (fs, N, u, v):
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
    
    a0 = 1 # Volts
    p0 = 0 # radianes
    f0 = fs/2   # Hz
    
    tiempo, señal = generador_senoidal(fs, f0, N, a0, p0)
    plt.plot(tiempo, señal, label = str(f0) + " Hz" )
    
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
#    
#    # Escribo la leyenda
#    axes_hdl = plt.gca()    # Tomo el objeto axes (Lugar donde se grafica)
#    axes_hdl.legend(loc='upper right')
    plt.ylim((-1,1))


testbench()
