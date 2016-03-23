# -*- coding: utf-8 -*-

"""
usage: asc_trans [options] xmlfilename1 [... xmlfilenameN]
Translate Android string resource xml from a template xlsx file

Translate options:
    -t TEMPLATE         path to output xlsx file
    -d RES_DIR          path to Android res directory

General options:
    -h, --help          show this help message and exit
"""

from os import path
import sys
import getopt
from XlWorkers import Utils
from XlWorkers.Config import Lang
from XlWorkers.StrResXml import StrResXml
from XlWorkers.TemplateReader import TemplateReader
from XlWorkers.Utils import to_str, print_err

__author__ = 'Vitor Chen'


def _print_help():
    print(__doc__)
    sys.exit(2)


def _parse_options():
    shortopts = 'ht:d:'
    longopts = ['help']

    try:
        optlist, xmlfiles = getopt.getopt(sys.argv[1:], shortopts, longopts)

        config = {}

        for key, value in optlist:
            if key in ('-h', '--help'):
                _print_help()
            elif key == '-t':
                config['TEMPLATE'] = to_str(value)
            elif key == '-d':
                config['RES_DIR'] = to_str(value)
    except getopt.GetoptError as e:
        print_err(e)
        _print_help()

    if not config:
        print_err('config not specified')
        _print_help()

    if not xmlfiles:
        print_err('must specified xml file name')
        _print_help()

    if config.get('TEMPLATE', None) is None:
        print_err('TEMPLATE not specified')
        _print_help()

    if config.get('RES_DIR', None) is None:
        print_err('RES_DIR not specified')
        _print_help()

    rel_file_names = []
    for filename in xmlfiles:
        rel_file_names.append(to_str(path.basename(path.normpath(filename))))

    print(rel_file_names)

    config['XML_FILES'] = rel_file_names

    return config


def trans(temp_file, res_dir, xml_files):
    template = TemplateReader(temp_file)

    fullpath = []
    lang_codes = []

    for xml_file in xml_files:
        for lang_obj in Lang:
            for region_code in lang_obj.reverse_region_codes():
                suffix = '-' + region_code if Utils.is_str_valid(region_code) else region_code
                values_dir = path.join(res_dir, 'values' + suffix)
                fullpath.append(path.join(values_dir, xml_file))
                lang_codes.append(lang_obj.code)

    for i in range(0, len(fullpath)):
        file_path = fullpath[i]
        tar_lang_code = lang_codes[i]
        out_xml = StrResXml(file_path)
        for entity in out_xml.gen_trans_entities():
            trans_str = template.get_res_str(tar_lang_code, entity.key)
            if Utils.is_str_valid(trans_str):
                out_xml.update_res_node(entity.key, trans_str)
        out_xml.save()
        print("Finish translate: " + file_path)
    pass


def main():
    config = _parse_options()

    temp_file = config.get('TEMPLATE')
    res_dir = config.get('RES_DIR')
    xml_files = config.get('XML_FILES')

    trans(temp_file, res_dir, xml_files)


if __name__ == '__main__':
    main()
