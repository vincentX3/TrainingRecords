# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './ui/index.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from ui_pages import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1654, 1141)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        # self.splitter.setGeometry(QtCore.QRect(30, 50, 0, 0))
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        # pages
        self.horizontalLayout.addWidget(self.splitter)
        self.home = Home()
        self.history = History()
        self.sidebar = Sidebar()
        self.analysis = Analysis()
        self.splitter.addWidget(self.sidebar)

        # switch pages
        self.sidebar.pushButton_train.clicked.connect(lambda: self.switch_page("train"))
        self.sidebar.pushButton_history.clicked.connect(lambda: self.switch_page("history"))
        self.sidebar.pushButton_analysis.clicked.connect(lambda: self.switch_page("analysis"))
        self.splitter.addWidget(self.home)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def switch_page(self, page_name):
        if page_name == 'train':
            self.splitter.widget(1).setParent(None)
            self.splitter.insertWidget(1, self.home)
        elif page_name == 'history':
            self.splitter.widget(1).setParent(None)
            self.splitter.insertWidget(1, self.history)
        elif page_name == 'analysis':
            self.splitter.widget(1).setParent(None)
            self.splitter.insertWidget(1, self.analysis)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
