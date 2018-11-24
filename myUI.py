# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\PycharmProjects\handle_oracle\oracle_query.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowTitle("IRN查询")
        MainWindow.resize(857, 664)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setAutoFillBackground(True)
        self.label_3.setTextFormat(QtCore.Qt.PlainText)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 9, 3, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 8, 0, 1, 1)
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setObjectName("textEdit")
        self.gridLayout.addWidget(self.textEdit, 0, 2, 5, 2)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 5, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setAutoFillBackground(True)
        self.label.setStyleSheet("font: 12pt \"黑体\";")
        self.label.setTextFormat(QtCore.Qt.PlainText)
        self.label.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 2)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed,
            QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setMinimumSize(QtCore.QSize(75, 0))
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 0, 4, 1, 1)
        self.tableView = QtWidgets.QTableView(self.centralwidget)
        self.tableView.setObjectName("tableView")
        self.gridLayout.addWidget(self.tableView, 10, 0, 1, 3)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setAutoFillBackground(True)
        self.label_2.setTextFormat(QtCore.Qt.PlainText)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 9, 0, 1, 1)
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setObjectName("checkBox")
        self.gridLayout.addWidget(self.checkBox, 3, 0, 1, 1)
        self.filepath = QtWidgets.QLineEdit(self.centralwidget)
        self.filepath.setObjectName("filepath")
        self.gridLayout.addWidget(self.filepath, 5, 1, 1, 4)
        self.tableView_2 = QtWidgets.QTableView(self.centralwidget)
        self.tableView_2.setObjectName("tableView_2")
        self.gridLayout.addWidget(self.tableView_2, 10, 3, 1, 4)
        self.lcdNumber = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber.setObjectName("lcdNumber")
        self.gridLayout.addWidget(self.lcdNumber, 0, 6, 1, 1)
        self.lcdNumber_2 = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber_2.setObjectName("lcdNumber_2")
        self.gridLayout.addWidget(self.lcdNumber_2, 2, 6, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setAutoFillBackground(True)
        self.label_5.setStyleSheet("font: 14pt \"黑体\";")
        self.label_5.setTextFormat(QtCore.Qt.PlainText)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 2, 5, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setAutoFillBackground(True)
        self.label_4.setStyleSheet("font: 14pt \"黑体\";")
        self.label_4.setTextFormat(QtCore.Qt.PlainText)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 5, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 857, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.pushButton.clicked.connect(MainWindow.sql_query)
        self.pushButton_2.clicked.connect(MainWindow.output_excel)
        self.pushButton_3.clicked.connect(MainWindow.open_file)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_3.setText(_translate("MainWindow", "日志输出"))
        self.pushButton_2.setToolTip(
            _translate(
                "MainWindow",
                "<html><head/><body><p>查询数据库</p></body></html>"))
        self.pushButton_2.setText(_translate("MainWindow", "输出EXCEL"))
        self.pushButton_3.setToolTip(
            _translate(
                "MainWindow",
                "<html><head/><body><p>查询数据库</p></body></html>"))
        self.pushButton_3.setText(_translate("MainWindow", "打开EXCEL"))
        self.label.setText(_translate("MainWindow", "输入查询条件 多行支持\n"
                                      "参数可以是MRID,NAME,IRN"))
        self.pushButton.setToolTip(
            _translate(
                "MainWindow",
                "<html><head/><body><p>查询数据库</p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "查询"))
        self.label_2.setText(_translate("MainWindow", "查询结果输出"))
        self.checkBox.setText(_translate("MainWindow", "模糊查询(只支持单行)"))
        self.label_5.setWhatsThis(
            _translate(
                "MainWindow",
                "<html><head/><body><p><br/></p></body></html>"))
        self.label_5.setText(_translate("MainWindow", "成功返回条数"))
        self.label_4.setText(_translate("MainWindow", "查询条数"))
