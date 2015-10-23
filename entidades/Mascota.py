# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 16:04:49 2015

@author: alan




"""

class Mascota():
    
     def __init__(self,nombre = None , raza = None, peso= None , ID = None, dueño = None, paseador= None):
         self.__nombre = nombre
         self.__raza = raza
         self.__peso = peso
         self.__ID = ID #este id se genra automaticamente
         self.__dueño = dueño # codigo por el cual se va a vincular con su dueño
         self.__paseador = paseador #codigo por el cual se va a vincular con su paseador
    
     def get_nombre(self):
         return self.__nombre
        
     def get_raza(self):
         return self.__raza
         
     def get_ID(self):
         return self.__ID
         
     def get_peso(self):
         return self.__peso
         
     def get_dueño(self):
         return self.__dueño
         
     def get_paseador(self):
         return self.__paseador
        
     def set_nombre(self,nombre):
         self.__nombre = nombre
        
     def set_raza(self,raza):
         self.__raza = raza
         
     def set_peso(self,peso):
         self.__peso = peso
         
     def set_ID(self , ID):
         self.__ID = ID
        
     def set_dueño(self,dueño):
          self.__dueño = dueño
         
     def set_paseador(self,paseador):
          self.__paseador = paseador
