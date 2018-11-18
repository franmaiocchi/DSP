# -*- coding: utf-8 -*-
"""
Created on Fri Nov 16 19:37:15 2018

@author: Francisco
"""

import matplotlib as mpl
import matplotlib.pyplot as plt
import pdsmodulos.generador as gen
import numpy as np
import pdsmodulos.tools as tools
from scipy import signal as sig
from scipy.fftpack import fft
import scipy.io as sio

def testbench():
    
    ww, hh3 = sig.freqz(np.array([1/3, 1/3, 1/3]), 1)
    ww, hh4 = sig.freqz(np.array([1/4, 1/4, 1/4, 1/4]), 1)
    ww, hh5 = sig.freqz(np.array([1/5, 1/5, 1/5, 1/5, 1/5]), 1)
    ww = ww / np.pi
    
    plt.figure()
    
    plt.subplot(2,1,1)
    plt.plot(ww, 20 * np.log10(abs(hh3) + np.finfo(float).eps), label='N = 3')
    plt.plot(ww, 20 * np.log10(abs(hh4) + np.finfo(float).eps), label='N = 4')
    plt.plot(ww, 20 * np.log10(abs(hh5) + np.finfo(float).eps), label='N = 5')
    plt.title('Módulo')
    plt.xlabel('Frequencia normalizada')
    plt.ylabel('Módulo [dB]')
    plt.ylim((-80, 5))
    plt.grid()
    
    axes_hdl = plt.gca()
    axes_hdl.legend()
    
    plt.subplot(2,1,2)
    plt.plot(ww, np.unwrap(np.arctan2(np.imag(hh3),np.real(hh3))), label='N = 3')
    plt.plot(ww, np.unwrap(np.arctan2(np.imag(hh4),np.real(hh4))), label='N = 4')
    plt.plot(ww, np.unwrap(np.arctan2(np.imag(hh5),np.real(hh5))), label='N = 5')    
    plt.title('Fase')
    plt.xlabel('Frequencia normalizada')
    plt.ylabel('Fase [rad]')
    plt.grid()
    
    axes_hdl = plt.gca()
    axes_hdl.legend()
    
#    plt.show()
    
testbench()
