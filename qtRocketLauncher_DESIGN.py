# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qtRocketLauncher_DESIGN.ui'
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
        MainWindow.resize(360, 94)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.horizontalLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(8, 10, 341, 51))
        self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.comboBox = QtGui.QComboBox(self.horizontalLayoutWidget)
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.horizontalLayout.addWidget(self.comboBox)
        self.buttonLoad = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.buttonLoad.setObjectName(_fromUtf8("buttonLoad"))
        self.horizontalLayout.addWidget(self.buttonLoad)
        self.horizontalLayout.setStretch(0, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 360, 24))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        MainWindow.setMenuBar(self.menubar)
        self.actionDetector_Pool_Homepage = QtGui.QAction(MainWindow)
        self.actionDetector_Pool_Homepage.setObjectName(_fromUtf8("actionDetector_Pool_Homepage"))
        self.menuHelp.addAction(self.actionDetector_Pool_Homepage)
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.comboBox.setItemText(0, _translate("MainWindow", "Select Detector...", None))
        self.buttonLoad.setText(_translate("MainWindow", "Load", None))
        self.menuHelp.setTitle(_translate("MainWindow", "Help", None))
        self.actionDetector_Pool_Homepage.setText(_translate("MainWindow", "Detector Pool Homepage", None))
