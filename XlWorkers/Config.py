# -*- coding: utf-8 -*-
from enum import Enum

from XlWorkers.CellInfo import *

__author__ = 'Vitor Chen'


# language list
class LangCode(Enum):
    EN = 'en'
    DE = 'de'
    ES = 'es'
    FR = 'fr'
    IN = 'in'
    IT = 'it'
    JA = 'ja'
    KO = 'ko'
    PT = 'pt'
    RU = 'ru'
    TH = 'th'
    TR = 'tr'
    VI = 'vi'
    ZH = 'zh'
    ZH_rHK = 'zh-rHK'
    ZH_rTW = 'zh-rTW'


HEADER_COL_LIST = [HeaderColInfo('String res key'),
                   HeaderColInfo('Description'), ]
for lang_code in LangCode:
    HEADER_COL_LIST.append(LangColInfo(lang_code.name, lang_code.value))
