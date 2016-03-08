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
    # app = Application()
    # app.master.title('Hello World')
    # app.mainloop()

    from XlWorkers import TemplateGenerator

    generator = TemplateGenerator.TemplateGenerator()
    str_keys = ('string_res_1', 'string_res_2', 'string_res_3')
    generator.append_res_keys(str_keys)
    str_descs = ('desc_1', 'desc_2', 'desc_3')
    generator.append_res_descs(str_descs)
    generator.gen_template()
