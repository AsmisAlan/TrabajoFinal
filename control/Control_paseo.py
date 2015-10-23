# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 15:01:45 2015

@author: alan
"""

import random

class Control_paseo():
    
    def __init__(self):
        self.lista = []
    
    def agregar(self,nuevo):
        self.lista.append(nuevo)

    def obtener(self, ID):
        return self.lista[ID]
    
    def tamanio(self):
        return len(self.lista) 