# -*- coding: utf-8 -*-
"""
Created on Sat Oct 17 20:30:41 2015

@author: Franco
"""

class Control():



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



