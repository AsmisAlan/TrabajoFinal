# -*- coding: utf-8 -*-
"""
Created on Fri Oct 23 14:50:19 2015

@author: alan
"""

from PyQt4 import QtGui, uic , QtCore
mapax = uic.loadUiType("interfas/mapa.ui")[0]
class Mapa(QtGui.QWidget,mapax):
    
    def __init__(self,direccion, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.setupUi(self)
        self.dir = direccion
        self.zoom = 14
        self.latitud = 769132
        self.longitud = 2309826
        self.style = 'roadmap'
        self.mapa.setUrl(QtCore.QUrl( self.set_direccion(direccion)))   
        self.mas_zoom.clicked.connect(self.zoomMas)
        self.menos_zoom.clicked.connect(self.zoomMenos)
        self.up.clicked.connect(self.goUp)
        self.down.clicked.connect(self.goDown)
        self.left.clicked.connect(self.goLeft)
        self.right.clicked.connect(self.goRight)
        self.road.clicked.connect(self.changeToRoad)
        self.satelital.clicked.connect(self.changeToSatelital)
        
    def set_direccion(self , direccion ):
        url = "http://maps.googleapis.com/maps/api/staticmap?"
        center = "center= -32.4"+str(self.latitud)+",-58."+str(self.longitud)
        zoom = "&zoom="+str(self.zoom)
        size = "&size=640x640"
        markers = "&markers=" + direccion 
        path = "&path=" + direccion
        imgformat = "&format=png"
        maptype="&maptype="+self.style    
        sensor = "&sensor=true"
        url = url + center + zoom + size + markers+ path + imgformat + maptype + sensor
        return url
        
    def zoomMas(self):
        if self.zoom < 20 :
            self.zoom +=1
            self.mapa.load(QtCore.QUrl( self.set_direccion(self.dir))) 
        
    def zoomMenos(self):
        if self.zoom > 0 :
            self.zoom -=1
            self.mapa.load(QtCore.QUrl( self.set_direccion(self.dir))) 
        
    def goUp(self):
        self.latitud -= (self.spinBox.value() * 100 )
        self.mapa.load(QtCore.QUrl( self.set_direccion(self.dir))) 
    
    def goDown(self):
        self.latitud += (self.spinBox.value() * 100 )
        self.mapa.load(QtCore.QUrl( self.set_direccion(self.dir))) 
    
    def goRight(self):
        self.longitud -= (self.spinBox.value() * 100 )
        self.mapa.load(QtCore.QUrl( self.set_direccion(self.dir))) 
    
    def goLeft(self):
        self.longitud += (self.spinBox.value() * 100 )
        self.mapa.load(QtCore.QUrl( self.set_direccion(self.dir))) 
    
    def changeToRoad(self):
        if self.style != 'roadmap' : 
            self.style = 'roadmap'
            self.mapa.load(QtCore.QUrl( self.set_direccion(self.dir)))
            
        
    def changeToSatelital(self):
        if self.style != 'hybrid' : 
            self.style = 'hybrid'
            self.mapa.load(QtCore.QUrl( self.set_direccion(self.dir)))
        
    