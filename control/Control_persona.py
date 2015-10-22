# -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 23:02:27 2015

@author: Franco
"""

class Control():
    
    lista = []

    
    
    def control_agregar(self,nuevo):
        for Persona in self.lista_cliente:
            if (nuevo.get_DNI() == Persona.get_DNI()):
                return True
        else:
            self.lista.append(nuevo)
            return False