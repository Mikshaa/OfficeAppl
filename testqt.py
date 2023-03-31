# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Michael\Desktop\design.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import * 
from PyQt5.QtCore import *

mainMode = 'Изделие'
secondMode = 'Консолидация'
curDeviceCode = 'Не выбрано'

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(1200, 500)

        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("background-color: #F5F5F5")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        #############################################
        
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(60, 70, 225, 66))
        self.pushButton.clicked.connect(self.change_color)
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(False)
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.pushButton.setStyleSheet("QPushButton{\n"
"background-color: #94C7E6;\n"
"border: 0px solid;\n"
"border-color: #000000;\n"
"border-radius: 33px;\n"
"color: #000;\n"
"\n"
"}\n"
"\n"
"")
        self.pushButton.setObjectName("pushButton")

        #############################################
        
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(60, 170, 225, 66))
        self.pushButton_2.clicked.connect(self.change_color_1)
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(False)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.pushButton_2.setStyleSheet("QPushButton{\n"
"background-color: #ffffff;\n"
"border: 1px solid;\n"
"border-color: #000000;\n"
"border-radius: 33px;\n"
"color: #000;\n"
"\n"
"}\n"
"\n"
"")
        self.pushButton_2.setObjectName("pushButton_2")

        #############################################
        
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(365, 350, 470, 88))


        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(False)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_3.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.pushButton_3.setStyleSheet("QPushButton{\n"
"background-color: #94C7E6;\n"
"border: 1px solid;\n"
"border-color: #000000;\n"
"border-radius: 44px;\n"
"color: #000;\n"
"\n"
"}\n"
"\n"
"")
        self.pushButton_3.setObjectName("pushButton_3")

        #############################################
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(320, 80, 340, 30))
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setObjectName("label")

        #############################################
        
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(650, 150, 40, 40))
        self.pushButton_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_4.setStyleSheet("border-color: #000;\n"
"border: 1px solid;\n"
"border-radius: 4px;\n"
"background-color: #fff")
        self.pushButton_4.clicked.connect(self.get_output_files_path)
        self.pushButton_4.setObjectName("pushButton_4")

        #############################################
        
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(650, 75, 40, 40))
        self.pushButton_5.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_5.setStyleSheet("border-color: #000;\n"
"border: 1px solid;\n"
"border-radius: 4px;\n"
"background-color: #fff")
        self.pushButton_5.clicked.connect(self.get_input_files_path)
        self.pushButton_5.setObjectName("pushButton_5")
        
        #############################################
        
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(475, 155, 150, 22))
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        #############################################
        
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(730, 80, 210, 30))
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

        #############################################
        
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(775, 155, 162, 22))
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(11)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")

        #############################################
        
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(940, 81, 220, 34))
        self.comboBox.addItem('Apple')
        self.comboBox.addItem('banana')
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(9)
        self.comboBox.setFont(font)
        self.comboBox.setStyleSheet("QComboBox{\n"
"background-color: #fff;\n"
"border: 1px solid;\n"
"border-radius: 4px;\n"
"\n"
"}\n"
"QComboBox::drop-down{\n"
"width: 30px;\n"
"height: 30px;\n"
"top: 0px;\n"
"border: 1px solid;\n"
"border-left: 2px solid;\n"
"border-radius: 3px;\n"
"background-color: #94C7E6;\n"
"\n"
"}\n"
"\n"
"QComboBox::down-arrow{\n"
"image: url(:/img/Polygon 2.svg)\n"
"}\n"
"")

        self.comboBox.setCurrentText("Выберите")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.activated[str].connect(self.onChanged)

        #############################################
        
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.textChanged.connect(self.extt)
        self.lineEdit.setGeometry(QtCore.QRect(940, 153, 220, 34))
        self.lineEdit.setValidator(QIntValidator())
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("padding-left: 2px;\n"
"top: 0px;\n"
"border: 1px solid;\n"
"border-radius: 3px;\n"
"font-weight: 400;\n"
"background-color: #fff")
        self.lineEdit.setObjectName("lineEdit")
        MainWindow.setCentralWidget(self.centralwidget)

        #############################################
        
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def onChanged(self, text):
        try:
            #check izdelie
            
        
    def extt(self, text):
        print(text)

    def change_color(self):
        self.pushButton.setStyleSheet("QPushButton{\n"
"background-color: #94C7E6;\n"
"border: 0px solid;\n"
"border-color: #000000;\n"
"border-radius: 33px;\n"
"}\n")

            #color = 'background-color: #94C7E6;\n'
        self.pushButton_2.setStyleSheet("QPushButton{\n"
"background-color: #ffffff;\n"
"border: 1px solid;\n"
"border-color: #000000;\n"
"border-radius: 33px;\n"
"}\n")

    def change_color_1(self):
        self.pushButton_2.setStyleSheet("QPushButton{\n"
"background-color: #94C7E6;\n"
"border: 0px solid;\n"
"border-color: #000000;\n"
"border-radius: 33px;\n"
"}\n")

            #color = 'background-color: #94C7E6;\n'
        self.pushButton.setStyleSheet("QPushButton{\n"
"background-color: #ffffff;\n"
"border: 1px solid;\n"
"border-color: #000000;\n"
"border-radius: 33px;\n"
"}\n")

    def get_input_files_path(self):
        input_file_path = QtWidgets.QFileDialog.getExistingDirectory()
        print(input_file_path)

    def get_output_files_path(self):
        output_file_path = QtWidgets.QFileDialog.getExistingDirectory()
        print(output_file_path)
        print(1)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Изделие"))
        self.pushButton_2.setText(_translate("MainWindow", "Договор"))
        self.pushButton_3.setText(_translate("MainWindow", "Сгенерировать"))
        self.label.setText(_translate("MainWindow", "Выбор набора шаблонов"))
        self.pushButton_4.setText(_translate("MainWindow", "..."))
        self.pushButton_5.setText(_translate("MainWindow", "..."))
        self.label_2.setText(_translate("MainWindow", "Сохранять в"))
        self.label_3.setText(_translate("MainWindow", "Выбор изделия"))
        self.label_4.setText(_translate("MainWindow", "Количество"))
import rec_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())