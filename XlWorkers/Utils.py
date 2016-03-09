# -*- coding: utf-8 -*-

__author__ = 'Vitor Chen'


def is_str_valid(tar_str):
    if isinstance(tar_str, str) and len(tar_str) > 0:
        return True
    else:
        return False
