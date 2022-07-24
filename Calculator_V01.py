# -*- coding: utf-8 -*-
"""
@author: Willy Fang (方聖瑋)
"""
from UI_Plot import *

print("Loading......")



class AppWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Calculator_Main()
        self.ui.setupUi(self)
        self.setup_control()
        self.show()


    def setup_control(self):
        self.ui.Button_0.clicked.connect(self.Button_0_clicked)
        self.ui.Button_1.clicked.connect(self.Button_1_clicked)
        self.ui.Button_2.clicked.connect(self.Button_2_clicked)
        self.ui.Button_3.clicked.connect(self.Button_3_clicked)
        self.ui.Button_4.clicked.connect(self.Button_4_clicked)
        self.ui.Button_5.clicked.connect(self.Button_5_clicked)
        self.ui.Button_6.clicked.connect(self.Button_6_clicked)
        self.ui.Button_7.clicked.connect(self.Button_7_clicked)
        self.ui.Button_8.clicked.connect(self.Button_8_clicked)
        self.ui.Button_9.clicked.connect(self.Button_9_clicked)
        self.ui.Button_Dot.clicked.connect(self.Button_Dot_clicked)
        self.ui.Button_AC.clicked.connect(self.Button_AC_clicked)
        self.ui.Button_LeftBracket.clicked.connect(self.Button_LeftBracket_clicked)
        self.ui.Button_RightBracket.clicked.connect(self.Button_RightBracket_clicked)
        self.ui.Button_Add.clicked.connect(self.Button_Add_clicked)
        self.ui.Button_Minus.clicked.connect(self.Button_Minus_clicked)
        self.ui.Button_Times.clicked.connect(self.Button_Times_clicked)
        self.ui.Button_Divide.clicked.connect(self.Button_Divide_clicked)
        self.ui.Button_Delete.clicked.connect(self.Button_Delete_clicked)
        self.ui.Button_Equal.clicked.connect(self.Button_Equal_clicked)


    def Button_0_clicked(self):
        self.ui.Formula_Text.setText(self.ui.Formula_Text.toPlainText() + "0")


    def Button_1_clicked(self):
        self.ui.Formula_Text.setText(self.ui.Formula_Text.toPlainText() + "1")


    def Button_2_clicked(self):
        self.ui.Formula_Text.setText(self.ui.Formula_Text.toPlainText() + "2")


    def Button_3_clicked(self):
        self.ui.Formula_Text.setText(self.ui.Formula_Text.toPlainText() + "3")


    def Button_4_clicked(self):
        self.ui.Formula_Text.setText(self.ui.Formula_Text.toPlainText() + "4")


    def Button_5_clicked(self):
        self.ui.Formula_Text.setText(self.ui.Formula_Text.toPlainText() + "5")


    def Button_6_clicked(self):
        self.ui.Formula_Text.setText(self.ui.Formula_Text.toPlainText() + "6")


    def Button_7_clicked(self):
        self.ui.Formula_Text.setText(self.ui.Formula_Text.toPlainText() + "7")


    def Button_8_clicked(self):
        self.ui.Formula_Text.setText(self.ui.Formula_Text.toPlainText() + "8")


    def Button_9_clicked(self):
        self.ui.Formula_Text.setText(self.ui.Formula_Text.toPlainText() + "9")


    def Button_0_clicked(self):
        self.ui.Formula_Text.setText(self.ui.Formula_Text.toPlainText() + "0")


    def Button_Dot_clicked(self):
        self.ui.Formula_Text.setText(self.ui.Formula_Text.toPlainText() + ".")


    def Button_AC_clicked(self):
        self.ui.Formula_Text.setText("")


    def Button_Add_clicked(self):
        self.ui.Formula_Text.setText(self.ui.Formula_Text.toPlainText() + "+")


    def Button_Minus_clicked(self):
        self.ui.Formula_Text.setText(self.ui.Formula_Text.toPlainText() + "-")


    def Button_Times_clicked(self):
        self.ui.Formula_Text.setText(self.ui.Formula_Text.toPlainText() + "×")


    def Button_Divide_clicked(self):
        self.ui.Formula_Text.setText(self.ui.Formula_Text.toPlainText() + "÷")


    def Button_LeftBracket_clicked(self):
        self.ui.Formula_Text.setText(self.ui.Formula_Text.toPlainText() + "(")


    def Button_RightBracket_clicked(self):
        self.ui.Formula_Text.setText(self.ui.Formula_Text.toPlainText() + ")")


    def Button_Delete_clicked(self):
        if self.ui.Formula_Text.toPlainText() == "":
            pass
        else:
            self.ui.Formula_Text.setText(self.ui.Formula_Text.toPlainText()[:-1])


    def Button_Equal_clicked(self):
        math_formula = self.ui.Formula_Text.toPlainText()
        if math_formula == "":
            self.ui.Result_Text.setText("0")
        else:
            math_formula = math_formula.replace("×", "*").replace("÷", "/")
            self.ui.Result_Text.setText(str(eval(math_formula)))







if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    Error_Data_Plot = AppWindow()
    Error_Data_Plot.show()
    sys.exit(app.exec_())