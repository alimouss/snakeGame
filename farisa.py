#!/usr/bin/python3
from tkinter import *
from random import randrange

class Farisa(object):
    def __init__(self,can,posX=0,posY=0,coul="red",infolist=[]):
        self.info = infolist
        self.can=can                ## Display screen (canvas)
        self.coul=coul              ## color of Farisa
        self.xf,self.yf =posX,posY  ## (y,x) position of head of farisa  in the canvas
        self.cc=15                  ## rayon of farisa body
        self.coordf= []
        self.body= self.can.create_oval(self.xf,self.yf,self.xf+self.cc,    ## body of farisa
                                             self.yf+self.cc,fill=coul)
        self.coordf=[self.body,self.xf,self.yf]    ## a list which contain three elements (reference of body, posX, posY)

    def move_random(self):
        """This method allows the farise move randomly in the canvas"""
        self.coordf[1],self.coordf[2] = randrange(10,490,15),randrange(10,490,15)

        for i in range(len(self.info)):
            if (self.coordf[1], self.coordf[2]) not in self.info[i]:
                self.can.coords(self.coordf[0],self.coordf[1],self.coordf[2],
                                self.coordf[1]+self.cc,self.coordf[2]+self.cc)