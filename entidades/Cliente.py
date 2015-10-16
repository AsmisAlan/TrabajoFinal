# -*- coding: utf-8 -*-

from Persona import Persona

class Cliente(Persona):
    
    def __init__(self,nombre , apellido ,DNI , telefono , direc):
        self.__init__(self,nombre, apellido ,DNI, telefono , direc)
        self.__listaMascotas=[]

    def cargar_mascota(self,mascota):
        self.__listaMascotas.append(mascota);