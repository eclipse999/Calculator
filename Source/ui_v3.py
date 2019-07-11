# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_v3.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(281, 441)
        MainWindow.setMinimumSize(QtCore.QSize(281, 441))
        MainWindow.setMaximumSize(QtCore.QSize(281, 441))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/cal_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.seven = QtWidgets.QPushButton(self.centralwidget)
        self.seven.setGeometry(QtCore.QRect(0, 200, 71, 61))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.seven.setFont(font)
        self.seven.setStyleSheet("QPushButton {\n"
"   border: 1px solid gray;\n"
"    color: rgb(255, 255, 255);\n"
"\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #000000, stop: 1 #323232);\n"
"}")
        self.seven.setObjectName("seven")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 20, 281, 61))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setStyleSheet("QLabel {\n"
"  qproperty-alignment: \'AlignVCenter | AlignRight\';\n"
"  border: 1px solid gray;\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.five = QtWidgets.QPushButton(self.centralwidget)
        self.five.setGeometry(QtCore.QRect(70, 260, 71, 61))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.five.setFont(font)
        self.five.setStyleSheet("QPushButton {\n"
"   border: 1px solid gray;\n"
"    color: rgb(255, 255, 255);\n"
"\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #000000, stop: 1 #323232);\n"
"}")
        self.five.setObjectName("five")
        self.eight = QtWidgets.QPushButton(self.centralwidget)
        self.eight.setGeometry(QtCore.QRect(70, 200, 71, 61))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.eight.setFont(font)
        self.eight.setStyleSheet("QPushButton {\n"
"   border: 1px solid gray;\n"
"    color: rgb(255, 255, 255);\n"
"\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #000000, stop: 1 #323232);\n"
"}")
        self.eight.setObjectName("eight")
        self.pos_neg = QtWidgets.QPushButton(self.centralwidget)
        self.pos_neg.setGeometry(QtCore.QRect(140, 380, 71, 61))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.pos_neg.setFont(font)
        self.pos_neg.setStyleSheet("QPushButton {\n"
"  color: rgb(255, 255, 255);\n"
"    background-color: rgb(30, 30, 30);\n"
"  border: 1px solid gray;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #1E1E1E, stop: 1 #4a4a4a);\n"
"}")
        self.pos_neg.setObjectName("pos_neg")
        self.six = QtWidgets.QPushButton(self.centralwidget)
        self.six.setGeometry(QtCore.QRect(140, 260, 71, 61))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.six.setFont(font)
        self.six.setStyleSheet("QPushButton {\n"
"   border: 1px solid gray;\n"
"    color: rgb(255, 255, 255);\n"
"\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #000000, stop: 1 #323232);\n"
"}")
        self.six.setObjectName("six")
        self.four = QtWidgets.QPushButton(self.centralwidget)
        self.four.setGeometry(QtCore.QRect(0, 260, 71, 61))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.four.setFont(font)
        self.four.setStyleSheet("QPushButton {\n"
"   border: 1px solid gray;\n"
"    color: rgb(255, 255, 255);\n"
"\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #000000, stop: 1 #323232);\n"
"}")
        self.four.setObjectName("four")
        self.point = QtWidgets.QPushButton(self.centralwidget)
        self.point.setGeometry(QtCore.QRect(0, 380, 71, 61))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.point.setFont(font)
        self.point.setStyleSheet("QPushButton {\n"
"  color: rgb(255, 255, 255);\n"
"    background-color: rgb(30, 30, 30);\n"
"  border: 1px solid gray;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #1E1E1E, stop: 1 #4a4a4a);\n"
"}")
        self.point.setObjectName("point")
        self.zero = QtWidgets.QPushButton(self.centralwidget)
        self.zero.setGeometry(QtCore.QRect(70, 380, 71, 61))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.zero.setFont(font)
        self.zero.setStyleSheet("QPushButton {\n"
"   border: 1px solid gray;\n"
"    color: rgb(255, 255, 255);\n"
"\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #000000, stop: 1 #323232);\n"
"}")
        self.zero.setObjectName("zero")
        self.one = QtWidgets.QPushButton(self.centralwidget)
        self.one.setGeometry(QtCore.QRect(0, 320, 71, 61))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.one.setFont(font)
        self.one.setStyleSheet("QPushButton {\n"
"   border: 1px solid gray;\n"
"    color: rgb(255, 255, 255);\n"
"\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #000000, stop: 1 #323232);\n"
"}")
        self.one.setObjectName("one")
        self.equal = QtWidgets.QPushButton(self.centralwidget)
        self.equal.setGeometry(QtCore.QRect(210, 380, 71, 61))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.equal.setFont(font)
        self.equal.setStyleSheet("QPushButton {\n"
"  background-color: #003148;\n"
"  color: white; \n"
"  border: 1px solid gray;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #003148, stop: 1 #004667);\n"
"}")
        self.equal.setObjectName("equal")
        self.nine = QtWidgets.QPushButton(self.centralwidget)
        self.nine.setGeometry(QtCore.QRect(140, 200, 71, 61))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.nine.setFont(font)
        self.nine.setStyleSheet("QPushButton {\n"
"   border: 1px solid gray;\n"
"    color: rgb(255, 255, 255);\n"
"\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #000000, stop: 1 #323232);\n"
"}")
        self.nine.setObjectName("nine")
        self.divide = QtWidgets.QPushButton(self.centralwidget)
        self.divide.setGeometry(QtCore.QRect(210, 140, 71, 61))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.divide.setFont(font)
        self.divide.setStyleSheet("QPushButton {\n"
"  background-color: #003148;\n"
"  color: white; \n"
"  border: 1px solid gray;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #003148, stop: 1 #004667);\n"
"}")
        self.divide.setObjectName("divide")
        self.minus = QtWidgets.QPushButton(self.centralwidget)
        self.minus.setGeometry(QtCore.QRect(210, 260, 71, 61))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.minus.setFont(font)
        self.minus.setStyleSheet("QPushButton {\n"
"  background-color: #003148;\n"
"  color: white; \n"
"  border: 1px solid gray;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #003148, stop: 1 #004667);\n"
"}")
        self.minus.setObjectName("minus")
        self.multiply = QtWidgets.QPushButton(self.centralwidget)
        self.multiply.setGeometry(QtCore.QRect(210, 200, 71, 61))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.multiply.setFont(font)
        self.multiply.setStyleSheet("QPushButton {\n"
"  background-color: #003148;\n"
"  color: white; \n"
"  border: 1px solid gray;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #003148, stop: 1 #004667);\n"
"}")
        self.multiply.setObjectName("multiply")
        self.plus = QtWidgets.QPushButton(self.centralwidget)
        self.plus.setGeometry(QtCore.QRect(210, 320, 71, 61))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.plus.setFont(font)
        self.plus.setStyleSheet("QPushButton {\n"
"  background-color: #003148;\n"
"  color: white; \n"
"  border: 1px solid gray;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #003148, stop: 1 #004667);\n"
"}")
        self.plus.setObjectName("plus")
        self.m_plus = QtWidgets.QPushButton(self.centralwidget)
        self.m_plus.setGeometry(QtCore.QRect(140, 80, 71, 61))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.m_plus.setFont(font)
        self.m_plus.setStyleSheet("QPushButton {\n"
"  color: rgb(255, 255, 255);\n"
"    background-color: rgb(30, 30, 30);\n"
"  border: 1px solid gray;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #1E1E1E, stop: 1 #4a4a4a);\n"
"}")
        self.m_plus.setObjectName("m_plus")
        self.c = QtWidgets.QPushButton(self.centralwidget)
        self.c.setGeometry(QtCore.QRect(0, 140, 71, 61))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.c.setFont(font)
        self.c.setStyleSheet("QPushButton {\n"
"  color: rgb(255, 255, 255);\n"
"    background-color: rgb(30, 30, 30);\n"
"  border: 1px solid gray;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #1E1E1E, stop: 1 #4a4a4a);\n"
"}")
        self.c.setObjectName("c")
        self.ce = QtWidgets.QPushButton(self.centralwidget)
        self.ce.setGeometry(QtCore.QRect(70, 140, 71, 61))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.ce.setFont(font)
        self.ce.setStyleSheet("QPushButton {\n"
"  color: rgb(255, 255, 255);\n"
"    background-color: rgb(30, 30, 30);\n"
"  border: 1px solid gray;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #1E1E1E, stop: 1 #4a4a4a);\n"
"}")
        self.ce.setObjectName("ce")
        self.mr = QtWidgets.QPushButton(self.centralwidget)
        self.mr.setGeometry(QtCore.QRect(70, 80, 71, 61))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.mr.setFont(font)
        self.mr.setStyleSheet("QPushButton {\n"
"  color: rgb(255, 255, 255);\n"
"    background-color: rgb(30, 30, 30);\n"
"  border: 1px solid gray;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #1E1E1E, stop: 1 #4a4a4a);\n"
"}")
        self.mr.setObjectName("mr")
        self.two = QtWidgets.QPushButton(self.centralwidget)
        self.two.setGeometry(QtCore.QRect(70, 320, 71, 61))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.two.setFont(font)
        self.two.setStyleSheet("QPushButton {\n"
"   border: 1px solid gray;\n"
"    color: rgb(255, 255, 255);\n"
"\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #000000, stop: 1 #323232);\n"
"}")
        self.two.setObjectName("two")
        self.three = QtWidgets.QPushButton(self.centralwidget)
        self.three.setGeometry(QtCore.QRect(140, 320, 71, 61))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.three.setFont(font)
        self.three.setStyleSheet("QPushButton {\n"
"   border: 1px solid gray;\n"
"    color: rgb(255, 255, 255);\n"
"\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #000000, stop: 1 #323232);\n"
"}")
        self.three.setObjectName("three")
        self.mc = QtWidgets.QPushButton(self.centralwidget)
        self.mc.setGeometry(QtCore.QRect(0, 80, 71, 61))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.mc.setFont(font)
        self.mc.setStyleSheet("QPushButton {\n"
"  color: rgb(255, 255, 255);\n"
"    background-color: rgb(30, 30, 30);\n"
"  border: 1px solid gray;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #1E1E1E, stop: 1 #4a4a4a);\n"
"}")
        self.mc.setObjectName("mc")
        self.m_minus = QtWidgets.QPushButton(self.centralwidget)
        self.m_minus.setGeometry(QtCore.QRect(210, 80, 71, 61))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.m_minus.setFont(font)
        self.m_minus.setStyleSheet("QPushButton {\n"
"  color: rgb(255, 255, 255);\n"
"    background-color: rgb(30, 30, 30);\n"
"  border: 1px solid gray;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #1E1E1E, stop: 1 #4a4a4a);\n"
"}")
        self.m_minus.setObjectName("m_minus")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(5, 60, 31, 20))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.pa = QtWidgets.QPushButton(self.centralwidget)
        self.pa.setGeometry(QtCore.QRect(140, 140, 71, 61))
        self.pa.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.pa.setFont(font)
        self.pa.setStyleSheet("QPushButton {\n"
"  color: rgb(255, 255, 255);\n"
"    background-color: rgb(30, 30, 30);\n"
"  border: 1px solid gray;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #1E1E1E, stop: 1 #4a4a4a);\n"
"}")
        self.pa.setObjectName("pa")
        self.switch2b = QtWidgets.QPushButton(self.centralwidget)
        self.switch2b.setGeometry(QtCore.QRect(0, 0, 81, 20))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.switch2b.setFont(font)
        self.switch2b.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.switch2b.setStyleSheet("QPushButton {\n"
"   border: 1px solid gray;\n"
"    color: rgb(255, 255, 255);\n"
"\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #000000, stop: 1 #323232);\n"
"}")
        self.switch2b.setCheckable(False)
        self.switch2b.setObjectName("switch2b")
        self.doc = QtWidgets.QPushButton(self.centralwidget)
        self.doc.setGeometry(QtCore.QRect(80, 0, 81, 20))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.doc.setFont(font)
        self.doc.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.doc.setStyleSheet("QPushButton {\n"
"   border: 1px solid gray;\n"
"    color: rgb(255, 255, 255);\n"
"\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #000000, stop: 1 #323232);\n"
"}")
        self.doc.setCheckable(False)
        self.doc.setObjectName("doc")
        self.back = QtWidgets.QPushButton(self.centralwidget)
        self.back.setGeometry(QtCore.QRect(0, 200, 31, 20))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.back.setFont(font)
        self.back.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.back.setStyleSheet("QPushButton {\n"
"   border: 1px solid gray;\n"
"    color: rgb(255, 255, 255);\n"
"\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #000000, stop: 1 #323232);\n"
"}")
        self.back.setCheckable(False)
        self.back.setObjectName("back")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "calculator"))
        self.seven.setText(_translate("MainWindow", "7"))
        self.label.setText(_translate("MainWindow", "0"))
        self.five.setText(_translate("MainWindow", "5"))
        self.eight.setText(_translate("MainWindow", "8"))
        self.pos_neg.setText(_translate("MainWindow", "+/-"))
        self.six.setText(_translate("MainWindow", "6"))
        self.four.setText(_translate("MainWindow", "4"))
        self.point.setText(_translate("MainWindow", "."))
        self.zero.setText(_translate("MainWindow", "0"))
        self.one.setText(_translate("MainWindow", "1"))
        self.equal.setText(_translate("MainWindow", "="))
        self.nine.setText(_translate("MainWindow", "9"))
        self.divide.setText(_translate("MainWindow", "÷"))
        self.minus.setText(_translate("MainWindow", "-"))
        self.multiply.setText(_translate("MainWindow", "x"))
        self.plus.setText(_translate("MainWindow", "+"))
        self.m_plus.setText(_translate("MainWindow", "M+"))
        self.c.setText(_translate("MainWindow", "C"))
        self.ce.setText(_translate("MainWindow", "CE"))
        self.mr.setText(_translate("MainWindow", "MR"))
        self.two.setText(_translate("MainWindow", "2"))
        self.three.setText(_translate("MainWindow", "3"))
        self.mc.setText(_translate("MainWindow", "MC"))
        self.m_minus.setText(_translate("MainWindow", "M-"))
        self.pa.setText(_translate("MainWindow", "%"))
        self.switch2b.setText(_translate("MainWindow", "Switch Theme"))
        self.doc.setText(_translate("MainWindow", "Manual"))
        self.back.setText(_translate("MainWindow", "←"))


import image_rc
