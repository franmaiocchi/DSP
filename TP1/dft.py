# -*- coding: utf-8 -*-
"""
Created on Sat Aug 25 15:24:28 2018

@author: Francisco
"""

#%%  Importacion de librerias
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import pdsmodulos.generador as gen

#%%  Funciones
def dft(x):
    
    # Obtengo la cantidad de muestras de la señal
    N = np.shape(x)[0] 
    # Array de salida
    X = np.zeros((int(N/2+1), 1), dtype = np.complex)
    
    for m in range(N//2+1):
        for n in range(N):
            X[m] = X[m] + x[n]*(np.cos(2*np.pi*n*m/N)-1j*np.sin(2*np.pi*n*m/N))
    
    return X

#%% Testbench
def testbench():
    
    fs = 500
    N = 500
    
    a0 = 1
    f0 = 10

    df = fs/N 
    ff = np.linspace(0, int(fs/2), int(N/2 + 1))
    
    tiempo, señal = gen.generador_senoidal(fs, f0, N, a0)
    Y = dft(señal)
    plt.subplot(2,1,1)
    plt.plot(tiempo, señal)
    plt.subplot(2,1,2)
    plt.plot(ff, np.abs(Y))
 
#%% Ejecucion

testbench()

            
        

