# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 22:35:52 2015

@author: Franco
"""

from PyQt4 import QtGui, uic ,QtCore
from interfas.Submenu_alta_baja_mascota import Submenu_alta_baja_mascota
from interfas.ManejoTablas import *
from interfas.Mapa import Mapa
from interfas.Detalle_mascota import Detalle_mascota

Menu_ge = uic.loadUiType("interfas/Menu_gestion.ui")[0]

class Menu_gestion_mascota(QtGui.QWidget,Menu_ge):

    def __init__(self,lista_clientes,lista_paseadores,lista_mascotas , parent=None ):
         QtGui.QWidget.__init__(self, parent)
         self.setupUi(self)
         
         self.boton_detalles.clicked.connect(self.detalles)
         self.boton_mapa.clicked.connect(self.direccion)
         self.boton_nuevo.clicked.connect(self.nueva_mascota)
         self.tabla_mascota.doubleClicked.connect(self.modificar)
         self.tabla_persona.close()
          
         #La variable por referencia Self.lista_clientes va a apuntar al mismo objeto que la lista_clientes.
         self.lista_clientes = lista_clientes 
         #La variable por referencia Self.lista_paseadores va a apuntar al mismo objeto que la lista_paseadores.
         self.lista_paseadores = lista_paseadores
         #La variable por referencia Self.lista_mascotas va a apuntar al mismo objeto que la lista_mascotas.
         self.lista_mascotas = lista_mascotas
         self.titulo_submenu.setText('GESTION MASCOTAS' )
         CargarTablaMascota(self.tabla_mascota ,self.lista_mascotas.lista)
             
    

    def nueva_mascota(self):
        #debe haber por lo menos un paseador y un cliente para asignar la mascota.
        if(self.lista_clientes.tamanio() > 0) and (self.lista_paseadores.tamanio() >0):
            self.nueva_mascota = Submenu_alta_baja_mascota(self.lista_mascotas,self.lista_clientes,self.lista_paseadores.obtener_Random(),self.tabla_mascota)
            self.nueva_mascota.setVisible(True)
        else:
            self.error = Error_alta_baja()
            self.error.setVisible(True)
            self.error.mensaje_error.setText('Debes tener al menos 1 cliente/paseador.')
            self.error.titulo.setText('Error')
            
    
    def modificar(self):
        pos = self.tabla_mascota.currentRow()
        self.nuevo = Submenu_alta_baja_mascota( self.lista_mascotas,self.lista_clientes,self.lista_paseadores,self.tabla_mascota,self.lista_mascotas.lista[pos] )
        self.nuevo.setVisible(True)

    
    def detalles(self):
        pos = self.tabla_mascota.currentRow()
        if (pos != None):
            mascota = self.lista_mascotas.lista[pos]
            cliente = self.lista_clientes.obtener_por_dni(mascota.get_dueño())
            paseador = self.lista_paseadores.obtener_por_dni(mascota.get_paseador())
            self.nuevo = Detalle_mascota(mascota,cliente,paseador)
            self.nuevo.setVisible(True)
    
    def direccion(self):
        print('mapa')
        