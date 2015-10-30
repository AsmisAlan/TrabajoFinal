# -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 04:35:48 2015

@author: alan
"""
import random
from PyQt4 import QtGui, uic, QtCore
from interfas.Error_alta_baja import Error_alta_baja
from interfas.ManejoTablas import *
from interfas.Mapa import Mapa
from entidades.Mascota import Mascota

dialogo_alta_baja_mascota= uic.loadUiType('interfas/alta_baja_mascota.ui')[0]


class Submenu_alta_baja_mascota(QtGui.QWidget, dialogo_alta_baja_mascota):
    
    def __init__ (self,lista_mascotas,lista_clientes,paseador,tabla,mascota = None,parent = None):
        QtGui.QWidget.__init__(self, parent)
        self.setupUi(self)
        self.barra_peso.valueChanged.connect(self.manejo_peso)
        self.boton_guardar.clicked.connect(self.guardar)
        
        self.lista_mascotas = lista_mascotas
        self.lista_clientes = lista_clientes
        self.chico.show()
        self.mediano.close()
        self.grande.close() 
        self.box_cliente.addItems(self.lista_clientes.ListaNombres())
        self.tabla = tabla
        if(mascota != None):
            self.linea_raza.setText(mascota.get_raza())
            self.barra_peso.setValue(mascota.get_peso())
            self.id = mascota.get_ID()
            self.linea_id.setText(str (self.id))
            self.manejo_peso()
            self.linea_nombre.setText(mascota.get_nombre())
            self.box_paseador.addItems(paseador.ListaNombres())
            self.paseador_asignado = paseador.obtener(self.box_cliente.currentIndex()).get_DNI()
        else:
            self.id = lista_mascotas.tamanio()
            self.linea_id.setText(str (self.id))
            self.paseador_asignado = paseador.get_DNI()
            self.box_paseador.addItem(paseador.get_apellido_nombre())
            
        
        
    def manejo_peso(self):
        if (self.Peso.intValue() < 20):
            self.chico.show()
            self.mediano.close()
            self.grande.close()
        elif(self.Peso.intValue() < 50):
            self.chico.close()
            self.mediano.show()
            self.grande.close()
        else:
            self.chico.close()
            self.mediano.close()
            self.grande.show()
            
            
    def guardar(self):
        error = ''
        ID = self.id
        paseador = self.paseador_asignado
        dueño = self.lista_clientes.obtener(self.box_cliente.currentIndex()).get_DNI()
        nombre = self.linea_nombre.text()
        if (nombre == ''):
            error += ' nombre'
        raza = self.linea_raza.text()
        if (raza == ''):
            error += ' raza'
        peso = self.Peso.intValue()
        if(error !=''):
            self.mostra_error(error)
        else:
            self.guardar_como(Mascota(nombre , raza , peso ,ID,dueño ,paseador))
        
    def guardar_como(self,mascota):
        if self.id == self.lista_mascotas.tamanio() :            
            self.lista_mascotas.agregar(mascota)
            add_in_tabla_mascota(self.tabla,self.lista_mascotas)
            self.close()
        else:
            self.lista_mascotas.lista[self.id] = mascota
            setChangeTablaMascota(self.tabla , self.lista_mascotas,self.id,self.tabla.currentRow())
            self.close()

        
     
    def mostra_error(self,detalles):
        self.error = Error_alta_baja()
        self.error.setVisible(True)
        self.error.mensaje_error.setText('Error en el campo: ' + detalles)
        
        
        

        
        
            