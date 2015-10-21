# -*- coding: utf-8 -*-

import Persona 

class Cliente(Persona):
    
    def __init__(self,nombre = None , apellido = None ,DNI = None , telefono = None , direc = None, lista = []):
        self.__init__(self,nombre, apellido ,DNI, telefono , direc)
        self.__listaMascotas=lista

    def cargar_mascota(self,mascota):
        self.__listaMascotas.append(mascota);
        
    def Get_Mascota(self , mascota_id):
        pos = -1
        for mascota in self.__listaMascotas:
            pos +=1
            if(mascota.get_ID() == mascota_id):
                return pos
        return -1