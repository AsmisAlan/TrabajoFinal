# -*- coding: utf-8 -*-
"""
Created on Sat Oct 17 20:30:41 2015

@author: Franco
"""
from entidades import Mascota
class Control():
    lista_cliente = []
    


    def control_mascota(mascota, paseador):
        lista = paseador.get_lista_paseo()
        contador = 0
        while (contador < len(lista)):
            if lista[contador].get_id() == mascota.get_id:
                if lista[contador].get_nombre()== mascota.get_nombre:
                    return False

            contador += 1

        return True


    def control_paseo(paseo,paseador):
       if paseo.get_paseador == paseador.get_dni :
           return False

       else:
           return True

    
    def control_cliente(self,nuevo_cliente, lista_cliente):
        for cliente in lista_cliente:
            if (nuevo_cliente.get_DNI() == cliente.get_DNI()):
                return True
        else:
            self.lista_cliente.append(nuevo_cliente)
            return False
            
        
