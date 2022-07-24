# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Calculator_V02sLiItp.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Calculator_Main(object):
    def setupUi(self, Calculator_Main):
        if not Calculator_Main.objectName():
            Calculator_Main.setObjectName(u"Calculator_Main")
        Calculator_Main.resize(543, 691)
        self.Button_Dot = QPushButton(Calculator_Main)
        self.Button_Dot.setObjectName(u"Button_Dot")
        self.Button_Dot.setGeometry(QRect(170, 520, 75, 75))
        font = QFont()
        font.setFamily(u"Arial")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.Button_Dot.setFont(font)
        self.Button_3 = QPushButton(Calculator_Main)
        self.Button_3.setObjectName(u"Button_3")
        self.Button_3.setGeometry(QRect(300, 420, 75, 75))
        self.Button_3.setFont(font)
        self.Button_5 = QPushButton(Calculator_Main)
        self.Button_5.setObjectName(u"Button_5")
        self.Button_5.setGeometry(QRect(170, 320, 75, 75))
        self.Button_5.setFont(font)
        self.Button_7 = QPushButton(Calculator_Main)
        self.Button_7.setObjectName(u"Button_7")
        self.Button_7.setGeometry(QRect(40, 210, 75, 75))
        self.Button_7.setFont(font)
        self.Button_9 = QPushButton(Calculator_Main)
        self.Button_9.setObjectName(u"Button_9")
        self.Button_9.setGeometry(QRect(300, 210, 75, 75))
        self.Button_9.setFont(font)
        self.Button_0 = QPushButton(Calculator_Main)
        self.Button_0.setObjectName(u"Button_0")
        self.Button_0.setGeometry(QRect(40, 520, 75, 75))
        self.Button_0.setFont(font)
        self.Button_6 = QPushButton(Calculator_Main)
        self.Button_6.setObjectName(u"Button_6")
        self.Button_6.setGeometry(QRect(300, 320, 75, 75))
        self.Button_6.setFont(font)
        self.Button_4 = QPushButton(Calculator_Main)
        self.Button_4.setObjectName(u"Button_4")
        self.Button_4.setGeometry(QRect(40, 320, 75, 75))
        self.Button_4.setFont(font)
        self.Button_2 = QPushButton(Calculator_Main)
        self.Button_2.setObjectName(u"Button_2")
        self.Button_2.setGeometry(QRect(170, 420, 75, 75))
        self.Button_2.setFont(font)
        self.Button_Delete = QPushButton(Calculator_Main)
        self.Button_Delete.setObjectName(u"Button_Delete")
        self.Button_Delete.setGeometry(QRect(300, 520, 75, 75))
        font1 = QFont()
        font1.setFamily(u"Arial")
        font1.setPointSize(20)
        font1.setBold(True)
        font1.setWeight(75)
        self.Button_Delete.setFont(font1)
        self.Button_8 = QPushButton(Calculator_Main)
        self.Button_8.setObjectName(u"Button_8")
        self.Button_8.setGeometry(QRect(170, 210, 75, 75))
        self.Button_8.setFont(font)
        self.Button_1 = QPushButton(Calculator_Main)
        self.Button_1.setObjectName(u"Button_1")
        self.Button_1.setGeometry(QRect(40, 420, 75, 75))
        self.Button_1.setFont(font)
        self.Button_LeftBracket = QPushButton(Calculator_Main)
        self.Button_LeftBracket.setObjectName(u"Button_LeftBracket")
        self.Button_LeftBracket.setGeometry(QRect(170, 100, 75, 75))
        self.Button_LeftBracket.setFont(font)
        self.Button_RightBracket = QPushButton(Calculator_Main)
        self.Button_RightBracket.setObjectName(u"Button_RightBracket")
        self.Button_RightBracket.setGeometry(QRect(300, 100, 75, 75))
        self.Button_RightBracket.setFont(font)
        self.Button_AC = QPushButton(Calculator_Main)
        self.Button_AC.setObjectName(u"Button_AC")
        self.Button_AC.setGeometry(QRect(40, 100, 75, 75))
        self.Button_AC.setFont(font)
        self.Button_Times = QPushButton(Calculator_Main)
        self.Button_Times.setObjectName(u"Button_Times")
        self.Button_Times.setGeometry(QRect(430, 210, 75, 75))
        self.Button_Times.setFont(font)
        self.Button_Divide = QPushButton(Calculator_Main)
        self.Button_Divide.setObjectName(u"Button_Divide")
        self.Button_Divide.setGeometry(QRect(430, 100, 75, 75))
        self.Button_Divide.setFont(font)
        self.Button_Minus = QPushButton(Calculator_Main)
        self.Button_Minus.setObjectName(u"Button_Minus")
        self.Button_Minus.setGeometry(QRect(430, 320, 75, 75))
        self.Button_Minus.setFont(font)
        self.Button_Add = QPushButton(Calculator_Main)
        self.Button_Add.setObjectName(u"Button_Add")
        self.Button_Add.setGeometry(QRect(430, 420, 75, 75))
        self.Button_Add.setFont(font)
        self.Button_Equal = QPushButton(Calculator_Main)
        self.Button_Equal.setObjectName(u"Button_Equal")
        self.Button_Equal.setGeometry(QRect(430, 520, 75, 75))
        self.Button_Equal.setFont(font)
        self.Formula_Text = QTextEdit(Calculator_Main)
        self.Formula_Text.setObjectName(u"Formula_Text")
        self.Formula_Text.setGeometry(QRect(40, 16, 465, 51))
        font2 = QFont()
        font2.setPointSize(22)
        font2.setBold(False)
        font2.setWeight(50)
        self.Formula_Text.setFont(font2)
        self.Formula_Text.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.Formula_Text.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.Result_Text = QTextEdit(Calculator_Main)
        self.Result_Text.setObjectName(u"Result_Text")
        self.Result_Text.setEnabled(False)
        self.Result_Text.setGeometry(QRect(40, 620, 465, 51))
        self.Result_Text.setFont(font2)
        self.Result_Text.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.Result_Text.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.retranslateUi(Calculator_Main)

        QMetaObject.connectSlotsByName(Calculator_Main)
    # setupUi

    def retranslateUi(self, Calculator_Main):
        Calculator_Main.setWindowTitle(QCoreApplication.translate("Calculator_Main", u"Calculator_Main", None))
        self.Button_Dot.setText(QCoreApplication.translate("Calculator_Main", u".", None))
        self.Button_3.setText(QCoreApplication.translate("Calculator_Main", u"3", None))
        self.Button_5.setText(QCoreApplication.translate("Calculator_Main", u"5", None))
        self.Button_7.setText(QCoreApplication.translate("Calculator_Main", u"7", None))
        self.Button_9.setText(QCoreApplication.translate("Calculator_Main", u"9", None))
        self.Button_0.setText(QCoreApplication.translate("Calculator_Main", u"0", None))
        self.Button_6.setText(QCoreApplication.translate("Calculator_Main", u"6", None))
        self.Button_4.setText(QCoreApplication.translate("Calculator_Main", u"4", None))
        self.Button_2.setText(QCoreApplication.translate("Calculator_Main", u"2", None))
        self.Button_Delete.setText(QCoreApplication.translate("Calculator_Main", u"\u232b", None))
        self.Button_8.setText(QCoreApplication.translate("Calculator_Main", u"8", None))
        self.Button_1.setText(QCoreApplication.translate("Calculator_Main", u"1", None))
        self.Button_LeftBracket.setText(QCoreApplication.translate("Calculator_Main", u"(", None))
        self.Button_RightBracket.setText(QCoreApplication.translate("Calculator_Main", u")", None))
        self.Button_AC.setText(QCoreApplication.translate("Calculator_Main", u"AC", None))
        self.Button_Times.setText(QCoreApplication.translate("Calculator_Main", u"\u00d7", None))
        self.Button_Divide.setText(QCoreApplication.translate("Calculator_Main", u"\u00f7", None))
        self.Button_Minus.setText(QCoreApplication.translate("Calculator_Main", u"-", None))
        self.Button_Add.setText(QCoreApplication.translate("Calculator_Main", u"+", None))
        self.Button_Equal.setText(QCoreApplication.translate("Calculator_Main", u"=", None))
        self.Formula_Text.setHtml(QCoreApplication.translate("Calculator_Main", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'PMingLiU'; font-size:22pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1+1</p></body></html>", None))
        self.Result_Text.setHtml(QCoreApplication.translate("Calculator_Main", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'PMingLiU'; font-size:22pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
    # retranslateUi

