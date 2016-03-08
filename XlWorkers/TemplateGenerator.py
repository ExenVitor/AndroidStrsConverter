# -*- coding: utf-8 -*-

from openpyxl import Workbook

from XlWorkers.Config import *

__author__ = 'Vitor Chen'


class TemplateGenerator(object):
    def __init__(self):
        super().__init__()
        self.str_descs = []
        self.str_keys = []
        self.column_titles = []
        for col_info in HEADER_COL_LIST:
            self.column_titles.append(col_info.display_name)

    def append_res_keys(self, keys):
        if self.__verify_input_array(keys):
            self.str_keys.extend(keys)

    def append_res_descs(self, descriptions):
        if self.__verify_input_array(descriptions):
            self.str_descs.extend(descriptions)

    def gen_template(self, output_path=None):
        wb = Workbook()
        ws = wb.active
        ws.append(self.column_titles)

        self._write_res_keys(ws)
        self._write_res_descs(ws)

        if output_path is None:
            output_path = 'template.xlsx'
        wb.save(output_path)

    def _write_res_keys(self, ws):
        key_start_row = 2
        key_col = 1
        keys_count = len(self.str_keys)

        if keys_count > 0:
            for i in range(keys_count):
                cell = ws.cell(row=key_start_row + i, column=key_col)
                cell.value = self.str_keys[i]

    def _write_res_descs(self, ws):
        desc_start_row = 2
        desc_col = 2
        descs_count = len(self.str_descs)

        if descs_count > 0:
            for i in range(descs_count):
                cell = ws.cell(row=desc_start_row + i, column=desc_col)
                cell.value = self.str_descs[i]

    @staticmethod
    def __verify_input_array(input_array):
        if isinstance(input_array, (list, tuple)):
            return True
        else:
            raise TypeError('Value must be a list, tuple. Supplied value is {0}'.format(
                type(input_array)))
