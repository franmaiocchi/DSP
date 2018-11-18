# -*- coding: utf-8 -*-
"""
Created on Sat Nov 17 20:00:42 2018

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
    
    ww, hh2 = sig.freqz(np.array([1, 0, -1]), 1)
    ww, hh3 = sig.freqz(np.array([1, 0, 0, -1]), 1)
    ww, hh4 = sig.freqz(np.array([1, 0, 0, 0, -1]), 1)
    ww = ww / np.pi
    
    plt.figure()
    
    plt.subplot(2,1,1)
    plt.plot(ww, 20 * np.log10(abs(hh2) + np.finfo(float).eps), label='N = 2')
    plt.plot(ww, 20 * np.log10(abs(hh3) + np.finfo(float).eps), label='N = 3')
    plt.plot(ww, 20 * np.log10(abs(hh4) + np.finfo(float).eps), label='N = 4')
    plt.title('Módulo')
    plt.xlabel('Frequencia normalizada')
    plt.ylabel('Módulo [dB]')
    plt.ylim((-80, 20))
    plt.grid()
    
    axes_hdl = plt.gca()
    axes_hdl.legend()
    
    plt.subplot(2,1,2)
    plt.plot(ww, np.unwrap(np.arctan2(np.imag(hh2),np.real(hh2))), label='N = 2')
    plt.plot(ww, np.unwrap(np.arctan2(np.imag(hh3),np.real(hh3))), label='N = 3')
    plt.plot(ww, np.unwrap(np.arctan2(np.imag(hh4),np.real(hh4))), label='N = 4')    
    plt.title('Fase')
    plt.xlabel('Frequencia normalizada')
    plt.ylabel('Fase [rad]')
    plt.grid()
    
    axes_hdl = plt.gca()
    axes_hdl.legend()

testbench()