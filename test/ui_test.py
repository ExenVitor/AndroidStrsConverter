# -*- coding: utf-8 -*-

from tkinter import *

__author__ = 'Vitor Chen'


class Application(Frame):
    def __init__(self, master=None, cnf=None, **kw):
        if not cnf:
            cnf = {}
        super().__init__(master, cnf, **kw)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.helloLabel = Label(self, text='Hello World!')
        self.helloLabel.pack()
        self.quitButton = Button(self, text='Quit', command=self.quit)
        self.quitButton.pack()


if __name__ == '__main__':
    app = Application()
    app.master.title('Hello World')
    app.mainloop()

