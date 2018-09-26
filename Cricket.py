# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Cricket.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit,QDialog
import sqlite3
import math
import Scoring

class Ui_Dialog(object):
    def change_text(self):
        txt=self.lineEdit.text()
        ui.label_14.setText(txt)
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(361, 244)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(0, 130, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 50, 141, 20))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(150, 50, 113, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(280, 50, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.change_text)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600;\">Enter Team Name</span></p></body></html>"))
        self.pushButton.setText(_translate("Dialog", "Enter"))


class Ui_Evaulate(object):
    def change_combo(self):
        txt=ui.label_14.text()
        connection=sqlite3.connect("Cricket.db")
        connection.execute("INSERT INTO Teams (Name) VALUES ('%s')" %(txt))
        result2=connection.execute("SELECT Name from Teams;")
        record2=result2.fetchall()
        for i in record2:
            self.comboBox_2.addItem(i[0])
            self.comboBox.addItem("Match")
        
        for i in range(ui.list2.count()):
            self.listWidget_2.addItem(ui.list2.item(i).text())
        for j in range(ui.list2.count()):
            txt=ui.list2.item(j).text()
            connection=sqlite3.connect("Cricket.db")
            point_2=connection.execute("SELECT Match.Wickets,Match.RunOut,Match.Bowled,Match.Given,Match.Catches,Match.Stumping,Match.Scored,Match.Fours,Match.Sixes,Match.Faced ,Stats.Category from Match,Stats WHERE Match.Player=Stats.Player AND Stats.Player='"+txt+"';")
            record_2=point_2.fetchall()
            for p in record_2:
                if p[10]=='AR':
                    points_bowl=int(Scoring.bowling(p[0],p[1],p[2],p[3],p[4],p[5]))
                    points_bat=int(Scoring.batting(p[6],p[7],p[8],p[9],0,0,0))
                    c=points_bowl
                    d=points_bat
                    e=c+d
                    self.listWidget.addItem(str(e))
                elif p[10]=='BAT':
                    points_bat=int(Scoring.batting(p[6],p[7],p[8],p[9],p[1],p[4],p[5]))
                    g=points_bat
                    self.listWidget.addItem(str(g))

                elif p[10]=='BWL':
                    points_bowl=int(Scoring.bowling(p[0],p[1],p[2],p[3],p[4],p[5]))
                    h=points_bowl
                    self.listWidget.addItem(str(h))

                elif p[10]=='WK':
                     points_bat=int(Scoring.batting(p[6],p[7],p[8],p[9],p[1],p[4],p[5]))
                     y=points_bat
                     self.listWidget.addItem(str(y))
        sums=0
        for i in range(self.listWidget.count()):
            a=int(self.listWidget.item(i).text())
            sums+=a
        self.label_5.setText(str(sums))
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
        self.pushButton.clicked.connect(self.change_combo)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(350, 510, 120, 23))
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(80, 100, 561, 20))
        self.line.setLineWidth(2)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        Evaulate.setCentralWidget(self.centralwidget)
        self.retranslateUi(Evaulate)
        QtCore.QMetaObject.connectSlotsByName(Evaulate)

    def retranslateUi(self, Evaulate):
        _translate = QtCore.QCoreApplication.translate
        Evaulate.setWindowTitle(_translate("Evaulate", "MainWindow"))
        self.label.setText(_translate("Evaulate", "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600;\">Evaluate the Performance of your Fantasy Team</span></p></body></html>"))
        self.label_2.setText(_translate("Evaulate", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Players</span></p></body></html>"))
        self.label_3.setText(_translate("Evaulate", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Points</span></p></body></html>"))
        self.pushButton.setText(_translate("Evaulate", "Calculate Score"))


    


class Ui_MainWindow(object):
    def Checkstate(self):
        if self.rb1.isChecked()==True:
            self.list1.clear()
            connection=sqlite3.connect("Cricket.db")
            result2=connection.execute("SELECT Player from Stats WHERE Category='BAT';")
            record2=result2.fetchall()
            a=0
            for i in record2:
                self.list1.addItem(i[0])
                a+=Scoring.batscoring(i[0])
            self.label_11.setText(str(a))
            self.label_6.setText("4")
            self.label_13.setText("0")
               
        elif self.rb2.isChecked()==True:
            self.list1.clear()
            connection=sqlite3.connect("Cricket.db")
            result4=connection.execute("SELECT Player from Stats WHERE Category='BWL';")
            record4=result4.fetchall()
            b=0
            for i in record4:
                self.list1.addItem(i[0])
                b+=Scoring.bowlscoring(i[0])
            self.label_11.setText(str(b))
            self.label_4.setText("4")
            self.label_13.setText("0")


        elif self.rb3.isChecked()==True:
             self.list1.clear()
             connection=sqlite3.connect("Cricket.db")
             point_2=connection.execute("SELECT  Player from Stats WHERE Category='AR';")
             record_2=point_2.fetchall()
             e=0
             for i in record_2:
                 self.list1.addItem(i[0])
                 e+=Scoring.AllRounder(i[0])  
             self.label_11.setText(str(e))
             self.label_3.setText("5")
             self.label_13.setText("0")
                 

        elif self.rb4.isChecked()==True:
            self.list1.clear()
            connection=sqlite3.connect("Cricket.db")
            result=connection.execute("SELECT Match.Player,Match.Scored,Match.Fours,Match.Sixes,Match.Faced,Match.RunOut,Match.Catches,Match.Stumping from Stats,Match WHERE Stats.Player=Match.Player AND Stats.Category='WK';")
            record=result.fetchall()
            f=0
            for i in record:
                self.list1.addItem(i[0])
                f+= Scoring.WicketKeeping(i[0])
            self.label_11.setText(str(f))
            self.label_8.setText("2")
            self.label_13.setText("0")

    def dialogshow(self):
        self.Dialog = QtWidgets.QDialog()
        self.sub_window = Ui_Dialog()
        self.sub_window.setupUi(self.Dialog)
        self.Dialog.show()

    def PointsUsed_1(self,txt):
            connection=sqlite3.connect("Cricket.db")
            point_2=connection.execute("SELECT  Category from Stats WHERE Player='"+txt+"';")
            record_2=point_2.fetchall()
            for i in record_2:
                if i[0]=='BAT':
                    Num=int(self.label_6.text())
                    text_2=int(self.label_13.text())
                    text=int(self.label_11.text())
                    a=int(Scoring.batscoring(txt))
                    f=text-a
                    g=text_2+a
                    Num-=1
                    self.label_11.setText(str(f))
                    self.label_13.setText(str(g))
                    self.label_6.setText(str(Num))
                elif i[0]=='BWL':
                    Num=int(self.label_4.text())
                    text_2=int(self.label_13.text())
                    text=int(self.label_11.text())
                    b=int(Scoring.bowlscoring(txt))
                    Num-=1
                    m=text-b
                    p=text_2+b
                    self.label_11.setText(str(m))
                    self.label_13.setText(str(p))
                    self.label_4.setText(str(Num))
                elif i[0]=='AR':
                    Num=int(self.label_3.text())
                    text_2=int(self.label_13.text())
                    text=int(self.label_11.text())
                    c=int(Scoring.AllRounder(txt))
                    j=text-c
                    y=text_2+c
                    Num-=1
                    self.label_11.setText(str(j))
                    self.label_13.setText(str(y))
                    self.label_3.setText(str(Num))

                elif i[0]=='WK':
                    Num=int(self.label_8.text())
                    text_2=int(self.label_13.text())
                    text=int(self.label_11.text())
                    d=int(Scoring.WicketKeeping(txt))
                    h=text-d
                    l=text_2+d
                    Num-=1
                    self.label_11.setText(str(h))
                    self.label_13.setText(str(l))
                    self.label_8.setText(str(Num))
    def PointsUsed_2(self,txt):
            connection=sqlite3.connect("Cricket.db")
            point_2=connection.execute("SELECT  Category from Stats WHERE Player='"+txt+"';")
            record_2=point_2.fetchall()
            for i in record_2:
                if i[0]=='BAT':
                    Num=int(self.label_6.text())
                    text_2=int(self.label_13.text())
                    text=int(self.label_11.text())
                    a=int(Scoring.batscoring(txt))
                    f=text+a
                    g=text_2-a
                    Num+=1
                    self.label_11.setText(str(f))
                    self.label_13.setText(str(g))
                    self.label_6.setText(str(Num))
                elif i[0]=='BWL':
                    Num=int(self.label_4.text())
                    text_2=int(self.label_13.text())
                    text=int(self.label_11.text())
                    b=int(Scoring.bowlscoring(txt))
                    Num+=1
                    m=text+b
                    p=text_2-b
                    self.label_11.setText(str(m))
                    self.label_13.setText(str(p))
                    self.label_4.setText(str(Num))
                elif i[0]=='AR':
                    Num=int(self.label_3.text())
                    text_2=int(self.label_13.text())
                    text=int(self.label_11.text())
                    c=int(Scoring.AllRounder(txt))
                    j=text+c
                    y=text_2-c
                    Num+=1
                    self.label_11.setText(str(j))
                    self.label_13.setText(str(y))
                    self.label_3.setText(str(Num))

                elif i[0]=='WK':
                    Num=int(self.label_8.text())
                    text_2=int(self.label_13.text())
                    text=int(self.label_11.text())
                    d=int(Scoring.WicketKeeping(txt))
                    h=text+d
                    l=text_2-d
                    Num+=1
                    self.label_11.setText(str(h))
                    self.label_13.setText(str(l))
                    self.label_8.setText(str(Num))

             

    def removelist1(self, item):
            txt=item.text()
            self.PointsUsed_1(txt)
            self.list1.takeItem(self.list1.row(item))
            self.list2.addItem(item.text())

    def removelist2(self, item):
        txt=item.text()
        self.PointsUsed_2(txt)
        self.list2.takeItem(self.list2.row(item))
        self.list1.addItem(item.text())
        
    def evaulateWindow(self):
            self.evaulateWindow=QtWidgets.QMainWindow()
            self.ui=Ui_Evaulate()
            self.ui.setupUi(self.evaulateWindow)
            self.evaulateWindow.show()
        

    def menufunction(self, action):
        txt=action.text()
        if txt =='New Team':
            self.dialogshow()
            self.rb1.toggled.connect(self.Checkstate)
            self.rb2.toggled.connect(self.Checkstate)
            self.rb3.toggled.connect(self.Checkstate)
            self.rb4.toggled.connect(self.Checkstate)
            self.list1.itemDoubleClicked.connect(self.removelist1)
            self.list2.itemDoubleClicked.connect(self.removelist2)

        elif txt=='Evaluate Team':
            self.evaulateWindow()

        elif txt=='Close ':
            sys.exit()
               
      
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(30, 40, 711, 80))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.label_6 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout.addWidget(self.label_6)
        self.label_5 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout.addWidget(self.label_5)
        self.label_4 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        self.label_7 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout.addWidget(self.label_7)
        self.label_3 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.label_8 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout.addWidget(self.label_8)
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(130, 140, 81, 16))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(220, 140, 47, 16))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(480, 140, 61, 16))
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(560, 140, 47, 16))
        self.label_13.setObjectName("label_13")
        self.treeWidget = QtWidgets.QTreeWidget(self.centralwidget)
        self.treeWidget.setGeometry(QtCore.QRect(75, 160, 671, 391))
        self.treeWidget.setObjectName("treeWidget")
        self.rb1 = QtWidgets.QRadioButton(self.centralwidget)
        self.rb1.setGeometry(QtCore.QRect(120, 170, 91, 21))
        self.rb1.setObjectName("rb1")
        self.rb2 = QtWidgets.QRadioButton(self.centralwidget)
        self.rb2.setGeometry(QtCore.QRect(180, 170, 82, 21))
        self.rb2.setObjectName("rb2")
        self.rb3 = QtWidgets.QRadioButton(self.centralwidget)
        self.rb3.setGeometry(QtCore.QRect(250, 170, 82, 21))
        self.rb3.setObjectName("rb3")
        self.rb4 = QtWidgets.QRadioButton(self.centralwidget)
        self.rb4.setGeometry(QtCore.QRect(300, 170, 82, 21))
        self.rb4.setObjectName("rb4")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(480, 170, 61, 16))
        self.label_9.setObjectName("label_9")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(560, 170, 47, 13))
        self.label_14.setObjectName("label_14")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(100, 190, 621, 361))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.list1 = QtWidgets.QListWidget(self.horizontalLayoutWidget_2)
        self.list1.setObjectName("list1")
        self.horizontalLayout_3.addWidget(self.list1)
        self.label_16 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_16.setObjectName("label_16")
        self.horizontalLayout_3.addWidget(self.label_16)
        self.list2 = QtWidgets.QListWidget(self.horizontalLayoutWidget_2)
        self.list2.setObjectName("list2")
        self.horizontalLayout_3.addWidget(self.list2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menuManage_Teams = QtWidgets.QMenu(self.menubar)
        self.menuManage_Teams.setObjectName("menuManage_Teams")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNew_Team = QtWidgets.QAction(MainWindow)
        self.actionNew_Team.setObjectName("actionNew_Team")
        self.actionClose = QtWidgets.QAction(MainWindow)
        self.actionClose.setObjectName("actionClose")
        self.actionEvaluate_Team = QtWidgets.QAction(MainWindow)
        self.actionEvaluate_Team.setObjectName("actionEvaluate_Team")
        self.menuManage_Teams.addAction(self.actionNew_Team)
        self.menuManage_Teams.addAction(self.actionEvaluate_Team)
        self.menuManage_Teams.addAction(self.actionClose)
        
        self.menubar.addAction(self.menuManage_Teams.menuAction())
        self.menuManage_Teams.triggered[QtWidgets.QAction].connect(self.menufunction)
         


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Batsman(BAT)"))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#5500ff;\">0</span></p></body></html>"))
        self.label_5.setText(_translate("MainWindow", "Bowling(BOW)"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#5500ff;\">0</span></p></body></html>"))
        self.label_7.setText(_translate("MainWindow", "AllRounder(AR)"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#5500ff;\">0</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "Wicket-Keeper(WK)"))
        self.label_8.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#5500ff;\">0</span></p></body></html>"))
        self.label_10.setText(_translate("MainWindow", "Points Available"))
        self.label_11.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#5500ff;\">0</span></p></body></html>"))
        self.label_12.setText(_translate("MainWindow", "Points Used"))
        self.label_13.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#5500ff;\">0</span></p></body></html>"))
        self.treeWidget.headerItem().setText(0, _translate("MainWindow", "             "))
        self.rb1.setText(_translate("MainWindow", "BAT"))
        self.rb2.setText(_translate("MainWindow", "BWL"))
        self.rb3.setText(_translate("MainWindow", "AR"))
        self.rb4.setText(_translate("MainWindow", "WK"))
        self.label_9.setText(_translate("MainWindow", "Team Name"))
        self.label_14.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#5500ff;\">###</span></p></body></html>"))
        self.label_16.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt; font-weight:600; color:#0000ff;\">&gt;</span></p></body></html>"))
        self.menuManage_Teams.setTitle(_translate("MainWindow", "Manage Teams"))
        self.actionNew_Team.setText(_translate("MainWindow", "New Team"))
        self.actionClose.setText(_translate("MainWindow", "Close "))
        self.actionEvaluate_Team.setText(_translate("MainWindow", "Evaluate Team"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

