# -*- coding: utf-8 -*-

__author__ = 'Vitor Chen'

import xml.etree.ElementTree as ET
import XlWorkers.Utils as Utils
from XlWorkers.Entities import TransEntity


class StrResXml(object):
    _STR_TAG = 'string'
    _NAME_ATTR = 'name'

    def __init__(self, filename):
        super().__init__()
        self._str_ele_map = {}
        self._xml_tree = ET.parse(filename)
        root_resource = self._xml_tree.getroot()
        for str_node in root_resource.findall(self._STR_TAG):
            node_attrib = str_node.attrib
            res_name = node_attrib.get(self._NAME_ATTR)
            if Utils.is_str_valid(res_name):
                self._str_ele_map[res_name] = str_node

    def get_res_value(self, res_name):
        result = ''
        str_node = self.get_res_node(res_name)
        if str_node:
            result = str_node.text
        return result

    def get_res_node(self, res_name):
        str_node = self._str_ele_map.get(res_name)
        return str_node

    def gen_trans_entities(self):
        entities = []
        keys = self._str_ele_map.keys()
        if keys is not None:
            for key in keys:
                trans_str = self._str_ele_map.get(key).text
                trans_entity = TransEntity(key, trans_str)
                entities.append(trans_entity)
        return entities
