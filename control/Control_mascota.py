# -*- coding: utf-8 -*-
"""
Created on Sat Oct 17 20:30:41 2015

@author: Franco
"""

class Control_mascota():
    
    def __init__(self):
        self.lista = []
        self.roll = 'MASCOTA'

    def get_roll(self):
        return self.roll
    
    def agregar(self,nuevo):
        self.lista.append(nuevo)

    def obtener(self, ID):
        return self.lista[ID]
    
    def tamanio(self):
        return len(self.lista) 
    
    
                    
        

