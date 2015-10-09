# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 15:14:34 2015

@author: alan
"""
class Persona(object):
    
     def __init__(self,nombre , apellido ,DNI , telefono , direc):
         self.__nombre = nombre
         self.__apellido = apellido
         self.__DNI = DNI
         self.__telefono = telefono
         self.__direc = direc
    
     def GetNombre(self):
         self.__nombre
        
     def GetApellido(self):
         self.__apellido
         
     def GetDNI(self):
         self.__DNI
         
     def GetTelefono(self):
         self.__telefono
         
     def GetDirec(self):
         self.__direc
         
     def SetNombre(self,nombre):
         self.__nombre = nombre
        
     def SetApellido(self,apellido):
         self.__apellido = apellido
         
     def SetDNI(self,DNI):
         self.__DNI = DNI
         
     def SetTelefono(self , telefono):
         self.__telefono = telefono
         
     def SetDirec(self , direc):
         self.__direc = direc
         
