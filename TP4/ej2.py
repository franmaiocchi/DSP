# -*- coding: utf-8 -*-
"""
Created on Fri Nov 16 20:30:21 2018

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
    
    ww, hh = sig.freqz(np.array([-1, 1]), 1)
    ww = ww / np.pi
    
    plt.figure()
    
    plt.subplot(2,1,1)
    plt.plot(ww, 20 * np.log10(abs(hh) + np.finfo(float).eps), label='$h(k) = (-1,1)$')
    plt.title('Módulo')
    plt.xlabel('Frequencia normalizada')
    plt.ylabel('Módulo [dB]')
    plt.ylim((-80, 10))
    plt.grid()
    
    axes_hdl = plt.gca()
    axes_hdl.legend()
    
    plt.subplot(2,1,2)
    plt.plot(ww, np.unwrap(np.arctan2(np.imag(hh),np.real(hh))), label='$h(k) = (-1,1)$')   
    plt.title('Fase')
    plt.xlabel('Frequencia normalizada')
    plt.ylabel('Fase [rad]')
    plt.grid()
    
    axes_hdl = plt.gca()
    axes_hdl.legend()
    
testbench()