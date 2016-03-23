# -*- coding: utf-8 -*-
from XlWorkers.Config import Lang
from XlWorkers.StrResXml import StrResXml
from XlWorkers.TemplateReader import TemplateReader
import XlWorkers.Utils as Utils

__author__ = 'Vitor Chen'


def main():
    template = TemplateReader('../guide.xlsx')

    path = '../output/values'
    xml_name = '/fotor_strings.xml'
    fullpath = []
    lang_codes = []

    for lang_obj in Lang:
        for region_code in lang_obj.reverse_region_codes():
            suffix = '-' + region_code if Utils.is_str_valid(region_code) else region_code
            fullpath.append(path + suffix + xml_name)
            lang_codes.append(lang_obj.code)

    print(str(fullpath))

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


if __name__ == '__main__':
    main()
