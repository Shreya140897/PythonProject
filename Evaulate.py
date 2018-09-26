# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Evaulate.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Evaulate(object):
    def change_text(self):
        txt=self.label_14.text()
        ui.comboBox_2.setText(txt)
    
    def setupUi(self, Evaulate):
        Evaulate.setObjectName("Evaulate")
        Evaulate.resize(712, 600)
        Evaulate.setMinimumSize(QtCore.QSize(100, 0))
        self.centralwidget = QtWidgets.QWidget(Evaulate)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(170, 20, 361, 20))
        self.label.setObjectName("label")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(80, 60, 561, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.comboBox_2 = QtWidgets.QComboBox(self.horizontalLayoutWidget)
        self.comboBox_2.setMinimumSize(QtCore.QSize(100, 0))
        self.comboBox_2.setCurrentText("")
        self.comboBox_2.setMaxVisibleItems(5)
        self.comboBox_2.setObjectName("comboBox_2")
        self.horizontalLayout.addWidget(self.comboBox_2)
        self.label_4 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        self.comboBox = QtWidgets.QComboBox(self.horizontalLayoutWidget)
        self.comboBox.setObjectName("comboBox")
        self.horizontalLayout.addWidget(self.comboBox)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(70, 150, 581, 321))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.listWidget_2 = QtWidgets.QListWidget(self.horizontalLayoutWidget_2)
        self.listWidget_2.setObjectName("listWidget_2")
        self.horizontalLayout_2.addWidget(self.listWidget_2)
        self.listWidget = QtWidgets.QListWidget(self.horizontalLayoutWidget_2)
        self.listWidget.setLineWidth(6)
        self.listWidget.setObjectName("listWidget")
        self.horizontalLayout_2.addWidget(self.listWidget)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(150, 130, 51, 21))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(490, 130, 47, 21))
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(310, 480, 91, 23))
        self.pushButton.setObjectName("pushButton")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(280, 510, 141, 51))
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(80, 100, 561, 20))
        self.line.setLineWidth(2)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        Evaulate.setCentralWidget(self.centralwidget)
        self.change_text()
        self.retranslateUi(Evaulate)
        QtCore.QMetaObject.connectSlotsByName(Evaulate)

    def retranslateUi(self, Evaulate):
        _translate = QtCore.QCoreApplication.translate
        Evaulate.setWindowTitle(_translate("Evaulate", "MainWindow"))
        self.label.setText(_translate("Evaulate", "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600;\">Evaluate the Performance of your Fantasy Team</span></p></body></html>"))
        self.label_2.setText(_translate("Evaulate", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Players</span></p></body></html>"))
        self.label_3.setText(_translate("Evaulate", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Points</span></p></body></html>"))
        self.pushButton.setText(_translate("Evaulate", "Calculate Score"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Evaulate = QtWidgets.QMainWindow()
    ui = Ui_Evaulate()
    ui.setupUi(Evaulate)
    Evaulate.show()
    sys.exit(app.exec_())

