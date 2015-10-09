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
    
     def GetNombre(self):
         self.__nombre
        
     def GetRaza(self):
         self.__raza
         
     def GetID(self):
         self.__ID
         
     def GetTelefono(self):
         self.__peso
         
         
     def SetNombre(self,nombre):
         self.__nombre = nombre
        
     def SetRaza(self,raza):
         self.__raza = raza
         
     def SetPeso(self,peso):
         self.__peso = peso
         
     def SetID(self , ID):
         self.__ID = ID
