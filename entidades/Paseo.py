# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 16:03:27 2015

@author: alan
"""

class Paseo():

    def __init__(self,tiempo , tiempoTentativo , DNI):
        self.__tiempo = tiempo
        self.__tiempoTentativo = tiempoTentativo
        self.listaMascota = []
        self.__ID = DNI

    def cargar_mascota(self,mascota):
        self.__listaMascotas.append(mascota);


    def get_paseador(self):
        return self.__ID