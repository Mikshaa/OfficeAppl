import os
import rec_rc
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import * 
from PyQt5.QtCore import *
import urllib


curMode = 'Изделие'
curSecondMode = 'Консолидация'
curDeviceCode = 'Не выбрано'
connection = False
curAmount = 0
inputFilesPath = ''
outputFilesPath = ''
contractFilePath = ''
devicesList = []
devicesTxt = ''


def connect(mode = 'check'):
    if mode == 'check':
        host = 'http://google.com'
    elif mode == 'recheck':
        host = 'https://ya.ru/'
    try:
        urllib.request.urlopen(host)
        connected = True
    except:
        connected = False
    if not connected:
        ui.showErrorMessagebox(mode='connection')

def checkFilesPath(path):
    if os.access(path, mode=os.F_OK):
        if os.access(path, mode=os.X_OK):
            return True
        else:
            ui.showErrorMessagebox(text='Нет доступа к директории')
            return False
    else:
        ui.showErrorMessagebox(text='Такой директории не существует')
        return False


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(1200, 400)
        MainWindow.setStyleSheet("background-color: #F5F5F5")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        #############################################

        self.radioButtonDevice = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButtonDevice.setGeometry(QtCore.QRect(40, 120, 130, 40))
        self.radioButtonDevice.setObjectName("radioButton")

        #############################################

        self.radioButtonContract = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButtonContract.setGeometry(QtCore.QRect(40, 160, 130, 40))
        self.radioButtonContract.setObjectName("radioButton_2")

        #############################################

        self.radioButtonConsolid = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButtonConsolid.setGeometry(QtCore.QRect(60, 200, 190, 40))
        self.radioButtonConsolid.setObjectName("radioButton_3")
        self.radioButtonConsolid.setChecked(True)
        self.radioButtonConsolid.setEnabled(False)

        ##############################################

        self.radioButtonDelen = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButtonDelen.setGeometry(QtCore.QRect(60, 240, 130, 40))
        self.radioButtonDelen.setObjectName("radioButton_4")
        self.radioButtonDelen.setEnabled(False)

        #############################################

        self.btngroup1 = QtWidgets.QButtonGroup()
        self.btngroup2 = QtWidgets.QButtonGroup()
        self.btngroup1.addButton(self.radioButtonDevice)
        self.btngroup1.addButton(self.radioButtonContract)
        self.btngroup2.addButton(self.radioButtonConsolid)
        self.btngroup2.addButton(self.radioButtonDelen)
        self.radioButtonDevice.setChecked(True)

        #############################################
        
        self.buttonGenerate = QtWidgets.QPushButton(self.centralwidget)
        self.buttonGenerate.setGeometry(QtCore.QRect(660, 300, 180, 35))
        self.buttonGenerate.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.buttonGenerate.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.buttonGenerate.setStyleSheet("QPushButton{\n"
                                        "border: 2px solid;\n"
                                        "border-color: #B7B7B7;\n"
                                        "border-radius: 6px;\n"
                                        "color: #B7B7B7;\n"
                                        "\n"
                                        "}\n"
                                        "\n"
                                        "")
        self.buttonGenerate.setObjectName("pushButton_3")
        self.buttonGenerate.setEnabled(False)

        #############################################

        self.buttonGenerate_1 = QtWidgets.QPushButton(self.centralwidget)
        self.buttonGenerate_1.setGeometry(QtCore.QRect(660, 215, 180, 35))
        self.buttonGenerate_1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.buttonGenerate_1.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.buttonGenerate_1.setStyleSheet("QPushButton{\n"
                                          "border: 1px solid;\n"
                                          "border-color: #000000;\n"
                                          "border-radius: 6px;\n"
                                          "color: #000;\n"
                                          "\n"
                                          "}\n"
                                          "\n"
                                          "")
        self.buttonGenerate_1.setObjectName("pushButton_9")

        #############################################

        self.labelGetInput = QtWidgets.QLabel(self.centralwidget)
        self.labelGetInput.setGeometry(QtCore.QRect(290, 80, 340, 30))
        self.labelGetInput.setObjectName("label")
        self.labelGetInput.setStyleSheet("font-size: 21px;\n")

        #############################################
        
        self.buttonGetOutput = QtWidgets.QPushButton(self.centralwidget)
        self.buttonGetOutput.setGeometry(QtCore.QRect(570, 150, 40, 40))
        self.buttonGetOutput.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.buttonGetOutput.setStyleSheet("border: 2px solid;\n"
                                        "border-radius: 4px;\n"
                                        "border-color: #858585;\n"
                                        "background-color: #D9D9D9")
        self.buttonGetOutput.setObjectName("pushButton_4")

        #############################################
        
        self.buttonGetInput = QtWidgets.QPushButton(self.centralwidget)
        self.buttonGetInput.setGeometry(QtCore.QRect(570, 75, 40, 40))
        self.buttonGetInput.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.buttonGetInput.setStyleSheet("border: 2px solid;\n"
                                        "border-radius: 4px;\n"
                                        "border-color: #858585;\n"
                                        "background-color: #D9D9D9")
        self.buttonGetInput.setObjectName("pushButton_5")

        #############################################
        
        self.labelGetOutput = QtWidgets.QLabel(self.centralwidget)
        self.labelGetOutput.setGeometry(QtCore.QRect(420, 155, 140, 30))
        self.labelGetOutput.setObjectName("label_2")
        self.labelGetOutput.setStyleSheet("font-size: 21px;\n")

        #############################################
        
        self.labelDeviceCode = QtWidgets.QLabel(self.centralwidget)
        self.labelDeviceCode.setGeometry(QtCore.QRect(660, 25, 210, 30))
        self.labelDeviceCode.setObjectName("label_3")
        self.labelDeviceCode.setStyleSheet("font-size: 21px;\n")

        #############################################

        self.labelContract = QtWidgets.QLabel(self.centralwidget)
        self.labelContract.setGeometry(QtCore.QRect(385, 300, 210, 30))
        self.labelContract.setObjectName("label_6")
        self.labelContract.setEnabled(False)

        #############################################

        self.buttonGetContract = QtWidgets.QPushButton(self.centralwidget)
        self.buttonGetContract.setGeometry(QtCore.QRect(570, 298, 40, 40))
        self.buttonGetContract.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.buttonGetContract.setStyleSheet("border: 2px solid;\n"
                                           "border-radius: 4px;\n"
                                            "color: #B7B7B7;\n"
                                           "border-color: #B7B7B7;\n"
                                           "background-color: #F4F4F4")
        self.buttonGetContract.setObjectName("pushButton_4")
        self.buttonGetContract.setEnabled(False)

        #############################################

        self.comboBoxGetDevice = QtWidgets.QComboBox(self.centralwidget)
        #self.comboBoxGetDevice.setEnabled(False)
        self.comboBoxGetDevice.setGeometry(QtCore.QRect(660, 75, 500, 40))
        self.comboBoxGetDevice.setStyleSheet("QComboBox{\n"
                                    "background-color: #fff;\n"
                                    "border: 1px solid;\n"
                                    "border-radius: 4px;\n"
                                    "\n"
                                    "}\n"
                                    "QComboBox::drop-down{\n"
                                    "width: 34px;\n"
                                    "height: 36px;\n"
                                    "top: 0px;\n"
                                    "border: 1px solid;\n"
                                    "border-left: 2px solid;\n"
                                    "border-radius: 3px;\n"
                                    "background-color: #fff;\n"
                                    "\n"
                                    "}\n"
                                    "\n"
                                    "QComboBox::down-arrow{\n"
                                    "image: url(:/img/Polygon 2.svg)\n"
                                    "}\n"
                                    "")
        self.comboBoxGetDevice.setCurrentText("Выберите")
        self.comboBoxGetDevice.setObjectName("comboBox")


        #############################################
        
        self.lineEditAmount = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditAmount.setGeometry(QtCore.QRect(660, 150, 50, 40))
        self.lineEditAmount.setValidator(QIntValidator())
        self.lineEditAmount.setStyleSheet("padding-left: 2px;\n"
                                    "top: 0px;\n"
                                    "border: 2px solid;\n"
                                    "border-radius: 3px;\n"
                                    "font-weight: 400;\n"
                                    "background-color: #fff")
        self.lineEditAmount.setObjectName("lineEdit")
        MainWindow.setCentralWidget(self.centralwidget)

        #############################################

        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(250, 75, 20, 250))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(660, 270, 500, 10))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")

        ############################################
        self.widgetConnect()
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def widgetConnect(self):
        self.lineEditAmount.textChanged.connect(self.setAmount)
        self.comboBoxGetDevice.activated[str].connect(self.deviceCodeChanged)
        self.buttonGetContract.clicked.connect(self.getContract)
        self.buttonGetInput.clicked.connect(self.getInputFilesPath)
        self.buttonGetOutput.clicked.connect(self.getOutputFilesPath)
        self.radioButtonConsolid.toggled.connect(lambda: self.changeSecondMode())
        self.radioButtonDevice.toggled.connect(lambda: self.changeMode(mode='device'))

    def deviceCodeChanged(self, text):
        if 1: #Нужна функция проверки наличия шаблона
            curDeviceCode = text
        else:
            self.showErrorMessagebox(text='Файл-шаблон\nотсутствует')

            #Вызов окна ошибки
            

    def setAmount(self, amount):
        global curAmount
        curAmount = amount

    def changeMode(self, mode):
        global curMode
        global curSecondMode
        if self.radioButtonDevice.isChecked():
            curMode = 'Device'
            print(curMode)
            self.radioButtonConsolid.setChecked(True)
            self.radioButtonDelen.setChecked(False)
            self.radioButtonConsolid.setEnabled(False)
            self.radioButtonDelen.setEnabled(False)
            self.buttonGetContract.setStyleSheet("border: 1px solid;\n"
                                            "border-radius: 4px;\n"
                                            "border-color: #B7B7B7;\n"
                                            "background-color: #F4F4F4\n")
            self.comboBoxGetDevice.setStyleSheet("QComboBox{\n"
                                                 "background-color: #fff;\n"
                                                 "border: 1px solid;\n"
                                                 "border-radius: 4px;\n"
                                                 "\n"
                                                 "}\n"
                                                 "QComboBox::drop-down{\n"
                                                 "width: 34px;\n"
                                                 "height: 36px;\n"
                                                 "top: 0px;\n"
                                                 "border: 1px solid;\n"
                                                 "border-left: 2px solid;\n"
                                                 "border-radius: 3px;\n"
                                                 "background-color: #fff;\n"
                                                 "\n"
                                                 "}\n"
                                                 "\n"
                                                 "QComboBox::down-arrow{\n"
                                                 "image: url(:/img/Polygon 2.svg)\n"
                                                 "}\n"
                                                 "")
            self.lineEditAmount.setStyleSheet("padding-left: 2px;\n"
                                              "top: 0px;\n"
                                              "border: 2px solid;\n"
                                              "border-radius: 3px;\n"
                                              "font-weight: 400;\n"
                                              "border-color: #000;\n"
                                              "background-color: #fff")
            self.buttonGenerate_1.setStyleSheet("QPushButton{\n"
                                                "border: 2px solid;\n"
                                                "color: #000;\n"
                                                "border-color: #000;\n"
                                                "border-radius: 6px;\n"
                                                # "color: #848484;\n"
                                                "\n"
                                                "}\n"
                                                "\n"
                                                "")
            self.buttonGenerate.setStyleSheet("QPushButton{\n"
                                              "border: 2px solid;\n"
                                              "color: #000;\n"
                                              "border-color: #000;\n"
                                              "border-radius: 6px;\n"
                                              # "color: #848484;\n"
                                              "\n"
                                              "}\n"
                                              "\n"
                                              "")
            self.buttonGenerate.setStyleSheet("QPushButton{\n"
                                              "border: 2px solid;\n"
                                              "color: #B7B7B7;\n"
                                              "border-color: #B7B7B7;\n"
                                              "border-radius: 6px;\n"
                                              # "color: #848484;\n"
                                              "\n"
                                              "}\n"
                                              "\n"
                                              "")
            self.buttonGetContract.setEnabled(False)
            self.buttonGenerate.setEnabled(False)
            self.labelContract.setEnabled(False)
            self.comboBoxGetDevice.setEnabled(True)
            self.labelDeviceCode.setEnabled(True)
            self.lineEditAmount.setEnabled(True)
            self.buttonGenerate_1.setEnabled(True)
        else:
            curMode = 'Contract'
            curSecondMode = 'Consolid'
            print(curMode)
            print(curSecondMode)
            self.radioButtonConsolid.setChecked(True)
            self.radioButtonDelen.setChecked(False)
            self.radioButtonConsolid.setEnabled(True)
            self.radioButtonDelen.setEnabled(True)
            self.comboBoxGetDevice.setStyleSheet("QComboBox{\n"
                                                 "background-color: #fff;\n"
                                                 "border: 1px solid;\n"
                                                 "border-radius: 4px;\n"
                                                 "border-color: #B7B7B7;\n"
                                                 "\n"
                                                 "}\n"
                                                 "QComboBox::drop-down{\n"
                                                 "width: 34px;\n"
                                                 "height: 36px;\n"
                                                 "top: 0px;\n"
                                                 "border: 1px solid;\n"
                                                 "border-left: 2px solid;\n"
                                                 "border-color: #B7B7B7;\n"
                                                 "border-radius: 3px;\n"
                                                 "background-color: #fff;\n"
                                                 "\n"
                                                 "}\n"
                                                 "\n"
                                                 "QComboBox::down-arrow{\n"
                                                 "image: url(:/img/PolygonGray.svg)\n"
                                                 "}\n"
                                                 "")
            self.buttonGetContract.setStyleSheet("border: 2px solid;\n"
                                                 "border-radius: 4px;\n"
                                                 "border-color: #858585;\n"
                                                 "background-color: #D9D9D9\n")
            self.buttonGenerate.setStyleSheet("QPushButton{\n"
                                              "border: 2px solid;\n"
                                              "color: #000;\n"
                                              "border-color: #000;\n"
                                              "border-radius: 6px;\n"
                                              #"color: #848484;\n"
                                              "\n"
                                              "}\n"
                                              "\n"
                                              "")
            self.buttonGenerate_1.setStyleSheet("QPushButton{\n"
                                              "border: 2px solid;\n"
                                              "color: #B7B7B7;\n"
                                              "border-color: #B7B7B7;\n"
                                              "border-radius: 6px;\n"
                                              # "color: #848484;\n"
                                              "\n"
                                              "}\n"
                                              "\n"
                                              "")
            self.lineEditAmount.setStyleSheet("padding-left: 2px;\n"
                                              "top: 0px;\n"
                                              "border: 2px solid;\n"
                                              "border-radius: 3px;\n"
                                              "font-weight: 400;\n"
                                              "border-color: #B7B7B7;\n"
                                              "background-color: #fff")
            self.buttonGenerate.setEnabled(True)
            self.buttonGetContract.setEnabled(True)
            self.labelContract.setEnabled(True)
            self.comboBoxGetDevice.setEnabled(False)
            self.labelDeviceCode.setEnabled(False)
            self.lineEditAmount.setEnabled(False)
            self.buttonGenerate_1.setEnabled(False)

    def showErrorMessagebox(self, mode='default',text=''):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Critical)
        #msg.setIcon(QtWidgets.QMessageBox.Information)
        msg.setText(text)
        msg.setWindowTitle("Information MessageBox")
        if mode == 'default':
            retval = msg.exec_()
        elif mode == 'connection':
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            text = 'Отсутствует\nинтернет-соединение'
            msg.setStandardButtons(QtWidgets.QMessageBox.Retry | QtWidgets.QMessageBox.Ok)
            buttonRetry = msg.button(QtWidgets.QMessageBox.Retry)
            msg.setText(text)
            buttonRetry.setText('Повторить')
            retval = msg.exec_()
            if retval == QtWidgets.QMessageBox.Retry:
                connect(mode='recheck')
    def showFinalMessage(self):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Information)
        msg.setText('Файл сгенерирован')
        msg.setWindowTitle("Готово")
        retval = msg.exec_()



    def changeSecondMode(self):
        global curSecondMode
        if self.radioButtonConsolid.isChecked():
            curSecondMode = 'Consolid'
        else:
            curSecondMode = 'Separate'
        print(curSecondMode)


    def getContract(self):
        global contractFilePath
        try:
            contractFilePath = QtWidgets.QFileDialog.getOpenFileName()[0]
            if 1: # check contract file на файлы шаблоны
                if 1: # check zeros in contract
                    pass
                else:
                    contractFilePath = ''
                    self.showErrorMessagebox(text='В файле-шоблоне\nнайдены нули')
            else:
                contractFilePath = ''
                self.showErrorMessagebox(text='Не найден файл шаблона')
        except:
            pass

    def getInputFilesPath(self):
        global inputFilesPath
        global devicesList
        global devicesTxt
        try:
            inputFilesPath = QtWidgets.QFileDialog.getExistingDirectory()
            if checkFilesPath(inputFilesPath):
                devicesList = os.listdir(inputFilesPath)
                if 'Перечень изделий ЗАО ЗЭТ.txt' in devicesList:
                    devicesTxt = devicesList[devicesList.index('Перечень изделий ЗАО ЗЭТ.txt')]
                    devicesList.remove('Перечень изделий ЗАО ЗЭТ.txt')
                    self.pasteDevicesCodes(devicesList)
                else:
                    self.showErrorMessagebox(text='Не найден файл с\nкодами устройств')
            else:
                inputFilesPath = ''
        except:
            pass


    def getOutputFilesPath(self):
        global outputFilesPath
        try:
            outputFilesPath = QtWidgets.QFileDialog.getExistingDirectory()
            if checkFilesPath(outputFilesPath):
                pass
            else:
                outputFilesPath = ''
        except:
            pass

    def pasteDevicesCodes(self, deviceCodes):
        for code in deviceCodes:
            self.comboBoxGetDevice.addItem(code)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.buttonGenerate.setText(_translate("MainWindow", "Сгенерировать"))
        self.buttonGenerate_1.setText(_translate("MainWindow", "Сгенерировать"))
        self.labelGetInput.setText(_translate("MainWindow", "Выбор набора шаблонов"))
        self.buttonGetOutput.setText(_translate("MainWindow", "..."))
        self.buttonGetInput.setText(_translate("MainWindow", "..."))
        self.labelGetOutput.setText(_translate("MainWindow", "Сохранять в"))
        self.labelDeviceCode.setText(_translate("MainWindow", "Выбор изделия"))
        #self.labelGetAmount.setText(_translate("MainWindow", "Количество"))
        self.labelContract.setText(_translate("MainWindow", "Выбор договора"))
        self.buttonGetContract.setText(_translate("MainWindow", "..."))
        self.radioButtonDevice.setText(_translate("MainWindow", "Изделие"))
        self.radioButtonContract.setText(_translate("MainWindow", "Договор"))
        self.radioButtonConsolid.setText(_translate("MainWindow", "Консолидация"))
        self.radioButtonDelen.setText(_translate("MainWindow", "Деление"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    connect()
    sys.exit(app.exec_())
