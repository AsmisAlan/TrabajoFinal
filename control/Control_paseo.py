# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 15:01:45 2015

@author: alan
"""

import random

class Control():
    
    def __init__(self):
        self.lista = []
    
    def control_agregar(self,nuevo):
        control = True
        for Persona in self.lista:
            if (nuevo.get_DNI() == Persona.get_DNI()):
                control = False
                break
        if (control):
            self.lista.append(nuevo)
        return control
            
    def obtener(self,pos ):
        return self.lista[pos]
        
    def tamanio(self):
        return len(self.lista) 
        
    def ListaNombres(self):
        lista_aux = []
        for Persona in self.lista:
            lista_aux.append(Persona.get_nombre()+' '+ Persona.get_apellido())
        return lista_aux
        
    def obtener_por_dni(self , DNI):
        for Persona in self.lista:
            if (DNI == Persona.get_DNI()):
                return Persona
                
    def obtener_Random(self):
           if( self.tamanio() > 0):
               return random.choice(self.lista)