# -*- coding: utf-8 -*-
from XlWorkers.Config import LangCode
from XlWorkers.StrResXml import StrResXml
from XlWorkers.TemplateReader import TemplateReader
import XlWorkers.Utils as Utils

__author__ = 'Vitor Chen'


def main():
    tar_lang_code = LangCode.ZH.code

    template = TemplateReader('../template.xlsx')

    out_xml = StrResXml('../out_strings.xml')
    for entity in out_xml.gen_trans_entities():
        trans_str = template.get_res_str(tar_lang_code, entity.key)
        if Utils.is_str_valid(trans_str):
            out_xml.update_res_node(entity.key, trans_str)
    out_xml.save()


if __name__ == '__main__':
    main()