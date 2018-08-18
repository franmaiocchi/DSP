# -*- coding: utf-8 -*-
"""
Created on Sat Aug 18 10:36:27 2018

@author: Francisco
"""

# Importacion de modulos
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

def pruebas():
    
    sig_type = { 'tipo': 'senoidal', 
                  'frecuencia': (3, 10, 20), # Uso de tuplas para las frecuencias 
                  'amplitud':   (1, 1,  1),
                  'fase':       (0, 0,  0)
                 } 
    # Como también puedo agregar un campo descripción de manera programática
    # este tipo de sintaxis es *MUY* de Python
    sig_type['descripcion'] = [ str(a_freq) + ' Hz' for a_freq in sig_type['frecuencia'] ]

    # Datos generales de la simulación
    fs = 1000.0 # frecuencia de muestreo (Hz)
    N = 10    # cantidad de muestras
    
    ts = 1/fs   # tiempo de muestreo
    
    # grilla de sampleo temporal
    tt = np.linspace(0, (N-1)*ts, N)
    print(tt)
    
    # Concatenación de matrices:
    # Creamos una matriz vacia con np.array. Luego, con reshape hacemos que sea una matriz vacia de N filas y 1 columna
    # Guardaremos las señales creadas al ir poblando la siguiente matriz vacía
    
    x = np.array([], dtype=np.float)
    print(x)
    x = x.reshape(N,0)
    print(x)

    for this_amp, this_freq, this_phase in zip(sig_type['amplitud'], sig_type['frecuencia'], sig_type['fase']):
        # prestar atención que las tuplas dentro de los diccionarios también pueden direccionarse mediante "ii"
        aux = this_amp * np.sin( 2*np.pi*this_freq*tt + this_phase )
        print(aux)
        aux = aux.reshape(N,1)
        print(aux)
        # para concatenar horizontalmente es necesario cuidar que tengan iguales FILAS
        x = np.hstack([x, aux])
        print(x)

pruebas()
        
    