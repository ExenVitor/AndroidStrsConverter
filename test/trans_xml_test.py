# -*- coding: utf-8 -*-
from XlWorkers.Config import LangCode
from XlWorkers.StrResXml import StrResXml
from XlWorkers.TemplateReader import TemplateReader
import XlWorkers.Utils as Utils

__author__ = 'Vitor Chen'


def main():
    template = TemplateReader('../guide.xlsx')

    path = '../output/values'
    xml_name = '/fotor_strings.xml'
    fullpath = []
    codes = []

    for lang_code in LangCode:
        subfix = ''
        if lang_code.code == LangCode.EN.code:
            subfix = ''
        elif lang_code.code == LangCode.ZH_rHK.code:
            continue
        else:
            subfix = '-' + lang_code.code

        fullpath.append(path + subfix + xml_name)
        codes.append(lang_code.code)

    fullpath.append(path + '-zh-rHK' + xml_name)
    codes.append(LangCode.ZH_rHK.code)
    fullpath.append(path + '-zh-rTW' + xml_name)
    codes.append(LangCode.ZH_rHK.code)

    print(str(fullpath))

    for i in range(0, len(fullpath)):
        file_path = fullpath[i]
        tar_lang_code = codes[i]
        out_xml = StrResXml(file_path)
        for entity in out_xml.gen_trans_entities():
            trans_str = template.get_res_str(tar_lang_code, entity.key)
            if Utils.is_str_valid(trans_str):
                out_xml.update_res_node(entity.key, trans_str)
        out_xml.save()


if __name__ == '__main__':
    main()
