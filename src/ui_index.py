# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './ui/index.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from ui_pages import *
from ui_macro import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(WIDTH, HEIGHT)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        # self.splitter.setSizes((1, 4))
        # self.splitter.setGeometry(QtCore.QRect(30, 50, 0, 0))
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")

        self.horizontalLayout.addWidget(self.splitter)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        # pages
        self.horizontalLayout.addWidget(self.splitter)
        self.home = Home()
        self.history = History()
        self.analysis = Analysis()
        self.sidebar = Sidebar()
        self.settings = Settings()
        self.splitter.addWidget(self.sidebar)

        # switch pages
        self.sidebar.pushButton_train.clicked.connect(lambda: self.switch_page("train"))
        self.sidebar.pushButton_history.clicked.connect(lambda: self.switch_page("history"))
        self.sidebar.pushButton_analysis.clicked.connect(lambda: self.switch_page("analysis"))
        self.sidebar.pushButton_settings.clicked.connect(lambda: self.switch_page("settings"))
        self.splitter.addWidget(self.home)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def switch_page(self, page_name):
        if page_name == 'train':
            self.splitter.widget(1).setParent(None)
            self.home.refresh_date()
            self.splitter.insertWidget(1, self.home)
        elif page_name == 'history':
            self.splitter.widget(1).setParent(None)
            self.history.refresh_date()
            self.splitter.insertWidget(1, self.history)
        elif page_name == 'analysis':
            self.splitter.widget(1).setParent(None)
            self.splitter.insertWidget(1, self.analysis)
        elif page_name == 'settings':
            self.splitter.widget(1).setParent(None)
            self.splitter.insertWidget(1, self.settings)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Keep Fit!"))
