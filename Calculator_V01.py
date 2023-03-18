# -*- coding: utf-8 -*-
"""
@author: Willy Fang
"""
# https://stackoverflow.com/questions/24368329/two-key-shortcuts
# https://doc.qt.io/qt-5/qshortcut.html
# https://zetcode.com/pyqt/qshortcut/
# https://stackoverflow.com/questions/20420072/use-keypressevent-to-catch-enter-or-return
# https://stackoverflow.com/questions/57351709/disable-carriage-return-enter-key-press-in-qplaintextedit
# https://stackoverflow.com/questions/54875284/scrollbar-to-always-show-the-bottom-of-a-qtextbrowser-streamed-text
# https://stackoverflow.com/questions/4939151/how-to-program-scrollbar-to-jump-to-bottom-top-in-case-of-change-in-qplaintexted
# https://forum.qt.io/topic/23321/solved-qplaintextedit-scroll-to-the-bottom
# https://stackoverflow.com/questions/7778726/autoscroll-pyqt-qtextwidget
# https://stackoverflow.com/questions/7280965/how-to-scroll-qplaintextedit-to-top
# https://www.geeksforgeeks.org/python-add-comma-between-numbers/
# https://stackoverflow.com/questions/5180365/add-commas-into-number-string
# https://stackoverflow.com/questions/658763/how-to-suppress-scientific-notation-when-printing-float-values



from UI_Plot import *
import urllib.request

print("Loading......")


class AppWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Calculator()
        self.ui.setupUi(self)
        self.setup_control()
        self.show()

    def setup_control(self):
        self.ui.WinIcon_img = QPixmap()
        url = 'https://raw.githubusercontent.com/LeBronWilly/Calculator_Python/main/Calculator.png'
        img_data = urllib.request.urlopen(url).read()
        self.ui.WinIcon_img.loadFromData(img_data)
        self.ui.WinIcon_img = self.ui.WinIcon_img.scaled(75, 75)
        self.setWindowIcon(QIcon(self.ui.WinIcon_img))
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
        self.ui.Formula_Text.setLineWrapMode(QTextEdit.NoWrap)
        self.ui.Formula_Text.setWordWrapMode(QTextOption.NoWrap)
        self.ui.Formula_Text.setAlignment(Qt.AlignVCenter)
        # self.ui.Formula_Text.moveCursor(QTextCursor.Right)
        QShortcut(QKeySequence("Enter"), self.ui.Button_Equal, self.Button_Equal_clicked)
        QShortcut(QKeySequence("Return"), self.ui.Button_Equal, self.Button_Equal_clicked)
        QShortcut(QKeySequence("Space"), self.ui.Button_0, self.Button_0_clicked)
        # self.ui.Formula_Text.installEventFilter(self)

    # def eventFilter(self, obj, event):
    #     if obj is self.ui.Formula_Text and event.type() == QEvent.KeyPress:
    #         if event.key() in (Qt.Key_Return, Qt.Key_Enter):
    #             self.ui.Button_Equal.clicked.connect(self.Button_Equal_clicked)
    #             return True
    #     return super().eventFilter(obj, event)

    def Button_0_clicked(self):
        self.ui.Formula_Text.setText(self.ui.Formula_Text.toPlainText() + "0")
        self.ui.Formula_Text.horizontalScrollBar().setValue(self.ui.Formula_Text.horizontalScrollBar().maximum())

    def Button_1_clicked(self):
        self.ui.Formula_Text.setText(self.ui.Formula_Text.toPlainText() + "1")
        self.ui.Formula_Text.horizontalScrollBar().setValue(self.ui.Formula_Text.horizontalScrollBar().maximum())

    def Button_2_clicked(self):
        self.ui.Formula_Text.setText(self.ui.Formula_Text.toPlainText() + "2")
        self.ui.Formula_Text.horizontalScrollBar().setValue(self.ui.Formula_Text.horizontalScrollBar().maximum())

    def Button_3_clicked(self):
        self.ui.Formula_Text.setText(self.ui.Formula_Text.toPlainText() + "3")
        self.ui.Formula_Text.horizontalScrollBar().setValue(self.ui.Formula_Text.horizontalScrollBar().maximum())

    def Button_4_clicked(self):
        self.ui.Formula_Text.setText(self.ui.Formula_Text.toPlainText() + "4")
        self.ui.Formula_Text.horizontalScrollBar().setValue(self.ui.Formula_Text.horizontalScrollBar().maximum())

    def Button_5_clicked(self):
        self.ui.Formula_Text.setText(self.ui.Formula_Text.toPlainText() + "5")
        self.ui.Formula_Text.horizontalScrollBar().setValue(self.ui.Formula_Text.horizontalScrollBar().maximum())

    def Button_6_clicked(self):
        self.ui.Formula_Text.setText(self.ui.Formula_Text.toPlainText() + "6")
        self.ui.Formula_Text.horizontalScrollBar().setValue(self.ui.Formula_Text.horizontalScrollBar().maximum())

    def Button_7_clicked(self):
        self.ui.Formula_Text.setText(self.ui.Formula_Text.toPlainText() + "7")
        self.ui.Formula_Text.horizontalScrollBar().setValue(self.ui.Formula_Text.horizontalScrollBar().maximum())

    def Button_8_clicked(self):
        self.ui.Formula_Text.setText(self.ui.Formula_Text.toPlainText() + "8")
        self.ui.Formula_Text.horizontalScrollBar().setValue(self.ui.Formula_Text.horizontalScrollBar().maximum())

    def Button_9_clicked(self):
        self.ui.Formula_Text.setText(self.ui.Formula_Text.toPlainText() + "9")
        self.ui.Formula_Text.horizontalScrollBar().setValue(self.ui.Formula_Text.horizontalScrollBar().maximum())

    def Button_Dot_clicked(self):
        self.ui.Formula_Text.setText(self.ui.Formula_Text.toPlainText() + ".")
        self.ui.Formula_Text.horizontalScrollBar().setValue(self.ui.Formula_Text.horizontalScrollBar().maximum())

    def Button_AC_clicked(self):
        self.ui.Formula_Text.setText("")
        self.ui.Formula_Text.horizontalScrollBar().setValue(self.ui.Formula_Text.horizontalScrollBar().maximum())

    def Button_Add_clicked(self):
        self.ui.Formula_Text.setText(self.ui.Formula_Text.toPlainText() + "+")
        self.ui.Formula_Text.horizontalScrollBar().setValue(self.ui.Formula_Text.horizontalScrollBar().maximum())

    def Button_Minus_clicked(self):
        self.ui.Formula_Text.setText(self.ui.Formula_Text.toPlainText() + "-")
        self.ui.Formula_Text.horizontalScrollBar().setValue(self.ui.Formula_Text.horizontalScrollBar().maximum())

    def Button_Times_clicked(self):
        self.ui.Formula_Text.setText(self.ui.Formula_Text.toPlainText() + "×")
        self.ui.Formula_Text.horizontalScrollBar().setValue(self.ui.Formula_Text.horizontalScrollBar().maximum())

    def Button_Divide_clicked(self):
        self.ui.Formula_Text.setText(self.ui.Formula_Text.toPlainText() + "÷")
        self.ui.Formula_Text.horizontalScrollBar().setValue(self.ui.Formula_Text.horizontalScrollBar().maximum())

    def Button_LeftBracket_clicked(self):
        self.ui.Formula_Text.setText(self.ui.Formula_Text.toPlainText() + "(")
        self.ui.Formula_Text.horizontalScrollBar().setValue(self.ui.Formula_Text.horizontalScrollBar().maximum())

    def Button_RightBracket_clicked(self):
        self.ui.Formula_Text.setText(self.ui.Formula_Text.toPlainText() + ")")
        self.ui.Formula_Text.horizontalScrollBar().setValue(self.ui.Formula_Text.horizontalScrollBar().maximum())

    def Button_Delete_clicked(self):
        if self.ui.Formula_Text.toPlainText() == "":
            pass
        else:
            self.ui.Formula_Text.setText(self.ui.Formula_Text.toPlainText()[:-1])
        self.ui.Formula_Text.horizontalScrollBar().setValue(self.ui.Formula_Text.horizontalScrollBar().maximum())

    def Button_Equal_clicked(self):
        math_formula = self.ui.Formula_Text.toPlainText()
        try:
            if math_formula == "":
                self.ui.Result_Text.setText("0")
            else:
                math_formula = math_formula.replace("×", "*").replace("÷", "/")
                ans = eval(math_formula)
                if type(ans) == float:
                    ans = '{:,.8f}'.format(ans).rstrip("0")
                else:
                    ans = '{:,}'.format(ans)
                self.ui.Result_Text.setText(ans)
                # self.ui.Result_Text.setText('{:,}'.format(ans))
        except ZeroDivisionError:
            self.ui.Result_Text.setText("You can not divide by zero!")
            print("You can not divide by zero!")
        except:
            self.ui.Result_Text.setText("There's an error in the formula!")
            print("There's an error in the formula!")
        self.ui.Formula_Text.horizontalScrollBar().setValue(self.ui.Formula_Text.horizontalScrollBar().maximum())


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    Calculator_Tool = AppWindow()
    Calculator_Tool.show()
    sys.exit(app.exec_())
