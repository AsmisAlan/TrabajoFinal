# -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 15:30:06 2015

@author: alan
"""


from PyQt4 import QtGui, uic
import time

dialogo_alta_baja_paseo= uic.loadUiType('interfas/alta_baja_paseo.ui')[0]

class Submenu_alta_baja_paseo(QtGui.QWidget, dialogo_alta_baja_paseo):
    
    def __init__ (self,lista_paseos ,lista_paseadores , tabla , numero_mascotas ,parent = None):
        QtGui.QWidget.__init__(self, parent)
        self.setupUi(self)
        self.boton_guardar.clicked.connect(self.guardar)
        self.box_paseador.currentIndexChanged.connect(self.numeroMascotas)
        self.tabla = tabla
        self.lista_paseos = lista_paseos
        self.lista_paseadores = lista_paseadores
        self.lista_numero_mascotas = numero_mascotas
        self.paseo.setText(str(lista_paseos.tamanio() ))
        self.box_paseador.addItems(lista_paseadores.ListaNombres())
    
    def numeroMascotas(self):
        pos = self.box_paseador.currentIndex()
        self.mascota.setText(str(self.lista_numero_mascotas[pos]))
        
    def guardar(self):
        error = ''
        ID = self.lista_paseos.tamanio()
        pos = self.box_paseador.currentIndex()
        paseador = self.lista_paseadores.obtener(pos)
        numeroMascotas = self.lista_numero_mascotas[pos]
        if (numeroMascotas == 0):
            error = 'El paseador no posee mascotas a cargo'
        try:
            tiempo_estimado = int(self.tiempo_estimado.text())
        except(ValueError):
            error += 'EL TIEMPO ESTIMADO DEBE SER UN VALOR NUMERICO.'
        tiempo_salida = time.strftime('%H : %M : %S')
        tiempo_llegada = '----------'
        if(error == ''):
            self.lista_paseos.agregar(Paseo(tiempo_salida,tiempo_llegada, tiempo_estimado,ID,paseador))
            add_in_tabla_paseo(self.tabla,self.lista_paseos)
            self.close()
        else:
            self.mostra_error(error)

    def mostra_error(self,detalles):
        self.error = Error_alta_baja()
        self.error.setVisible(True)
        self.error.mensaje_error.setText(detalles)