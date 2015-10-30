# -*- coding: utf-8 -*-
"""
Created on Sat Oct 17 20:30:41 2015

@author: Franco
"""

class Control_mascota():
    
    def __init__(self):
        self.lista = []
        self.roll = 'MASCOTA'

    def get_roll(self):
        return self.roll
    
    def agregar(self,nuevo):
        self.lista.append(nuevo)

    def obtener(self, ID):
        return self.lista[ID]
    
    def tamanio(self):
        return len(self.lista) 
    
    def mascotas(self,paseador):
        lista_aux = []
        for mascota in self.lista : 
            if( mascota.get_paseador() == paseador.get_DNI() ):    
                lista_aux.append(mascota)
        return lista_aux
    
    def mascotas_cliente(self,cliente):
        lista_aux = []
        for mascota in self.lista : 
            if( mascota.get_dueño() == cliente.get_DNI() ):    
                lista_aux.append(mascota)
        return lista_aux
    
    def modificar_paseador(self,dni_viejo,dni_nuevo):
        for mascota in self.lista : 
            if( mascota.get_paseador() == dni_viejo):    
                mascota.set_paseador(dni_nuevo)
                    
    def modificar_dueño(self,dni_viejo,dni_nuevo):
        for mascota in self.lista : 
            if( mascota.get_dueño() == dni_viejo):    
                mascota.set_dueño(dni_nuevo)

        

