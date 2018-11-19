# -*- coding: utf-8 -*-
"""
Created on Sun Nov 18 17:06:53 2018

@author: Francisco
"""

import matplotlib as mpl
import matplotlib.pyplot as plt
import pdsmodulos.generador as gen
import numpy as np
import pdsmodulos.tools as tools
from scipy import signal
from scipy.fftpack import fft
import scipy.io as sio

def vertical_flaten(a):
    
    return a.reshape(a.shape[0],1)

def testbench():
    
    fs = 1000
    # para listar las variables que hay en el archivo
    #io.whosmat('ECG_TP4.mat')
    mat_struct = sio.loadmat('./ECG_TP4.mat')
    
    ecg_one_lead = vertical_flaten(mat_struct['ecg_lead'])
    N = len(ecg_one_lead)
    ecg_one_lead = ecg_one_lead.reshape(N)
    
    df = fs/N
    ff = np.linspace(0, int((N-1)*df), int(N))
    
    x = ecg_one_lead[303600:306000]
    
    plt.plot(x)
    tools.spectrum_analyzer(x, fs, len(x))
    
    
testbench()