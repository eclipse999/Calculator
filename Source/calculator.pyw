import sys
from PyQt5 import QtWidgets, QtGui
from ui_v3 import Ui_MainWindow


class Myapp(QtWidgets.QMainWindow, Ui_MainWindow):
    waitting_operation = True
    waitting_clear = True
    numssofar = 0.0
    pmsender = ""
    md_numsofar = 0.0
    mdsender = ""
    inmemory = 0.0
    theme = True

    def __init__(self, parent=None):
        super().__init__()
        self.setupUi(self)

        # 按鈕元件清單
        nums = [self.zero, self.one, self.two, self.three, self.four,
                self.five, self.six, self.seven, self.eight, self.nine]

        plus_minus = [self.plus, self.minus]

        multiply_divide = [self.multiply, self.divide]

        # 連結按鈕
        for i in nums:
            i.clicked.connect(self.number_clicked)

        for i in plus_minus:
            i.clicked.connect(self.pm_operator_clicked)

        for i in multiply_divide:
            i.clicked.connect(self.md_operator_clicked)

        self.equal.clicked.connect(self.equal_clicked)
        self.point.clicked.connect(self.point_clicked)
        self.pos_neg.clicked.connect(self.switch)
        self.pa.clicked.connect(self.percent)
        self.ce.clicked.connect(self.clear_entry)
        self.c.clicked.connect(self.clearall)
        self.m_minus.clicked.connect(self.memoryminus)
        self.m_plus.clicked.connect(self.memoryplus)
        self.mr.clicked.connect(self.memoryshow)
        self.mc.clicked.connect(self.memoryclear)
        self.switch2b.clicked.connect(self.switchcolor)
        self.doc.clicked.connect(self.manual)
        self.back.clicked.connect(self.backspace)

    def number_clicked(self):

        sender = self.sender()
        value = int(sender.text())

        if self.label.text() == "0" and value == 0:
            return

        if self.waitting_operation:
            self.label.clear()
            self.waitting_operation = False

        if not self.waitting_clear:
            self.label.clear()
            self.waitting_clear = True

        self.label.setText(self.label.text()+str(value))

    def pm_operator_clicked(self):
        sender = self.sender()
        whatop = sender.text()

        try:
            num = float(self.label.text())

            if self.mdsender:
                if not self.keisan(num, self.mdsender):
                    self.error()
                    return

                self.label.setText(f"{self.md_numsofar:.15g}")
                num = self.md_numsofar
                self.md_numsofar = 0.0
                self.mdsender = ""

            if self.pmsender:
                if not self.keisan(num, self.pmsender):
                    self.error()
                    return

                self.label.setText(f"{self.numssofar:.15g}")
            else:
                self.numssofar = num

            self.pmsender = whatop
            self.waitting_operation = True

        except ValueError:
            pass

    def md_operator_clicked(self):
        sender = self.sender()
        whatop = sender.text()

        try:
            num = float(self.label.text())

            if self.mdsender:
                if not self.keisan(num, self.mdsender):
                    self.error()
                    return

                self.label.setText(f"{self.md_numsofar:.15g}")
            else:
                self.md_numsofar = num

            self.mdsender = whatop
            self.waitting_operation = True

        except ValueError:
            pass

    def equal_clicked(self):
        try:
            num = float(self.label.text())

            if self.mdsender:
                if not self.keisan(num, self.mdsender):
                    self.error()
                    return
                num = self.md_numsofar
                self.md_numsofar = 0.0
                self.mdsender = ""
            if self.pmsender:
                if not self.keisan(num, self.pmsender):
                    self.error()
                    return
                self.pmsender = ""
            else:
                self.numssofar = num

            self.label.setText(f"{self.numssofar:.15g}")
            self.numssofar = 0.0
            self.waitting_operation = True
        except ValueError:
            pass

    def keisan(self, num, whatop):
        if whatop == "+":
            self.numssofar += num
        elif whatop == "-":
            self.numssofar -= num

        elif whatop == "x":
            self.md_numsofar *= num
        elif whatop == "÷":
            if num == 0.0:
                return False

            self.md_numsofar /= num

        return True

    def error(self):
        self.clearall()
        self.label.setText(u"操作有誤,請重新確認")

    def point_clicked(self):
        if self.waitting_operation:
            self.label.setText("0")
        if "." not in self.label.text():
            self.label.setText(self.label.text()+".")
        self.waitting_operation = False
        self.waitting_clear = True

    def switch(self):
        text = self.label.text()
        try:
            value = float(text)

            if value > 0.0:
                text = "-" + text
            elif value < 0.0:
                text = text[1:]

            self.label.setText(text)

        except ValueError:
            pass

    def clearall(self):
        self.numssofar = 0.0
        self.md_numsofar = 0.0
        self.pmsender = ""
        self.mdsender = ""
        self.label.setText("0")
        self.waitingFornum = True
        self.waitting_clear = False

    def clear_entry(self):
        self.label.clear()
        self.label.setText("0")
        self.waitting_clear = False

    def percent(self):
        text = self.label.text()
        try:
            value = float(text)

            value = value * 0.01

            self.label.setText(f"{value:.15g}")

        except ValueError:
            pass

    def memoryplus(self):
        self.equal_clicked()
        try:
            self.inmemory += float(self.label.text())

            if self.label.text() != "0":
                self.label_2.setText("M")
                if self.inmemory == 0:
                    self.memoryclear()
        except ValueError:
            pass

    def memoryminus(self):
        self.equal_clicked()
        try:
            self.inmemory -= float(self.label.text())

            if self.label.text() != "0":
                self.label_2.setText("M")
                if self.inmemory == 0:
                    self.memoryclear()
        except ValueError:
            pass

    def memoryshow(self):
        self.label.setText(f"{self.inmemory:.15g}")
        self.waitting_operation = True

    def memoryclear(self):
        self.label.setText("0")
        self.label_2.setText("")
        self.inmemory = 0.0

    def backspace(self):
        text = self.label.text()
        if not len(text) <= 1:
            self.label.setText(text[:-1])
        else:
            self.label.setText("0")
            self.waitting_clear = False

    def manual(self):
        self.manualbox = QtWidgets.QMessageBox()
        self.manualbox.setWindowTitle(u"使用說明")
        self.manualbox.setInformativeText(
            u"本計算機能進行基本四則運算\n計算模式遵循先乘除後加減原則\nM+：將當前數值,累加進記憶位置當中\nM-：總數扣除當前數值\nMC：將記憶的數值清空\nMR：將至今計算的數值呈現出來\n數字7上的←可將畫面上的數字退回一位")
        self.manualbox.exec_()

    def switchcolor(self):
        nums = [self.zero, self.one, self.two, self.three, self.four,
                self.five, self.six, self.seven, self.eight, self.nine]
        origin = [self.equal, self.plus,
                  self.minus, self.multiply, self.divide]

        other = [self.pa, self.ce, self.c, self.pos_neg, self.point, self.mc, self.mr,
                 self.m_plus, self.m_minus]

        if self.theme:
            self.setStyleSheet("")

            for i in other:
                i.setStyleSheet("QPushButton {\n"
                                "  background-color: rgb(215, 215, 215);\n"
                                "  border: 1px solid gray;\n"
                                "}\n"
                                "QPushButton:pressed {\n"
                                "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
                                "                                      stop: 0 #BEBEBE, stop: 1 #D7D7D7);\n"
                                "}")

            self.switch2b.setStyleSheet("QPushButton {\n"
                                        "  border: 1px solid gray;\n"
                                        "}\n"
                                        "QPushButton:pressed {\n"
                                        "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
                                        "                                      stop: 0 #BEBEBE, stop: 1 #D7D7D7);\n"
                                        "}")
            self.doc.setStyleSheet("QPushButton {\n"
                                   "  border: 1px solid gray;\n"
                                   "}\n"
                                   "QPushButton:pressed {\n"
                                   "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
                                   "                                      stop: 0 #BEBEBE, stop: 1 #D7D7D7);\n"
                                   "}")

            self.label.setStyleSheet("QLabel {\n"
                                     "  qproperty-alignment: \'AlignVCenter | AlignRight\';\n"
                                     "  border: 1px solid gray;\n"
                                     "}\n"
                                     "\n"
                                     "background-color : white;")
            self.back.setStyleSheet(
                "QPushButton {\n"
                "border: 1px solid gray;\n"
                "}\n"
                "QPushButton:pressed {\n"
                "background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
                "stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
                "}")
            for i in nums:
                i.setStyleSheet(
                    "QPushButton {\n"
                    "border: 1px solid gray;\n"
                    "}\n"
                    "QPushButton:pressed {\n"
                    "background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
                    "stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
                    "}")

            for i in origin:
                i.setStyleSheet("QPushButton {\n"
                                "  background-color: rgb(255, 151, 57);\n"
                                "  color: white; \n"
                                "  border: 1px solid gray;\n"
                                "}\n"
                                "\n"
                                "QPushButton:pressed {\n"
                                "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
                                "                                      stop: 0 #FF7832, stop: 1 #FF9739);\n"
                                "}")
            self.label_2.setStyleSheet("color:black")
            self.theme = False

        else:
            self.setStyleSheet("background-color: rgb(0, 0, 0)")

            for i in other:
                i.setStyleSheet("QPushButton {\n"
                                "  color: rgb(255, 255, 255);\n"
                                "    background-color: rgb(30, 30, 30);\n"
                                "  border: 1px solid gray;\n"
                                "}\n"
                                "QPushButton:pressed {\n"
                                "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
                                "                                      stop: 0 #1E1E1E, stop: 1 #4a4a4a);\n"
                                "}")

            self.switch2b.setStyleSheet("QPushButton {\n"
                                        "   border: 1px solid gray;\n"
                                        "    color: rgb(255, 255, 255);\n"
                                        "\n"
                                        "}\n"
                                        "QPushButton:pressed {\n"
                                        "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
                                        "                                      stop: 0 #000000, stop: 1 #323232);\n"
                                        "}")

            self.label.setStyleSheet("QLabel {\n"
                                     "  qproperty-alignment: \'AlignVCenter | AlignRight\';\n"
                                     "  border: 1px solid gray;\n"
                                     "    color: rgb(255, 255, 255);\n"
                                     "}\n"
                                     "")

            for i in nums:
                i.setStyleSheet("QPushButton {\n"
                                "   border: 1px solid gray;\n"
                                "    color: rgb(255, 255, 255);\n"
                                "\n"
                                "}\n"
                                "QPushButton:pressed {\n"
                                "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
                                "                                      stop: 0 #000000, stop: 1 #323232);\n"
                                "}")

            for i in origin:
                i.setStyleSheet("QPushButton {\n"
                                "  background-color: #003148;\n"
                                "  color: white; \n"
                                "  border: 1px solid gray;\n"
                                "}\n"
                                "\n"
                                "QPushButton:pressed {\n"
                                "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
                                "                                      stop: 0 #003148, stop: 1 #004667);\n"
                                "}")
            self.label_2.setStyleSheet("color: rgb(255, 255, 255)")
            self.doc.setStyleSheet("QPushButton {\n"
                                   "   border: 1px solid gray;\n"
                                   "    color: rgb(255, 255, 255);\n"
                                   "\n"
                                   "}\n"
                                   "QPushButton:pressed {\n"
                                   "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
                                   "                                      stop: 0 #000000, stop: 1 #323232);\n"
                                   "}")
            self.back.setStyleSheet("QPushButton {\n"
                                    "   border: 1px solid gray;\n"
                                    "    color: rgb(255, 255, 255);\n"
                                    "\n"
                                    "}\n"
                                    "QPushButton:pressed {\n"
                                    "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
                                    "                                      stop: 0 #000000, stop: 1 #323232);\n"
                                    "}")
            self.theme = True


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    w = Myapp()
    w.show()
    sys.exit(app.exec_())
