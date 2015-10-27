# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 17:38:43 2015

@author: alan
"""


from PyQt4 import QtGui

def add_in_tabla(tabla,lista):
    aux = lista.tamanio() -1
    tabla.insertRow(aux)
    nombre = QtGui.QTableWidgetItem(lista.obtener(aux).get_nombre() )
    apellido =QtGui.QTableWidgetItem( lista.obtener(aux).get_apellido() )
    dni = QtGui.QTableWidgetItem( str(lista.obtener(aux).get_DNI()) )
    tel = QtGui.QTableWidgetItem( str(lista.obtener(aux).get_telefono() ))
    direc = QtGui.QTableWidgetItem( lista.obtener(aux).get_direc() )
    tabla.setItem(aux ,0 , dni)
    tabla.setItem(aux ,1 , nombre )
    tabla.setItem(aux ,2, apellido)
    tabla.setItem(aux ,3 ,tel )
    tabla.setItem(aux ,4,direc )

def add_in_tabla_mascota(tabla,lista):
    aux = lista.tamanio() -1
    tabla.insertRow(aux)
    nombre = QtGui.QTableWidgetItem(lista.obtener(aux).get_nombre() )
    peso =QtGui.QTableWidgetItem( str(lista.obtener(aux).get_peso()) )
    raza = QtGui.QTableWidgetItem( lista.obtener(aux).get_raza() )
    dueño = QtGui.QTableWidgetItem( str(lista.obtener(aux).get_dueño() ))
    paseador = QtGui.QTableWidgetItem( str(lista.obtener(aux).get_paseador()) )
    tabla.setItem(aux ,0 , nombre)
    tabla.setItem(aux ,1 ,raza)
    tabla.setItem(aux ,2, peso)
    tabla.setItem(aux ,3 ,dueño )
    tabla.setItem(aux ,4,paseador)
    
def CargarTabla(tabla,lista):
        fila = 0
        for aux in lista.lista:
            tabla.insertRow(fila)
            nombre = QtGui.QTableWidgetItem( aux.get_nombre() )
            apellido =QtGui.QTableWidgetItem( aux.get_apellido() )
            dni = QtGui.QTableWidgetItem( str(aux.get_DNI()) )
            tel = QtGui.QTableWidgetItem( str(aux.get_telefono() ))
            direc = QtGui.QTableWidgetItem( aux.get_direc() )
            tabla.setItem(fila ,0 , dni)
            tabla.setItem(fila ,1 , nombre )
            tabla.setItem(fila ,2, apellido)
            tabla.setItem(fila ,3 ,tel )
            tabla.setItem(fila ,4,direc )
            fila+=1
            
def CargarTablaMascota(tabla_mascota,lista):
        fila = 0
        for aux in lista:
            tabla_mascota.insertRow(fila)
            nombre = QtGui.QTableWidgetItem(aux.get_nombre() )
            peso =QtGui.QTableWidgetItem( str(aux.get_peso()) )
            raza = QtGui.QTableWidgetItem( aux.get_raza() )
            dueño = QtGui.QTableWidgetItem(str( aux.get_dueño() ))
            paseador = QtGui.QTableWidgetItem( str(aux.get_paseador()) )
            tabla_mascota.setItem(fila ,0 , nombre)
            tabla_mascota.setItem(fila ,1 ,raza)
            tabla_mascota.setItem(fila ,2, peso)
            tabla_mascota.setItem(fila ,3 ,dueño )
            tabla_mascota.setItem(fila ,4,paseador)
            fila+=1
            
            
def setChangeTabla(tabla,lista,aux,pos):
    nombre = QtGui.QTableWidgetItem(lista.obtener(aux).get_nombre() )
    apellido =QtGui.QTableWidgetItem( lista.obtener(aux).get_apellido() )
    dni = QtGui.QTableWidgetItem( str(lista.obtener(aux).get_DNI()) )
    tel = QtGui.QTableWidgetItem( str(lista.obtener(aux).get_telefono() ))
    direc = QtGui.QTableWidgetItem( lista.obtener(aux).get_direc() )
    tabla.setItem(pos ,0 , dni)
    tabla.setItem(pos ,1 , nombre )
    tabla.setItem(pos ,2, apellido)
    tabla.setItem(pos ,3 ,tel )
    tabla.setItem(pos ,4,direc )
            
def setChangeTablaMascota(tabla_mascota,lista,aux,pos):
    nombre = QtGui.QTableWidgetItem(lista.obtener(aux).get_nombre() )
    peso =QtGui.QTableWidgetItem( str(lista.obtener(aux).get_peso()) )
    raza = QtGui.QTableWidgetItem( lista.obtener(aux).get_raza() )
    dueño = QtGui.QTableWidgetItem( str(lista.obtener(aux).get_dueño() ))
    paseador = QtGui.QTableWidgetItem( str(lista.obtener(aux).get_paseador()) )
    tabla_mascota.setItem(pos ,0 , nombre)
    tabla_mascota.setItem(pos ,1 ,raza)
    tabla_mascota.setItem(pos ,2, peso)
    tabla_mascota.setItem(pos ,3 ,dueño )
    tabla_mascota.setItem(pos ,4,paseador)
    
    
def add_in_tabla_paseo(tabla,lista):
    aux = lista.tamanio() -1
    tabla.insertRow(aux)
    paseador = QtGui.QTableWidgetItem(lista.obtener(aux).get_paseador().get_apellido_nombre() )
    horaS =QtGui.QTableWidgetItem( lista.obtener(aux).get_hora_salida() )
    ID = QtGui.QTableWidgetItem( str(lista.obtener(aux).get_id() ) )
    tiempo = QtGui.QTableWidgetItem( str(lista.obtener(aux).get_tiempo_tentativo() ) + ' hs')
    horal = QtGui.QTableWidgetItem( lista.obtener(aux).get_hora_llegada()) 
    tabla.setItem(aux ,0 ,ID)
    tabla.setItem(aux ,1 ,paseador )
    tabla.setItem(aux ,2, horaS)
    tabla.setItem(aux ,3 ,tiempo  )
    tabla.setItem(aux ,4,horal )
    
def CargarTablaPaseo(tabla,lista):
        fila = 0
        for aux in lista.lista:
            #tabla.insertRow(fila)
            paseador = QtGui.QTableWidgetItem( aux.get_paseador().get_apellido_nombre() )
            horaS =QtGui.QTableWidgetItem( aux.get_hora_salida() )
            ID = QtGui.QTableWidgetItem( str(aux.get_id()) )
            tiempo = QtGui.QTableWidgetItem( str(aux.get_tiempo_tentativo())+ ' hs')
            horal = QtGui.QTableWidgetItem( aux.get_hora_llegada() )
            tabla.setItem(fila ,0 ,ID)
            tabla.setItem(fila ,1 , paseador )
            tabla.setItem(fila ,2, horaS)
            tabla.setItem(fila ,3 ,tiempo )
            tabla.setItem(fila ,4,horal )
            fila+=1