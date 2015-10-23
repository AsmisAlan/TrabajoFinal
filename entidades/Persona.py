# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 15:14:34 2015

@author: alan
"""
class Persona():
    
     def __init__(self,nombre = None, apellido = None ,DNI = None , telefono  = None, direc = None ):
         self.__nombre = nombre
         self.__apellido = apellido
         self.__DNI = DNI
         self.__telefono = telefono
         self.__direc = direc
    
     def get_nombre(self):
         return self.__nombre
        
     def get_apellido(self):
         return self.__apellido
         
     def get_DNI(self):
         return self.__DNI
         
     def get_telefono(self):
         return self.__telefono
         
     def get_direc(self):
         return self.__direc
         
     def get_apellido_nombre(self):
         return self.__apellido +' '+ self.__nombre
         
     def set_nombre(self,nombre):
         self.__nombre = nombre
        
     def set_apellido(self,apellido):
         self.__apellido = apellido
         
     def set_DNI(self,DNI):
         self.__DNI = DNI
         
     def set_telefono(self , telefono):
         self.__telefono = telefono
         
     def set_direc(self , direc):
         self.__direc = direc
         
