# -*- coding: utf-8 -*-

__author__ = 'Vitor Chen'

import XlWorkers.Utils as Utils
from XlWorkers.Entities import TransEntity
from lxml import etree


class StrResXml(object):
    _STR_TAG = 'string'
    _NAME_ATTR = 'name'

    def __init__(self, filename):
        super().__init__()
        self._filename = filename
        self._str_ele_map = {}
        self._xml_tree = etree.parse(filename)
        root_resource = self._xml_tree.getroot()
        for str_node in root_resource.findall(self._STR_TAG):
            node_attrib = str_node.attrib
            res_name = node_attrib.get(self._NAME_ATTR)
            if Utils.is_str_valid(res_name):
                self._str_ele_map[res_name] = str_node

    def get_res_value(self, res_name):
        result = ''
        str_node = self.get_res_node(res_name)
        if str_node is not None:
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

    def update_res_node(self, res_name, trans_str):
        str_node = self.get_res_node(res_name)
        if str_node is not None:
            str_node.text = trans_str

    def save(self, file_or_filename=None):
        if not file_or_filename:
            file_or_filename = self._filename
        self._xml_tree.write(file_or_filename, encoding="utf-8", xml_declaration=True, pretty_print=True)
