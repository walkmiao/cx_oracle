#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/27 12:11
# @Author  : LCH
# @Site    : 
# @File    : handleItem.py
# @Software: PyCharm
from PyQt5.QtCore import QThread
from PyQt5.QtGui import QStandardItem, QStandardItemModel
import xlrd


class HandleItem(QThread):
    def __init__(self, parent):
        self.window = parent

    def handle_item(self, path='item.xlsx'):
        self.window.item_model.clear()
        self.window.factory_model.clear()
        self.window.factory_model.setHorizontalHeaderLabels(['电厂名称', '电厂指标'])
        self.window.item_model.setHorizontalHeaderLabels(['类型名称', '类型指标'])
        wb = xlrd.open_workbook(path)
        sheets = wb.sheets()
        factory_code_sheet, item_code_sheet = sheets
        for row_num in range(1, factory_code_sheet.nrows):
            row_data = factory_code_sheet.row_values(row_num)
            print(row_data)
            self.window.factory_model.appendRow([QStandardItem(str(int(i))) if not isinstance(i, str) else
                                                 QStandardItem(i) for i in row_data])
        for row_num in range(1, item_code_sheet.nrows):
            row_data = item_code_sheet.row_values(row_num)
            print(row_data)
            self.window.item_model.appendRow([QStandardItem(str(int(i))) if not isinstance(i, str) else
                                              QStandardItem(i) for i in row_data])



if __name__ == '__main__':
    pass
