# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 16:03:27 2015

@author: alan
"""

from Persona import Persona

class Paseador(Persona):

    def __init__(self,nombre  = None , apellido  = None ,DNI  = None, telefono  = None, direc  = None, lista = []):
        self.__init__(self,nombre, apellido ,DNI, telefono , direc)
        self.__listaMascotas = lista

    def cargar_mascota(self,mascota):
        return self.__listaMascotas.append(mascota)
    
    def get_lista_mascotas(self):
        return self.__listaMascotas
        
    def get_mascota(self , ID):
        for mascota in self.__listaMascotas : 
            if( ID == mascota.getID()):
                return mascota
        return None
        


