# -*- coding: utf-8 -*-
"""
Created on Wed Sep 26 16:17:28 2018

@author: Francisco
"""

import matplotlib as mpl
import matplotlib.pyplot as plt
import pdsmodulos.generador as gen
import numpy as np
import pdsmodulos.tools as tools
from scipy import signal

def barlett(N):
    
    k = np.linspace(0, (N-1), N)
    w = (2/(N-1))*((N-1)/2 - np.abs(k-(N-1)/2))
    return w
        
def hann(N):
    
    k = np.linspace(0, (N-1), N)
    w = 0.5*(1 - np.cos((2*np.pi*k)/(N-1)))
    return w
    
def blackman(N):
    
    k = np.linspace(0, (N-1), N)
    w = 0.42 - 0.5*np.cos((2*np.pi*k)/(N - 1)) + 0.08*np.cos((4*np.pi*k)/(N - 1))
    return w
    
def flat_top(N):
    # Ojo que saque la ecucacion de wikipedia
    k = np.linspace(0, (N-1), N)
    w = 1 - 1.93*np.cos((2*np.pi*k)/(N - 1)) + 1.29*np.cos((4*np.pi*k)/(N - 1)) - 0.388*np.cos((6*np.pi*k)/(N - 1)) + 0.032*np.cos((8*np.pi*k)/(N - 1))
    w = w/np.max(w)
    return w

w = flat_top(41)
plt.stem(w)
 
    
