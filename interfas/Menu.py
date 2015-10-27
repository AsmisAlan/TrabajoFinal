# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 23:00:37 2015

@author: alan
"""

import sys
from PyQt4 import QtGui, uic 
from entidades.Persona import Persona
from entidades.Mascota import Mascota
from entidades.Paseo import Paseo
from control.Control_mascota import Control_mascota
from control.Control_persona import Control
from control.Control_paseo import Control_paseo
from interfas.Error_alta_baja import Error_alta_baja
from interfas.Detalles_persona import Detalles_persona
from interfas.ManejoTablas import *
from interfas.Mapa import Mapa
import time




#==============================================================================
#                             MENU PRINCIPAL
#==============================================================================

Menu = uic.loadUiType("interfas/Menu.ui")[0]
class Menu(QtGui.QMainWindow,Menu):
    
    def __init__(self, parent=None):
         QtGui.QMainWindow.__init__(self, parent)
         self.setupUi(self)
         
         self.lista_mascotas = Control_mascota()
         self.lista_clientes = Control('CLIENTE')
         self.lista_paseadores = Control('PASEADOR') 
         self.lista_paseos = Control_paseo()

         self.boton_cliente.clicked.connect(self.gestionCliente)
         self.boton_mascota.clicked.connect(self.gestionMascota)
         self.boton_paseador.clicked.connect(self.gestionPaseador)
         self.boton_nuevo_paseo.clicked.connect(self.gestionPaseo)
         self.llegada.clicked.connect(self.marcarLlegada)
         self.boton_mapa.clicked.connect(self.verRecorrido)
         self.tabla_paseos.clicked.connect(self.activar)
         
    
    def gestionCliente(self):
        self.menu_cliente = Menu_gestion(self.lista_clientes,self.lista_mascotas)
        self.menu_cliente.setVisible(True)
        
    def gestionMascota(self):
        self.menu_mascota = Menu_gestion_mascota(self.lista_clientes,self.lista_paseadores,self.lista_mascotas)
        self.menu_mascota.setVisible(True)
    
    def gestionPaseador(self):
        self.menu_paseador = Menu_gestion(self.lista_paseadores,self.lista_mascotas)
        self.menu_paseador.setVisible(True)
    
    def gestionPaseo(self):
        if(self.lista_paseadores.tamanio() > 0):
            self.menu_nuevo_paseo = Submenu_alta_baja_paseo(self.lista_paseos,self.lista_paseadores,self.tabla_paseos,self.lista_paseadores.cantidad_mascotas(self.lista_mascotas))
            self.menu_nuevo_paseo.setVisible(True)
        else:
            self.mostra_error('No hay Paseadores.')
        
    def marcarLlegada(self):
        self.lista_paseos.obtener(self.tabla_paseos.currentRow()).set_hora_llegada(time.strftime('%H : %M : %S'))
        CargarTablaPaseo(self.tabla_paseos , self.lista_paseos)
        self.llegada.setEnabled(False)
        self.boton_mapa.setEnabled(True)
    
    def verRecorrido(self):
        paseador = self.lista_paseos.obtener(self.tabla_paseos.currentRow()).get_paseador()  
        direcciones = self.lista_clientes.direcciones(self.lista_mascotas.mascotas(paseador))
        print(direcciones)        
        self.mapa_recorrido = Mapa(direcciones)
        self.mapa_recorrido.setVisible(True)
        
    def activar(self):
        if(self.lista_paseos.obtener(self.tabla_paseos.currentRow()).get_hora_llegada().find('-') > -1):
            self.llegada.setEnabled(True)
        else:
            self.llegada.setEnabled(False)
        self.boton_mapa.setEnabled(True)
        
    def mostra_error(self,detalles):
        self.error = Error_alta_baja()
        self.error.setVisible(True)
        self.error.mensaje_error.setText( detalles)
            
        
        

        
        
        
#==============================================================================
#              MENU DE GESTION (paseadores , clientes)
#==============================================================================
        
Menu_ge = uic.loadUiType("interfas/Menu_gestion.ui")[0]

class Menu_gestion(QtGui.QWidget,Menu_ge):

    def __init__(self,lista,mascotas, parent=None ):
         QtGui.QWidget.__init__(self, parent)
         self.setupUi(self)
         
         self.tabla_mascota.close()
         self.texto_menu = lista.get_roll() #guardo el roll que poseen los objetos de la lista.
         self.lista = lista #La variable por referencia Self.lista va a apuntar al mismo objeto que la lista.
         self.lista_mascotas = mascotas
         self.titulo_submenu.setText('GESTION ' + self.texto_menu )  
         CargarTabla(self.tabla_persona ,self.lista)
         
         self.boton_detalles.clicked.connect(self.detalles)
         self.boton_mapa.clicked.connect(self.direccion)
         self.boton_nuevo.clicked.connect(self.nuevo)
         self.tabla_persona.doubleClicked.connect(self.modificar)
    
    def modificar(self):
        pos = self.tabla_persona.item(self.tabla_persona.currentRow(),0) #devuelve el documento de la tabla
        if (pos != None ):
            doc = int (QtGui.QTableWidgetItem.text(pos) ) # combierte el documento qtable gidget en entero
            self.nuevo = Submenu_alta_baja( self.lista,self.tabla_persona,self.lista.obtener_pos_dni(doc) )
            self.nuevo.setVisible(True)

    def nuevo(self):
        #esto pide, la lista , una tabla y la persona si se quiere modificar.
        self.nuevo = Submenu_alta_baja( self.lista,self.tabla_persona ) 
        self.nuevo.setVisible(True)
    
    def detalles(self):
        pos = self.tabla_persona.item(self.tabla_persona.currentRow(),0)
        if (pos != None ):
            doc = int (QtGui.QTableWidgetItem.text(pos) )
            self.detallar = Detalles_persona(self.lista.obtener_por_dni(doc),self.lista.get_roll(),self.lista_mascotas)
            self.detallar.setVisible(True)
    
    def direccion(self):
        pos = self.tabla_persona.item(self.tabla_persona.currentRow(),4)
        if (pos != None ):
            direccion = str (QtGui.QTableWidgetItem.text(pos) )
            self.mapa_persona = Mapa(direccion)
            self.mapa_persona.setVisible(True)
            
        
#==============================================================================
#                        MENU DE GESTION (mascotas )
#==============================================================================
        
        
Menu_ge = uic.loadUiType("interfas/Menu_gestion.ui")[0]

class Menu_gestion_mascota(QtGui.QWidget,Menu_ge):

    def __init__(self,lista_clientes,lista_paseadores,lista_mascotas , parent=None ):
         QtGui.QWidget.__init__(self, parent)
         self.setupUi(self)
         
         self.boton_detalles.clicked.connect(self.detalles)
         self.boton_mapa.clicked.connect(self.direccion)
         self.boton_nuevo.clicked.connect(self.nueva_mascota)
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

    
    def detalles(self):
        print('detalles')
    
    def direccion(self):
        print('mapa')
        
        
        
#==============================================================================
#                          NUEVO - MODIFICAR (CLIENTE / PASEADOR)
#==============================================================================
        

dialogo_alta_baja = uic.loadUiType('interfas/alta_baja.ui')[0]

class Submenu_alta_baja(QtGui.QWidget, dialogo_alta_baja):
    
    def __init__ (self,lista,tabla,pos= None, parent = None):
        QtGui.QWidget.__init__(self, parent)
        self.setupUi(self)
        self.pos = pos
        self.lista  = lista
        self.tabla = tabla
       
        if(pos != None):
            persona = self.lista.lista[self.pos]
            self.linea_nombre.setText(persona.get_nombre())
            self.linea_apellido.setText(persona.get_apellido())
            self.linea_dni.setText(str(persona.get_DNI()))
            self.linea_telefono.setText(str(persona.get_telefono()))
            self.linea_direccion.setText(persona.get_direc())
            self.text.setText('MODIFICAR '+ lista.get_roll())
        else:
            self.text.setText('NUEVO '+ lista.get_roll() )
        
        self.boton_guardar.clicked.connect(self.guardar)
            
        
    def guardar(self):
        error = ''
        dni  = 0
        telefono = 0
        nombre = self.linea_nombre.text()
        if (nombre == ''):
            error += 'nombre' 
        apellido = self.linea_apellido.text()
        if (apellido == ''):
            error += ', apellido' 
        try:
            dni = int(self.linea_dni.text())
        except(ValueError):
            error += ', dni' 
        try:
            telefono = int(self.linea_telefono.text())
        except(ValueError):
            error += ', telefono'
        direccion = self.linea_direccion.text() + 'Concepcion del Uruguay'
        if (direccion == ''):
            error += ', direccion'
            
        if (error != ''): #verifica que los campos sean correctos
            self.mostra_error(error)
        else:
            self.guardar_como(Persona(nombre,apellido,dni,telefono,direccion))            
            
            
    def guardar_como(self,persona):
        if self.pos == None :            
            if(self.lista.control_agregar(persona)):
                add_in_tabla(self.tabla,self.lista)
                self.close()
            else:
                self.mostra_error('El '+self.lista.get_roll()+' con el documento' +str(persona.get_DNI())+ ' ya existe.')
        else:
            if self.lista.obtener_por_dni(persona.get_DNI()) == None :
                self.lista.lista[self.pos] = persona
                setChangeTabla(self.tabla , self.lista,self.pos,self.tabla.currentRow())
                self.close()
            else:
                self.mostra_error('El '+self.lista.get_roll()+' con el documento' +str(persona.get_DNI())+ ' ya existe.')
        
        
    def mostra_error(self,detalles):
        self.error = Error_alta_baja()
        self.error.setVisible(True)
        self.error.mensaje_error.setText('Error en el campo: ' + detalles)
        
        
#==============================================================================
#                          NUEVO - MODIFICAR (MASCOTA)
#==============================================================================
        
        
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
            self.linea_nombre().setText(mascota.get_nombre())
            self.box_paseador.addItem(str(mascota.get_paseador() ))
            self.paseador_asignado=mascota.get_paseador() 
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
            self.lista_mascotas.agregar( Mascota(nombre , raza , peso ,ID,dueño ,paseador))
            add_in_tabla_mascota(self.tabla , self.lista_mascotas )
            self.close()
        
    def mostra_error(self,detalles):
        self.error = Error_alta_baja()
        self.error.setVisible(True)
        self.error.mensaje_error.setText('Error en el campo: ' + detalles)
        
        
        
#==============================================================================
#                          NUEVO - MODIFICAR (PASEO)
#==============================================================================
        
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
        
        
        
#==============================================================================
#                            BLOQUE DE EJECUCION
#==============================================================================
        
app = QtGui.QApplication(sys.argv)
menu = Menu(None)
menu.show()
app.exec_()