# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 16:03:27 2015

@author: alan
"""

from Persona import Persona

class Paseador(Persona):

    def __init__(self,nombre , apellido ,DNI , telefono , direc):
        self.__init__(self,nombre, apellido ,DNI, telefono , direc)
        self.__lista__paseos = []

    def get_lista_paseo(self):
        return self.__lista_paseos

