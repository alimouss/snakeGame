#!/usr/bin/python3
from farisa import *
from status import *
from walls import *
class Snik(object):
    def __init__(self, can, larg, haut, flag=0, coul="red"):
        self.canx, self.cany = larg, haut  ## width and high of the canvas(display screen)
        self.coul = coul  ## the color of the snake
        self.can = can
        self.flag = flag  ## the flag
        self.dx, self.dy = 0, 0  ## the orients of  x & y positions of snake
        x, y, self.cc = 100, 100, 15  ## x & y positions , rayon of each part in the snake body
        self.serp = []
        """Here we create the snake body with five parts and 
           saved each information(reference of parts , x & y positions)
           of parts in a list , finaly we saved this lists in one list called serp"""
        i = 0
        while i < 5:
            self.carre = self.can.create_oval(x, y, x + self.cc, y + self.cc,
                                              fill=self.coul)
            self.serp.append([self.carre, x, y])
            x = x + self.cc
            i = i + 1
        """creation the instants"""
        InfoList = ((70, 25, -1, 1), (self.canx - 80, 25, 1, 1), (70, self.cany - 40, -1, -1),
                    (self.canx - 80, self.cany - 40, 1, -1))
        # Hera we create an instant from the wall class

        self.walls = []
        for x, y, dx, dy in InfoList:
            self.wall = Wall(self.can, x, y, dx, dy)
            self.walls.append(self.wall.infoCoords)
        # Here we create an instant from the Farisa class
        self.farisa = Farisa(can, larg / 2, haut / 2, coul='blue',infolist=self.walls)
        # Here we create an instant from the state class
        self.st = State(can, larg, haut)
        # Hera we create an instant from the wall class

        self.walls = []
        for x, y, dx, dy in InfoList:
            self.wall = Wall(self.can, x, y, dx, dy)
            self.walls.append(self.wall)

    def move(self):
        c = self.serp[0]  ## The head of snake [reference of the head ,x,y]
        cq = c[0]  ## The reference of the head
        l = len(self.serp)  ## The length of the snake
        c = self.serp[l - 1]  ## The tale of the snake
        xt, yt = c[1], c[2]  ## x & y positions of the tale

        xq, yq = xt + self.dx * self.cc, yt + self.dy * self.cc  # the xt and yt  becomes the the position of head

        if xq < 0 or xq > self.canx - self.cc or yq < 0 or yq > self.cany - self.cc :
            self.flag =0
            self.st.lose()


        if xq == self.farisa.coordf[1] and yq == self.farisa.coordf[2]:
            self.st.score += 1
            self.farisa.move_random()
            carre1 = self.can.create_oval(xq, yq, xq + self.cc, yq + self.cc,
                                          fill="red")  # we add another parts in the snake
            self.serp.append([carre1, self.farisa.coordf[1], self.farisa.coordf[2]])


        # we move move the tale to the the head (will be comes new head in the can)
        self.can.coords(cq, xq, yq, xq + self.cc,yq + self.cc)

        # we add the 3 informations of the new head in the list serp
        self.serp.append([cq, xq, yq])

        del (self.serp[0])  # we deleted the old head in the list


        if self.isSnarl(xq,yq):
            self.flag=0
            self.st.lose()

        # we count the score if the score = 10 we show them in the canvas
        if self.st.score == 15:
            self.flag=0
            self.st.win()

        # if flag is 1 the snake stay move
        if self.flag > 0:
            self.can.master.after(100, self.move)

    def isSnarl(self,xq,yq):
        listOfPosition =[]
        for part in self.serp[:-1]:
            (x,y) = part[1],part[2]
            listOfPosition.append((x,y))
        if (xq,yq) in listOfPosition:
            return True
        else:
            return False
