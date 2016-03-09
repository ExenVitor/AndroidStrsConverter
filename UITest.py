# -*- coding: utf-8 -*-

from tkinter import *
from XlWorkers.StrResXml import StrResXml
from XlWorkers.Entities import TransEntity

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

    str_res_xml = StrResXml('en_strings.xml')
    trans_entities = str_res_xml.gen_trans_entities()

    generator.append_trans_entities(trans_entities)

    generator.gen_template()
