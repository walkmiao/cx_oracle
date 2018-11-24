#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/29 10:33
# @Author  : LCH
# @Site    : 
# @File    : test.py
# @Software: PyCharm
from myUI import Ui_MainWindow
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMessageBox
from PyQt5.QtCore import QObject,pyqtSignal
from oracle_handle import OracleInit
from config import *
import sys
import time
import xlrd, xlwt


class MyWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    sendmsg = pyqtSignal(int)
    sendmsg2 = pyqtSignal(int)

    def __init__(self):
        super(MyWindow, self).__init__()
        self.setupUi(self)
        # 根据模板生成后自己再做一些自定义
        self.model = QStandardItemModel()  # tableview的model
        self.model.setHorizontalHeaderLabels(['IRN', 'MRID', 'NAME'])
        self.tableView.horizontalHeader().setStretchLastSection(True)  # 水平方向标签拓展剩下的窗口部分，填满表格
        self.tableView.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)  # 水平方向，表格大小拓展到适当的尺寸
        self.tableView.setModel(self.model)  # 实现和model的绑定
        self.log_mode = QStandardItemModel()
        self.log_mode.setHorizontalHeaderLabels(['时间', '事件'])
        self.tableView_2.setModel(self.log_mode)
        self.tableView_2.horizontalHeader().setStretchLastSection(True)  # 水平方向标签拓展剩下的窗口部分，填满表格
        self.tableView_2.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)  # 水平方向，表格大小拓展到适当的尺寸

    def get_time(self):
        t = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        return t

    def sql_query(self):
        self.append_log("当前通过查询框输入获取输出结果！")
        self.model.clear()
        self.model.setHorizontalHeaderLabels(['IRN', 'MRID', 'NAME'])
        # try:
        #     self.statusbar.showMessage("正在连接数据库de3db....")
        #     self.ora_ins = OracleInit(self, table=table, user=user, pwd=pwd, host=host, service_name=sid)
        #     self.statusbar.showMessage("连接数据库de3db成功....", 5000)
        #     self.ora_ins.start()
        # except Exception as e:
        #     self.statusbar.showMessage("连接数据库de3db失败", 5000)
        #     self.append_log("[ERROR]{}".format(e))
        # self.statusbar.showMessage("正在连接数据库de3db....")
        # self.ora_ins = OracleInit(self, table=table, user=user, pwd=pwd, host=host, service_name=sid)
        # self.statusbar.showMessage("连接数据库de3db成功....", 5000)
        if self.ora_ins:
            self.ora_ins.start()
        else:
            self.append_log("无法打开数据库")

    def output_excel(self):
        xls_file = self.filepath.text()
        if xls_file != '':
            self.append_log("当前通过excel文件获取输出结果！")
        save_path, _ = QFileDialog.getSaveFileName(self, 'Open file', 'C:\\', 'XLS files (*.xls *.xlsx )')
        try:
            wt = self.get_excel_input(xls_file)
            wt.save(save_path)
            self.append_log("保存输出结果至{}成功！".format(save_path))
        except Exception as e:
            self.append_log(e)

    def __getattr__(self, item):
        try:
            self.statusbar.showMessage("正在连接数据库de3db....")
            self.ora_ins = OracleInit(self, table=table, user=user, pwd=pwd, host=host, service_name=sid)
            self.statusbar.showMessage("连接数据库de3db成功....", 5000)
            return self.ora_ins
        except:
            self.statusbar.showMessage("连接数据库de3db失败", 5000)
            return

    def get_excel_input(self, file_path, num=20):
        wt = xlwt.Workbook()
        write_table = wt.add_sheet("result")  # 在Excel工作簿里面创建一个的表格
        wb = xlrd.open_workbook(file_path)
        sheet = wb.sheets()[0]
        mrid_col = sheet.col_values(1)[1:]
        result = []
        input_mrid_num = 0
        if self.ora_ins:
            while mrid_col:
                if len(mrid_col) >= num:
                    mrid_list = mrid_col[:num]
                    mrid_col = mrid_col[num:]
                else:
                    mrid_list = mrid_col[:]
                    mrid_col.clear()
                try:
                    fetch_result = self.ora_ins.sql_query(table, mrid_list)
                except Exception as e:
                    self.append_log("[ERROR]{}".format(e))
                    fetch_result = []
                input_mrid_num += len(mrid_list)
                result += fetch_result
            self.sendmsg.emit(input_mrid_num)
            if result:
                row_num = len(result)
                self.sendmsg2.emit(row_num)
                column_num = len(result[0])
                for row in range(row_num):
                    for col in range(column_num):
                        temp_data = result[row][col]
                        write_table.write(row, col, temp_data)
            return wt
        else:
            return

    def append_log(self, param):
        self.log_mode.appendRow([QStandardItem(self.get_time()), QStandardItem(param)])

    def open_file(self):
        # 从C盘打开文件格式（*.jpg *.gif *.png *.xls）文件，返回路径
        xls_file, _ = QFileDialog.getOpenFileName(self, 'Open file', 'C:\\', 'Image files (*.xls *.xlsx )')
        self.filepath.setText(xls_file)
        return xls_file


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.sendmsg.connect(window.lcdNumber.display)
    window.sendmsg2.connect(window.lcdNumber_2.display)
    window.show()
    sys.exit(app.exec_())