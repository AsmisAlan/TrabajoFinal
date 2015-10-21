# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 16:03:27 2015

@author: alan
"""

from Persona import Persona

class Paseador(Persona):

    def __init__(self,nombre , apellido ,DNI , telefono , direc , lista = []):
        self.__init__(self,nombre, apellido ,DNI, telefono , direc)
        self.__listaMascotas = lista

    def cargar_mascota(self,mascota):
        return self.__listaMascotas.append(mascota)
        


