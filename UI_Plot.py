# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Tool_UI_Display_Plot_V02EaQyBR.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Plot_Data_Display(object):
    def setupUi(self, Plot_Data_Display):
        if not Plot_Data_Display.objectName():
            Plot_Data_Display.setObjectName(u"Plot_Data_Display")
        Plot_Data_Display.resize(1857, 908)
        self.pushButton_2 = QPushButton(Plot_Data_Display)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setEnabled(True)
        self.pushButton_2.setGeometry(QRect(220, 810, 181, 41))
        font = QFont()
        font.setFamily(u"Arial")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.label_7 = QLabel(Plot_Data_Display)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(10, 160, 200, 31))
        font1 = QFont()
        font1.setFamily(u"Arial")
        font1.setPointSize(16)
        font1.setBold(True)
        font1.setWeight(75)
        self.label_7.setFont(font1)
        self.label_7.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)
        self.label_4 = QLabel(Plot_Data_Display)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, 300, 200, 31))
        self.label_4.setFont(font1)
        self.label_4.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)
        self.label_6 = QLabel(Plot_Data_Display)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(10, 870, 411, 31))
        font2 = QFont()
        font2.setFamily(u"Arial")
        font2.setPointSize(10)
        font2.setBold(True)
        font2.setItalic(True)
        font2.setWeight(75)
        self.label_6.setFont(font2)
        self.label_6.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)
        self.label_3 = QLabel(Plot_Data_Display)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 230, 200, 31))
        self.label_3.setFont(font1)
        self.label_3.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)
        self.plainTextEdit_3 = QPlainTextEdit(Plot_Data_Display)
        self.plainTextEdit_3.setObjectName(u"plainTextEdit_3")
        self.plainTextEdit_3.setEnabled(False)
        self.plainTextEdit_3.setGeometry(QRect(20, 790, 181, 31))
        font3 = QFont()
        font3.setFamily(u"Arial")
        font3.setPointSize(14)
        font3.setKerning(True)
        self.plainTextEdit_3.setFont(font3)
        self.plainTextEdit_3.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.plainTextEdit_3.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.comboBox_4 = QComboBox(Plot_Data_Display)
        self.comboBox_4.addItem("")
        self.comboBox_4.setObjectName(u"comboBox_4")
        self.comboBox_4.setGeometry(QRect(200, 300, 201, 31))
        font4 = QFont()
        font4.setFamily(u"Arial")
        font4.setPointSize(14)
        self.comboBox_4.setFont(font4)
        self.label_1 = QLabel(Plot_Data_Display)
        self.label_1.setObjectName(u"label_1")
        self.label_1.setGeometry(QRect(10, 90, 200, 31))
        self.label_1.setFont(font1)
        self.label_1.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)
        self.pushButton_1 = QPushButton(Plot_Data_Display)
        self.pushButton_1.setObjectName(u"pushButton_1")
        self.pushButton_1.setEnabled(False)
        self.pushButton_1.setGeometry(QRect(220, 750, 181, 41))
        self.pushButton_1.setFont(font)
        self.comboBox_1 = QComboBox(Plot_Data_Display)
        self.comboBox_1.addItem("")
        self.comboBox_1.setObjectName(u"comboBox_1")
        self.comboBox_1.setGeometry(QRect(200, 90, 201, 31))
        self.comboBox_1.setFont(font4)
        self.label = QLabel(Plot_Data_Display)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 10, 391, 51))
        self.label.setPixmap(QPixmap(u"../../../\u4e0b\u8f09/118489.png"))
        self.label.setAlignment(Qt.AlignCenter)
        self.comboBox_3 = QComboBox(Plot_Data_Display)
        self.comboBox_3.addItem("")
        self.comboBox_3.setObjectName(u"comboBox_3")
        self.comboBox_3.setGeometry(QRect(200, 230, 201, 31))
        self.comboBox_3.setFont(font4)
        self.label_5 = QLabel(Plot_Data_Display)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(20, 760, 191, 31))
        font5 = QFont()
        font5.setFamily(u"Arial")
        font5.setPointSize(10)
        font5.setBold(True)
        font5.setWeight(75)
        self.label_5.setFont(font5)
        self.label_5.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)
        self.comboBox_2 = QComboBox(Plot_Data_Display)
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setGeometry(QRect(200, 160, 201, 31))
        self.comboBox_2.setFont(font4)
        self.graphicsView_1 = QGraphicsView(Plot_Data_Display)
        self.graphicsView_1.setObjectName(u"graphicsView_1")
        self.graphicsView_1.setGeometry(QRect(1010, 20, 831, 831))
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.graphicsView_1.sizePolicy().hasHeightForWidth())
        self.graphicsView_1.setSizePolicy(sizePolicy)
        self.tableWidget = QTableWidget(Plot_Data_Display)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(410, 20, 591, 831))
        font6 = QFont()
        font6.setPointSize(8)
        self.tableWidget.setFont(font6)
        self.tableWidget.setAlternatingRowColors(False)
        self.label_9 = QLabel(Plot_Data_Display)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(1010, 860, 831, 31))
        font7 = QFont()
        font7.setFamily(u"Arial")
        font7.setPointSize(18)
        font7.setBold(True)
        font7.setWeight(75)
        self.label_9.setFont(font7)
        self.label_9.setAlignment(Qt.AlignCenter)
        self.label_8 = QLabel(Plot_Data_Display)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(409, 860, 591, 31))
        self.label_8.setFont(font7)
        self.label_8.setAlignment(Qt.AlignCenter)
        self.pushButton_3 = QPushButton(Plot_Data_Display)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setEnabled(True)
        self.pushButton_3.setGeometry(QRect(820, 860, 101, 31))
        font8 = QFont()
        font8.setFamily(u"Arial")
        font8.setPointSize(12)
        font8.setBold(True)
        font8.setWeight(75)
        self.pushButton_3.setFont(font8)
        self.pushButton_4 = QPushButton(Plot_Data_Display)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setEnabled(True)
        self.pushButton_4.setGeometry(QRect(1540, 860, 111, 31))
        self.pushButton_4.setFont(font8)
        self.label_10 = QLabel(Plot_Data_Display)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(10, 370, 200, 31))
        self.label_10.setFont(font1)
        self.label_10.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)
        self.comboBox_5 = QComboBox(Plot_Data_Display)
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.setObjectName(u"comboBox_5")
        self.comboBox_5.setGeometry(QRect(200, 370, 201, 31))
        self.comboBox_5.setFont(font4)
        self.label_11 = QLabel(Plot_Data_Display)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(10, 430, 200, 31))
        self.label_11.setFont(font5)
        self.label_11.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)
        self.plainTextEdit_4 = QPlainTextEdit(Plot_Data_Display)
        self.plainTextEdit_4.setObjectName(u"plainTextEdit_4")
        self.plainTextEdit_4.setEnabled(True)
        self.plainTextEdit_4.setGeometry(QRect(10, 460, 391, 271))
        font9 = QFont()
        font9.setFamily(u"Arial")
        font9.setPointSize(14)
        font9.setBold(True)
        font9.setWeight(75)
        font9.setKerning(True)
        self.plainTextEdit_4.setFont(font9)
        self.plainTextEdit_4.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.plainTextEdit_4.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)

        self.retranslateUi(Plot_Data_Display)

        QMetaObject.connectSlotsByName(Plot_Data_Display)
    # setupUi

    def retranslateUi(self, Plot_Data_Display):
        Plot_Data_Display.setWindowTitle(QCoreApplication.translate("Plot_Data_Display", u"Plot_Data_Display", None))
        self.pushButton_2.setText(QCoreApplication.translate("Plot_Data_Display", u"Refresh", None))
        self.label_7.setText(QCoreApplication.translate("Plot_Data_Display", u"Errors\uff1a", None))
        self.label_4.setText(QCoreApplication.translate("Plot_Data_Display", u"Data\uff1a", None))
        self.label_6.setText(QCoreApplication.translate("Plot_Data_Display", u"Developed by Willy Fang", None))
        self.label_3.setText(QCoreApplication.translate("Plot_Data_Display", u"Dates\uff1a", None))
        self.plainTextEdit_3.setPlainText(QCoreApplication.translate("Plot_Data_Display", u"Ready", None))
        self.comboBox_4.setItemText(0, QCoreApplication.translate("Plot_Data_Display", u"\u8acb\u9078\u53d6\u8cc7\u6599", None))

        self.label_1.setText(QCoreApplication.translate("Plot_Data_Display", u"SC_nums\uff1a", None))
        self.pushButton_1.setText(QCoreApplication.translate("Plot_Data_Display", u"Show", None))
        self.comboBox_1.setItemText(0, QCoreApplication.translate("Plot_Data_Display", u"\u8acb\u9078\u53d6\u8eca\u865f", None))

        self.label.setText("")
        self.comboBox_3.setItemText(0, QCoreApplication.translate("Plot_Data_Display", u"\u8acb\u9078\u53d6\u65e5\u671f", None))

        self.label_5.setText(QCoreApplication.translate("Plot_Data_Display", u"\u7a0b\u5f0f\u72c0\u614b\u63d0\u793a\uff1a", None))
        self.comboBox_2.setItemText(0, QCoreApplication.translate("Plot_Data_Display", u"\u8acb\u9078\u53d6\u7570\u5e38", None))

        self.label_9.setText(QCoreApplication.translate("Plot_Data_Display", u"Screen 2", None))
        self.label_8.setText(QCoreApplication.translate("Plot_Data_Display", u"Screen 1", None))
        self.pushButton_3.setText(QCoreApplication.translate("Plot_Data_Display", u"Clear", None))
        self.pushButton_4.setText(QCoreApplication.translate("Plot_Data_Display", u"Clear", None))
        self.label_10.setText(QCoreApplication.translate("Plot_Data_Display", u"Map Mode\uff1a", None))
        self.comboBox_5.setItemText(0, QCoreApplication.translate("Plot_Data_Display", u"Shelf", None))
        self.comboBox_5.setItemText(1, QCoreApplication.translate("Plot_Data_Display", u"Encoder", None))

        self.label_11.setText(QCoreApplication.translate("Plot_Data_Display", u"\u7570\u5e38\u4f4d\u7f6e\uff08X , Y\uff09\uff1a", None))
        self.plainTextEdit_4.setPlainText("")
    # retranslateUi

