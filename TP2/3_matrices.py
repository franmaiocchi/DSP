# -*- coding: utf-8 -*-
"""
Created on Wed Sep 26 21:23:32 2018

@author: Francisco
"""


import matplotlib as mpl
import matplotlib.pyplot as plt
import pdsmodulos.generador as gen
import numpy as np
import pdsmodulos.tools as tools

def testbench():
    
    fs = 1024
    N = 1024
    a0 = 2
    f0 = fs/4
    cantidad_realizaciones = 200
    estimador_a0 = []
    estimador_a1 = []
    
    m_f0 = int(N*(f0)/fs)
    a = m_f0 -2
    b = m_f0 + 2
    
    df = fs/N
    
    fr = gen.generador_ruido(fs, cantidad_realizaciones, low = -2, high = 2, distribution = 'Uniform')
    f1 = f0 + fr
    signals = gen.generador_senoidal(fs, f1, N, a0)    
    
    
#        spectrum = tools.spectrum_analyzer(signal, fs, N, plot = False)
#        estimador_a0.append(2.0/N * np.abs(spectrum[m_f0]))
#        estimador_a1.append(tools.rms(2.0/N * np.abs(spectrum[a:b])))
#        
#    valor_esperado0 = np.average(estimador_a0)
#    sesgo0 = valor_esperado0 - a0
#    varianza0 = np.var(estimador_a0)
#    plt.figure()
#    plt.subplot(2,1,1)
#    plt.title("Estimador a0")
#    plt.xlim((0,2))
#    plt.hist(estimador_a0, bins = 10)
#    print("El sesgo de a0 es " + str(sesgo0))
#    print("La varianza de a0 es " + str(varianza0))
#    
#    valor_esperado1 = np.average(estimador_a1)
#    sesgo1 = valor_esperado1 - a0
#    varianza1 = np.var(estimador_a1)
#    plt.subplot(2,1,2)
#    plt.title("Estimador a1")
#    plt.xlim((0,2))
#    plt.hist(estimador_a1, bins = 10)
#    print("El sesgo de a0 es " + str(sesgo1))
#    print("La varianza de a0 es " + str(varianza1))
    

testbench()