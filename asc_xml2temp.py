# -*- coding: utf-8 -*-

"""
usage: asc_xml2temp [options]
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
    sys.exit(2)


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
        _print_help()

    if not config:
        print_err('config not specified')
        _print_help()

    if config.get('SRC_XML', None) is None:
        print_err('SRC_XML not specified')
        _print_help()

    if config.get('TEMPLATE', None) is None:
        print_err('TEMPLATE not specified')
        _print_help()

    config['LANG_CODE'] = to_str(config.get('LANG_CODE', Lang.EN.code))

    return config


def gen_template(src_path, template_path, lang_code):
    generator = TemplateGenerator()

    str_res_xml = StrResXml(src_path)
    trans_entities = str_res_xml.gen_trans_entities()

    generator.append_trans_entities(trans_entities)

    generator.gen_template(output_path=template_path, lang_code=lang_code)

    print('Generate success! Template file: ' + path.realpath(template_path))


def main():
    config = _parse_options()

    src_path = config.get('SRC_XML')

    template_path = config.get('TEMPLATE')

    lang_code = config.get('LANG_CODE')

    gen_template(src_path, template_path, lang_code)

if __name__ == '__main__':
    main()
