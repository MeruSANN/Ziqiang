# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ToolBox.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QFileDialog
import base64
import json
import os
import qrcode


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(300, 300)
        MainWindow.setMinimumSize(QtCore.QSize(300, 300))
        MainWindow.setMaximumSize(QtCore.QSize(300, 300))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setEnabled(True)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 300, 300))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setMinimumSize(QtCore.QSize(300, 300))
        self.tabWidget.setMaximumSize(QtCore.QSize(300, 300))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setMinimumSize(QtCore.QSize(300, 300))
        self.tab.setMaximumSize(QtCore.QSize(300, 300))
        self.tab.setObjectName("tab")
        self.Encode = QtWidgets.QPushButton(self.tab)
        self.Encode.setGeometry(QtCore.QRect(0, 20, 80, 41))
        self.Encode.setCheckable(False)
        self.Encode.setAutoDefault(False)
        self.Encode.setDefault(False)
        self.Encode.setFlat(False)
        self.Encode.setObjectName("Encode")
        self.Decode = QtWidgets.QPushButton(self.tab)
        self.Decode.setGeometry(QtCore.QRect(0, 70, 80, 41))
        self.Decode.setCheckable(False)
        self.Decode.setAutoDefault(False)
        self.Decode.setDefault(False)
        self.Decode.setFlat(False)
        self.Decode.setObjectName("Decode")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(80, 0, 151, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(80, 110, 171, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.Base64Input = QtWidgets.QPlainTextEdit(self.tab)
        self.Base64Input.setGeometry(QtCore.QRect(80, 20, 211, 91))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Base64Input.setFont(font)
        self.Base64Input.setFrameShape(QtWidgets.QFrame.Panel)
        self.Base64Input.setLineWidth(3)
        self.Base64Input.setPlainText("")
        self.Base64Input.setObjectName("Base64Input")
        self.Result = QtWidgets.QPlainTextEdit(self.tab)
        self.Result.setGeometry(QtCore.QRect(80, 130, 211, 101))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Result.setFont(font)
        self.Result.setFrameShape(QtWidgets.QFrame.Panel)
        self.Result.setLineWidth(3)
        self.Result.setReadOnly(True)
        self.Result.setObjectName("Result")
        self.tabWidget.addTab(self.tab, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setMinimumSize(QtCore.QSize(300, 300))
        self.tab_3.setMaximumSize(QtCore.QSize(300, 300))
        self.tab_3.setObjectName("tab_3")
        self.JSONInput = QtWidgets.QPlainTextEdit(self.tab_3)
        self.JSONInput.setGeometry(QtCore.QRect(0, 20, 141, 181))
        self.JSONInput.setFrameShape(QtWidgets.QFrame.Panel)
        self.JSONInput.setLineWidth(3)
        self.JSONInput.setReadOnly(False)
        self.JSONInput.setObjectName("JSONInput")
        self.JSONResult = QtWidgets.QPlainTextEdit(self.tab_3)
        self.JSONResult.setGeometry(QtCore.QRect(150, 20, 141, 181))
        self.JSONResult.setFrameShape(QtWidgets.QFrame.Panel)
        self.JSONResult.setLineWidth(3)
        self.JSONResult.setReadOnly(True)
        self.JSONResult.setObjectName("JSONResult")
        self.label_3 = QtWidgets.QLabel(self.tab_3)
        self.label_3.setGeometry(QtCore.QRect(0, 0, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.tab_3)
        self.label_4.setGeometry(QtCore.QRect(150, 0, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.Transform1 = QtWidgets.QPushButton(self.tab_3)
        self.Transform1.setGeometry(QtCore.QRect(64, 210, 171, 23))
        self.Transform1.setObjectName("Transform1")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setMinimumSize(QtCore.QSize(300, 300))
        self.tab_2.setMaximumSize(QtCore.QSize(300, 300))
        self.tab_2.setObjectName("tab_2")
        self.label_6 = QtWidgets.QLabel(self.tab_2)
        self.label_6.setGeometry(QtCore.QRect(10, 60, 150, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.FileName = QtWidgets.QLineEdit(self.tab_2)
        self.FileName.setGeometry(QtCore.QRect(10, 80, 271, 20))
        self.FileName.setObjectName("FileName")
        self.Transform2 = QtWidgets.QPushButton(self.tab_2)
        self.Transform2.setGeometry(QtCore.QRect(100, 130, 91, 61))
        self.Transform2.setObjectName("Transform2")
        self.tabWidget.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 300, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action1 = QtWidgets.QAction(MainWindow)
        self.action1.setCheckable(True)
        self.action1.setVisible(True)
        self.action1.setObjectName("action1")

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.Encode.clicked.connect(self.buttonClicked)
        self.Decode.clicked.connect(self.buttonClicked)
        self.Transform1.clicked.connect(self.buttonClicked)
        self.Transform2.clicked.connect(self.buttonClicked)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ToolBox"))
        self.Encode.setText(_translate("MainWindow", "Encode"))
        self.Decode.setText(_translate("MainWindow", "Decode"))
        self.label.setText(_translate("MainWindow", "Input Here:"))
        self.label_2.setText(_translate("MainWindow", "Result:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Base64"))
        self.label_3.setText(_translate("MainWindow", "Input Here:"))
        self.label_4.setText(_translate("MainWindow", "Result:"))
        self.Transform1.setText(_translate("MainWindow", "Transform"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "JSON"))
        self.label_6.setText(_translate("MainWindow", "File Path/Name:"))
        self.Transform2.setText(_translate("MainWindow", "Transform"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "QR Code"))
        self.action1.setText(_translate("MainWindow", "1"))

    def buttonClicked(self):
        sender = self.sender()
        st=self.Base64Input.toPlainText()
        if sender.objectName()=='Encode':
            self.Result.setPlainText(str(base64.b64encode(st.encode('utf-8')),'utf-8'))
        elif sender.objectName()=='Decode':
            try:
                self.Result.setPlainText(str(base64.b64decode(st.encode('utf-8')),'utf-8'))
            except :
                QMessageBox.information(self,'Error','Input Error!',QMessageBox.Ok)
        elif sender.objectName()=='Transform1':
            s=self.JSONInput.toPlainText()
            try:
                dic1=json.loads(s)
                dic2={}
                while len(dic1):
                    p=dic1.popitem()
                    if p[1] in dic2:
                        dic2[p[1]]=[dic2[p[1]],p[0]]
                    else:
                        dic2[p[1]]=p[0]
                jsn=json.dumps(dic2)
                self.JSONResult.setPlainText(str(dic2)+'\n'+str(type(dic2))+'\n'+str(jsn)+'\n'+str(type(jsn)))
            except:
                QMessageBox.information(self,'Error','Input Error!',QMessageBox.Ok)
        else:
            try:
                file=open(self.FileName.text(),'r')
                QRImagePath=os.getcwd()+'/QRcode.png'
                qr=qrcode.QRCode(
                    version=1,
                    error_correction=qrcode.constants.ERROR_CORRECT_L,
                    box_size=10,
                    border=2,
                )
                qr.add_data(file.readlines())
                img=qr.make_image()
                img.save('qrcode.png')
                QMessageBox.information(self,'Success','Done.',QMessageBox.Ok)
            except:
                QMessageBox.information(self,'Error','File Not Found!',QMessageBox.Ok)
            
