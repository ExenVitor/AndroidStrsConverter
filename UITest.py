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

    from XlWorkers.Entities import TransEntity
    trans_entities = []
    for i in range(10):
        res_key = 'string_res_{0}'.format(i)
        trans_str = 'Hello_res_{0}'.format(i)
        trans_entities.append(TransEntity(res_key, trans_str))
    generator.append_trans_entities(trans_entities)

    generator.gen_template()
