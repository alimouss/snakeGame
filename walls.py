from tkinter import *


class Wall(object):
    def __init__(self, can, xpos, ypos, dx, dy):
        self.can = can
        self.dx, self.dy = dx, dy
        self.x = xpos
        self.y = ypos
        cc = 15
        self.infoCoords = []
        for i in range(5):
            if self.x == xpos + 45 * dx:
                self.y = self.y + self.dy * cc
            else:
                self.x = self.x + self.dx * cc
            v,u = self.x,self.y
            self.infoCoords.append((v,u))
            self.can.create_rectangle(self.x, self.y, self.x + cc, self.y + cc,
                                      fill='red')


if __name__ == '__main__':
    tk = Tk()
    tk.title("Test lobo")
    heigh =300
    width = 400
    can = Canvas(tk, heigh=heigh, width=width, bg='green')
    can.pack()

    InfoList = ((70, 25, -1, 1), (width-80, 25, 1, 1), (70, heigh-40, -1, -1), (width-80, heigh-40, 1, -1))

    for x, y, dx, dy in InfoList:
        L = Wall(can, x, y, dx, dy)

    tk.mainloop()
