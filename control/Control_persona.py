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
        
    def obtener_pos_dni(self,dni):
        pos = 0 
        for Persona in self.lista:
            if (dni == Persona.get_DNI()):
                return pos
            pos+=1
        
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
        return None
                
    def obtener_Random(self):
           if( self.tamanio() > 0):
               return random.choice(self.lista)
               
    def cantidad_mascotas(self,lista_mascota): #puede mejorarce capas :P
        paseadores_aptos = []
        control = 0
        for paseador in self.lista : 
            paseadores_aptos.append(0)
            for mascota in lista_mascota.lista:
                if(mascota.get_paseador() == paseador.get_DNI()):
                    paseadores_aptos[control] +=1
            control +=1
        return paseadores_aptos
        
    def direcciones(self,lista_mascota):
        direcciones = ''
        lista_aux = []
        for mascota in lista_mascota : 
            cliente = self.obtener_por_dni(mascota.get_dueño())
            try:
                lista_aux.index(cliente)
            except:
                lista_aux.append(cliente)
                direcciones += cliente.get_direc() +' |'
        return direcciones
                
                    