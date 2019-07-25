# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qtDetector_DESIGN.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(361, 222)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 341, 181))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.buttonIOCstart = QtGui.QPushButton(self.verticalLayoutWidget)
        self.buttonIOCstart.setObjectName(_fromUtf8("buttonIOCstart"))
        self.horizontalLayout.addWidget(self.buttonIOCstart)
        self.buttonIOCstop = QtGui.QPushButton(self.verticalLayoutWidget)
        self.buttonIOCstop.setObjectName(_fromUtf8("buttonIOCstop"))
        self.horizontalLayout.addWidget(self.buttonIOCstop)
        self.horizontalLayout.setStretch(0, 1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_2 = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_2.addWidget(self.label_2)
        self.buttonMEDMstart = QtGui.QPushButton(self.verticalLayoutWidget)
        self.buttonMEDMstart.setObjectName(_fromUtf8("buttonMEDMstart"))
        self.horizontalLayout_2.addWidget(self.buttonMEDMstart)
        self.buttonMEDMstop = QtGui.QPushButton(self.verticalLayoutWidget)
        self.buttonMEDMstop.setObjectName(_fromUtf8("buttonMEDMstop"))
        self.horizontalLayout_2.addWidget(self.buttonMEDMstop)
        self.horizontalLayout_2.setStretch(0, 1)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_3 = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_3.addWidget(self.label_3)
        self.buttonIMAGEJstart = QtGui.QPushButton(self.verticalLayoutWidget)
        self.buttonIMAGEJstart.setObjectName(_fromUtf8("buttonIMAGEJstart"))
        self.horizontalLayout_3.addWidget(self.buttonIMAGEJstart)
        self.buttonIMAGEJstop = QtGui.QPushButton(self.verticalLayoutWidget)
        self.buttonIMAGEJstop.setObjectName(_fromUtf8("buttonIMAGEJstop"))
        self.horizontalLayout_3.addWidget(self.buttonIMAGEJstop)
        self.horizontalLayout_3.setStretch(0, 1)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.label_4 = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout_4.addWidget(self.label_4)
        self.buttonSAVEstart = QtGui.QPushButton(self.verticalLayoutWidget)
        self.buttonSAVEstart.setObjectName(_fromUtf8("buttonSAVEstart"))
        self.horizontalLayout_4.addWidget(self.buttonSAVEstart)
        self.buttonSAVEstop = QtGui.QPushButton(self.verticalLayoutWidget)
        self.buttonSAVEstop.setObjectName(_fromUtf8("buttonSAVEstop"))
        self.horizontalLayout_4.addWidget(self.buttonSAVEstop)
        self.horizontalLayout_4.setStretch(0, 1)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 361, 24))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuDP_Launcher = QtGui.QMenu(self.menubar)
        self.menuDP_Launcher.setObjectName(_fromUtf8("menuDP_Launcher"))
        MainWindow.setMenuBar(self.menubar)
        self.actionDetector_Pool_Homepage = QtGui.QAction(MainWindow)
        self.actionDetector_Pool_Homepage.setObjectName(_fromUtf8("actionDetector_Pool_Homepage"))
        self.menuDP_Launcher.addAction(self.actionDetector_Pool_Homepage)
        self.menubar.addAction(self.menuDP_Launcher.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.label.setText(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\">EPICS IOC</span></p></body></html>", None))
        self.buttonIOCstart.setText(_translate("MainWindow", "Start", None))
        self.buttonIOCstop.setText(_translate("MainWindow", "Stop", None))
        self.label_2.setText(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\">MEDM</span></p></body></html>", None))
        self.buttonMEDMstart.setText(_translate("MainWindow", "Start", None))
        self.buttonMEDMstop.setText(_translate("MainWindow", "Stop", None))
        self.label_3.setText(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\">ImageJ</span></p></body></html>", None))
        self.buttonIMAGEJstart.setText(_translate("MainWindow", "Start", None))
        self.buttonIMAGEJstop.setText(_translate("MainWindow", "Stop", None))
        self.label_4.setText(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\">SaveRestore</span></p></body></html>", None))
        self.buttonSAVEstart.setText(_translate("MainWindow", "Start", None))
        self.buttonSAVEstop.setText(_translate("MainWindow", "Stop", None))
        self.menuDP_Launcher.setTitle(_translate("MainWindow", "Help", None))
        self.actionDetector_Pool_Homepage.setText(_translate("MainWindow", "Detector Pool Homepage...", None))
