# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 11:11:08 2018

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
from scipy.interpolate import CubicSpline

#%% Variables de ECG_TP4.mat

# ecg_lead: Registro de ECG muestreado a fs=1 KHz durante una prueba de esfuerzo
# qrs_pattern1: Complejo de ondas QRS normal
# heartbeat_pattern1: Latido normal
# heartbeat_pattern2: Latido de origen ventricular
# qrs_detections: vector con las localizaciones (en # de muestras) donde ocurren los latidos
#%%

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
    
    qrs_pattern1 = vertical_flaten(mat_struct['qrs_pattern1'])
    heartbeat_pattern1 = vertical_flaten(mat_struct['heartbeat_pattern1'])
    heartbeat_pattern2 = vertical_flaten(mat_struct['heartbeat_pattern2'])
    qrs_detections = vertical_flaten(mat_struct['qrs_detections'])
    nivel_isoelectrico = qrs_detections - 68
    nivel_isoelectrico = nivel_isoelectrico.reshape(len(nivel_isoelectrico))
    
    df = fs/N
    ff = np.linspace(0, int((N-1)*df), int(N))
    
    zonas_con_interf_baja_frec = ( 
        np.array([12, 12.4]) *60*fs, # minutos a muestras
        np.array([15, 15.2]) *60*fs, # minutos a muestras
        )


    zonas_sin_interf = ( 
            np.array([5, 5.2]) *60*fs, # minutos a muestras
            [4000, 5500], # muestras
            [10e3, 11e3], # muestras
            )
    
    plt.figure()
#    plt.plot(ecg_one_lead, '-gD', markevery = nivel_isoelectrico.all())
    plt.plot(ecg_one_lead)
    plt.plot(nivel_isoelectrico, ecg_one_lead[nivel_isoelectrico], 'rx', markersize = 20, markeredgewidth = 4)
    plt.vlines(qrs_detections, ymin = -33000, ymax = 33000, color = 'r', linestyles = 'dashed')
    
    b = CubicSpline(nivel_isoelectrico, ecg_one_lead[nivel_isoelectrico])
    b = b(range(N))
    plt.figure()
    plt.plot(b)
    
    x = ecg_one_lead - b
    
#    plt.figure()
#    plt.plot(qrs_pattern1)
#    plt.figure()
#    plt.plot(heartbeat_pattern1)
#    plt.figure()
#    plt.plot(heartbeat_pattern2)
#    plt.figure()
#    plt.plot(qrs_detections)
    
    
    
    for ii in zonas_con_interf_baja_frec:
    
        # intervalo limitado de 0 a cant_muestras
        zoom_region = np.arange(np.max([0, ii[0]]), np.min([N, ii[1]]), dtype='uint')
        
        plt.figure()
        plt.plot(zoom_region, ecg_one_lead[zoom_region], label='ECG', lw=2)
        plt.plot(zoom_region, x[zoom_region], label = 'ECG Filtrado')
#        plt.plot(zoom_region, ECG_f_win[zoom_region], label='Win')
#        plt.plot(zoom_region, ECG_f_butt[zoom_region], label='Butter')
        
        plt.title('ECG filtrado en zona con interferencia de ' + str(ii[0]) + ' a ' + str(ii[1]) )
        plt.ylabel('Adimensional')
        plt.xlabel('Muestras (#)')
        plt.grid()
        
        axes_hdl = plt.gca()
        axes_hdl.legend()
        axes_hdl.set_yticks(())
        
    for ii in zonas_sin_interf:
    
        # intervalo limitado de 0 a cant_muestras
        zoom_region = np.arange(np.max([0, ii[0]]), np.min([N, ii[1]]), dtype='uint')
        
        plt.figure()
        plt.plot(zoom_region, ecg_one_lead[zoom_region], label='ECG', lw=2)
        plt.plot(zoom_region, x[zoom_region], label = 'ECG Filtrado')
#        plt.plot(zoom_region, ECG_f_win[zoom_region], label='Win')
#        plt.plot(zoom_region, ECG_f_butt[zoom_region], label='Butter')
        
        plt.title('ECG filtrado en zona sin interferencia de ' + str(ii[0]) + ' a ' + str(ii[1]) )
        plt.ylabel('Adimensional')
        plt.xlabel('Muestras (#)')
        plt.grid()
        
        axes_hdl = plt.gca()
        axes_hdl.legend()
        axes_hdl.set_yticks(())

testbench()