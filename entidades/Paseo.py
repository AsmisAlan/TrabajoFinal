# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 16:03:27 2015

@author: alan
"""


class Paseo():

    def __init__(self,hora_salida = None,hora_llegada = None, tiempo_Tentativo= None ,ID= None, paseador = None):
        self.__hora_salida = hora_salida
        self.__hora_llegada = hora_llegada
        self.__tiempo_tentativo = tiempo_Tentativo
        self.__ID = ID
        self.__paseador = paseador
        
    def set_hora_salida(self , hora):
        self.__hora_salida = hora
    
    def set_hora_llegada(self , hora):
        self.__hora_llegada = hora

    def set_paseador(self,paseador):
        self.__paseador = paseador
        
    def get_paseador(self):
        return self.__paseador
        
    def get_tiempo_tentativo(self):
        return self.__tiempo_tentativo
    
    def get_id(self):
        return self.__ID
        
    def get_hora_salida(self):
        return self.__hora_salida
        
    def get_hora_llegada(self):
        return self.__hora_llegada