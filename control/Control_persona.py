# -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 23:02:27 2015

@author: Franco
"""
import random

class Control():
    
    def __init__(self,roll):
        self.lista = []
        self.roll = roll
        
    def get_roll(self):
        return self.roll
    
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