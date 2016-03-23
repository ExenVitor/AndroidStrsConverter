# -*- coding: utf-8 -*-

__author__ = 'Vitor Chen'

from XlWorkers.StrResXml import StrResXml


def main():
    src_file = '../en_strings.xml'
    out_file = '../out_strings.xml'

    src_xml_ob = StrResXml(src_file)

    src_xml_ob.save(file_or_filename=out_file)


if __name__ == '__main__':
    main()
