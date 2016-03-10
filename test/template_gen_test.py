# -*- coding: utf-8 -*-
from XlWorkers.StrResXml import StrResXml
from XlWorkers import TemplateGenerator

__author__ = 'Vitor Chen'


def main():
    generator = TemplateGenerator.TemplateGenerator()

    str_res_xml = StrResXml('../en_strings.xml')
    trans_entities = str_res_xml.gen_trans_entities()

    generator.append_trans_entities(trans_entities)

    generator.gen_template(output_path='../template.xlsx')


if __name__ == '__main__':
    main()
