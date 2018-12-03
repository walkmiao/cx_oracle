#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/24 9:43
# @Author  : LCH
# @Site    : 
# @File    : oracle_demo.py
# @Software: PyCharm
import re
import cx_Oracle
from PyQt5.QtCore import QThread
from PyQt5.QtGui import QStandardItem


class OracleInit(QThread):
    def __init__(self, window,table, user, pwd, host, service_name, port=1521):
        super(OracleInit, self).__init__()
        self.window = window
        self.table = table
        self.user = user
        self.pwd = pwd
        self.host = host
        self.service_name = service_name
        self.port = port
        try:
            self.conn = cx_Oracle.connect("{user}/{pwd}@{host}:{port}/{sid}"
                                          .format(user=self.user, pwd=self.pwd,
                                           host=self.host, sid=self.service_name,port=self.port))
        except Exception as e:
            raise e

    def get_cursor(self):
        if self.conn:
            cur = self.conn.cursor()
            return cur
        else:
            return

    def sql_query(self, table, keyword=None):
        if keyword:
            if not isinstance(keyword, list):
                if '\n' in keyword:
                    keyword = [i for i in keyword.split('\n') if i]
                elif ' ' in keyword:
                    keyword = [i for i in keyword.split(' ') if i]
                else:
                    keyword = [i for i in keyword.split(',') if i]
            if re.match(r'^[\u4e00-\u9fa5]+.*$', str(keyword[0])):

                key ='NAME'

            elif re.match(r'^[0-9]+$', str(keyword[0])):
                key = 'IRN'
            else:
                key = 'MRID'
            self.window.sendmsg.emit(len(keyword))
            if self.window.checkBox.isChecked():
                keyword = keyword[0]
                sql = "select irn,mrid,name  from {table} where {key} like '%{keyword}%'"\
                    .format(table=self.table, key=key, keyword=keyword)
            else:
                if key == 'IRN':
                    in_p = ','.join(keyword)
                    if self.window.checkBox_2.isChecked():
                        table ='sys_indicators_data'
                        sql = "select *  from {table} where {key} in ( {in_p})" \
                            .format(table=table, key=key, in_p=in_p)
                    else:
                        sql = "select irn,mrid,name  from {table} where {key} in ( {in_p})" \
                            .format(table=table, key=key, in_p=in_p)
                else:
                    if key == 'MRID' and 'ZB-' not in keyword[0]:
                        keyword = ['ZB-' + key for key in keyword]
                    in_p = ','.join(list(map(lambda x: "'%s'" % x, keyword)))
                    in_p_s = ''.join(list(map(lambda x: "'%s'" % x, keyword)))
                    sql = "select irn,mrid,name from {table} where {key} in ( {in_p}) order by instr({in_p_s},{key})"\
                        .format(table=table, key=key, in_p=in_p,in_p_s=in_p_s)

            cursor = self.get_cursor()
            if cursor:
                result = cursor.execute(sql).fetchall()
                self.window.append_log("执行查询SQL:{}".format(sql))
                return result
            else:
                self.window.append_log("获取不到cursor！")
        else:
            self.window.sendmsg.emit(0)
            self.window.append_log("当前查询参数为空！")

    def run(self):
        keyword = self.window.textEdit.toPlainText()
        fetch_result = self.sql_query(self.table, keyword)
        if fetch_result:
            row_num = len(fetch_result)
            self.window.sendmsg2.emit(row_num)
            column_num = len(fetch_result[0])
            for row in range(row_num):
                for col in range(column_num):
                    temp_data = fetch_result[row][col]
                    data = QStandardItem(str(temp_data))
                    if self.window.checkBox_2.isChecked():
                        self.window.data_model.setItem(row, col, data)
                    else:
                        self.window.model.setItem(row,col,data)
        else:
            self.window.sendmsg2.emit(0)
            self.window.append_log("can't get result,check your sql expression")








