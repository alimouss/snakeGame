#!/usr/bin/python3
from tkinter import *

class State(object):
    def __init__(self,can, larg, haut):
        self.score = 0
        self.can,self.canx,self.cany = can, larg, haut  # The three elements (canvas,him width & high)

    def win(self):
        self.can.delete(ALL)
        self.can.create_text(self.canx / 2, self.cany / 2, anchor=CENTER,
                             text="لقد ربحت و رصيدك هو {0}".format(self.score),
                             fill="blue", font="Arail 16 bold")
    def lose(self):
        self.can.delete(ALL)
        self.can.create_text(self.canx / 2, self.cany / 2, anchor=CENTER,
                             text="لقد خسرت", fill="red", font="Arail 18 bold")
