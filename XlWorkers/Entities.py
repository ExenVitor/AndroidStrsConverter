# -*- coding: utf-8 -*-

__author__ = 'Vitor Chen'


class TransEntity(object):
    def __init__(self, key, trans_str, desc=''):
        super().__init__()
        self.key = key
        self.trans_str = trans_str
        self.desc = desc
