# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 16:03:27 2015

@author: alan
"""
import datetime

class Paseo():

    def __init__(self,hora_salida = None, tiempo_Tentativo= None ,ID= None, paseador = None):
        self.__hora_salida = hora_salida
        self.__tiempo_tentativo = tiempo_Tentativo
        self.__ID = ID
        self.__paseador = paseador
        
    def set_hora_salida(self , hora):
        self.__hora_salida = hora
        
    def set_string_to_Hora_salida(self, string):
        aux = datetime.datetime()
        aux.day()
        aux.month()
        aux.day()
        aux.hour()
        aux.minute()
        aux.second()
        self.__hora_salida = aux
    
    def get_hora_salida_String(self):
        self.__hora_salida

    def set_paseador(self,paseador):
        self.__paseador = paseador
        
    def get_paseador(self):
        return self.__paseador
    
    def get_lista_mascotas(self):
        return self.__paseador.get_lista_mascotas()
        
    def get_mascota(self,idmascota):
        return self.__paseador.get_mascota(idmascota)