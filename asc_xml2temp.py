# -*- coding: utf-8 -*-

"""
usage: asc_xml2temp [OPTION]...
Convert Android string resource xml to a template xlsx file

Convert options:
    -s SRC_XML          path to resource xml file
    -t TEMPLATE         path to output xlsx file
    --lang LANG_CODE    specified the language code of the resource xml file, default: en

general options:
    -h, --help          show this help message and exit
"""

import sys
import getopt
from XlWorkers.Utils import to_str, print_err
from XlWorkers.Config import Lang
from XlWorkers.StrResXml import StrResXml
from XlWorkers.TemplateGenerator import TemplateGenerator
from os import path

__author__ = 'Vitor Chen'


def _print_help():
    print(__doc__)
    sys.exit()


def _parse_options():
    shortopts = 'hs:t:'
    longopts = ['help', 'lang=']

    try:
        optlist, args = getopt.getopt(sys.argv[1:], shortopts, longopts)

        config = {}

        for key, value in optlist:
            if key in ('-h', '--help'):
                _print_help()
            elif key == '-s':
                config['SRC_XML'] = to_str(value)
            elif key == '-t':
                config['TEMPLATE'] = to_str(value)
            elif key == '--lang':
                config['LANG_CODE'] = to_str(value)
    except getopt.GetoptError as e:
        print_err(e)
        sys.exit(2)

    if not config:
        print_err('config not specified')
        _print_help()
        sys.exit(2)

    if config.get('SRC_XML', None) is None:
        print_err('SRC_XML not specified')
        _print_help()
        sys.exit(2)

    if config.get('TEMPLATE', None) is None:
        print_err('TEMPLATE not specified')
        _print_help()
        sys.exit(2)

    config['LANG_CODE'] = to_str(config.get('LANG_CODE', Lang.EN.code))

    return config


def main():
    config = _parse_options()

    generator = TemplateGenerator()

    str_res_xml = StrResXml(config.get('SRC_XML'))
    trans_entities = str_res_xml.gen_trans_entities()

    generator.append_trans_entities(trans_entities)

    template_path = config.get('TEMPLATE')

    generator.gen_template(output_path=config.get('TEMPLATE'), lang_code=config.get('LANG_CODE'))

    print('Generate success! Template file: ' + path.realpath(template_path))

if __name__ == '__main__':
    main()
