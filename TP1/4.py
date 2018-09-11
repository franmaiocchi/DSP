# -*- coding: utf-8 -*-
"""
Created on Mon Sep 10 19:48:41 2018

@author: Francisco
"""

import matplotlib as mpl
import matplotlib.pyplot as plt
import pdsmodulos.generador as gen
import numpy as np
import pdsmodulos.tools as tools

def signal_1():
   
    fs = 1000
    N = 1000
    f0 = 9*fs/N
    
    m_f0 = int(N*(f0)/fs)
    
    tt, signal = gen.generador_senoidal(fs, f0, N)
    plt.plot(tt, signal)
    spectrum = tools.spectrum_analyzer(signal, fs, N)
    
    energia_total = tools.energy(spectrum)
    energia_f0 = pow(2.0/N * np.abs(spectrum[m_f0]),2)
    
    print('La energia total es ' + str(energia_total))
    print('La energia en f0 es ' + str(energia_f0))    
    
def signal_2():
    
    fs = 1000
    N = 1000
    f0 = 9*fs/N
    
    m_f0 = int(N*(f0)/fs)
    
    tt, signal = gen.generador_senoidal(fs, f0, N)
    signal[int(fs/f0):] = 0
    plt.plot(tt, signal)
    
    
def signal_3():
    
    fs = 1000
    N = 1000
    
def signal_4():
 
    fs = 1000
    N = 1000
    
def signal_5():
 
    fs = 1000
    N = 1000
    
def signal_6():

    fs = 1000
    N = 1000
    
def signal_7():

    fs = 1000
    N = 1000
    
def signal_8():

    fs = 1000
    N = 1000
    
def signal_9():

    fs = 1000
    N = 1000    

signal_2()