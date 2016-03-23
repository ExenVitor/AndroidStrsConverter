# -*- coding: utf-8 -*-

import tkinter as tk

__author__ = 'Vitor Chen'


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.helloLabel = tk.Label(self, text='Hello World!')
        self.helloLabel.pack()

        self.hi_there = tk.Button(self)
        self.hi_there['text'] = "Hello World\n(click me)"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side='top')

        self.quitButton = tk.Button(self, text='Quit', fg="red", command=self.quit)
        self.quitButton.pack(side='bottom')

    def say_hi(self):
        print("Hi there, everyone!")


if __name__ == '__main__':
    root = tk.Tk()
    app = Application(master=root)
    app.master.title('Hello World')
    app.mainloop()

