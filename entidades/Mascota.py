# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 16:04:49 2015

@author: alan




"""

class Mascota(object):
    
     def __init__(self,nombre , raza , peso , ID):
         self.__nombre = nombre
         self.__raza = raza
         self.__peso = peso
         self.__ID = ID
    
     def get_nombre(self):
         self.__nombre
        
     def get_raza(self):
         self.__raza
         
     def get_id(self):
         self.__ID
         
     def get_peso(self):
         self.__peso
         
         
     def set_nombre(self,nombre):
         self.__nombre = nombre
        
     def SetRaza(self,raza):
         self.__raza = raza
         
     def SetPeso(self,peso):
         self.__peso = peso
         
     def SetID(self , ID):
         self.__ID = ID
