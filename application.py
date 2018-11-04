#!/usr/bin/python3
from snake import *
class Application(Tk):
    """This Class define the display screen and the Application attributes"""

    def __init__(self, larg=500, haut=500):
        Tk.__init__(self)
        self.title("Snake GAME")
        self.larg, self.haut = larg, haut
        self.can = Canvas(self, bg='dark green', width=larg,
                          height=haut)
        self.can.pack(padx=5, pady=5)

        # we create the snake instance from the Snake class
        self.snik1 = Snik(self.can, self.larg, self.haut, 0)

        self.bou2 = Button(self, text="Restart", width=10, command=self.restart)
        self.bou2.pack(side=LEFT)

        self.bind("<Left>", self.go_left)
        self.bind("<Right>", self.go_right)
        self.bind("<Up>", self.go_up)
        self.bind("<Down>", self.go_down)
        self.bind("<space>",self.stop_it)

    def start_it(self):
        "Demarrage de l'animation"
        if self.snik1.flag == 0:
            self.snik1.flag = 1
            self.snik1.move()

    def stop_it(self,event=None):
        "Arret de l'animation"
        self.snik1.flag = 0

    def restart(self):
        self.can.delete(ALL)
        self.snik1 = Snik(self.can, self.larg, self.haut, 0)

    def go_left(self, event=None):
        "move to left"
        if self.snik1.dx == 0 :
            self.snik1.dx, self.snik1.dy = -1, 0
            self.start_it()
    def go_right(self, event=None):
        "move to right"
        if self.snik1.dx == 0 :
            self.snik1.dx, self.snik1.dy = 1, 0
            self.start_it()

    def go_up(self, event=None):
        "move to up"
        if self.snik1.dy ==0 :
            self.snik1.dx, self.snik1.dy = 0, -1
            self.start_it()
    def go_down(self, event=None):
        "move to down"
        if self.snik1.dy==0 :
            self.snik1.dx, self.snik1.dy = 0, 1
            self.start_it()

if __name__ == "__main__":
    Application().mainloop()