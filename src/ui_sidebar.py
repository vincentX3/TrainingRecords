# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\ui\sidebar.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from ui_settings import *


class Ui_sidebar(object):
    def setupUi(self, sidebar):
        sidebar.setObjectName("sidebar")
        sidebar.resize(SIDEBAR_WIDTH, HEIGHT)

        self.verticalLayout = QtWidgets.QVBoxLayout(sidebar)
        self.verticalLayout.setObjectName("verticalLayout")

        self.pushButton_train = QtWidgets.QPushButton(sidebar)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../res/muscle.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_train.setIcon(icon)
        self.pushButton_train.setFlat(False)
        self.pushButton_train.setObjectName("pushButton_train")
        self.verticalLayout.addWidget(self.pushButton_train)
        self.pushButton_history = QtWidgets.QPushButton(sidebar)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../res/history.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_history.setIcon(icon1)
        self.pushButton_history.setObjectName("pushButton_history")
        self.verticalLayout.addWidget(self.pushButton_history)
        self.pushButton_analysis = QtWidgets.QPushButton(sidebar)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../res/analysis.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_analysis.setIcon(icon2)
        self.pushButton_analysis.setObjectName("pushButton_analysis")
        self.verticalLayout.addWidget(self.pushButton_analysis)

        self.retranslateUi(sidebar)
        QtCore.QMetaObject.connectSlotsByName(sidebar)

    def retranslateUi(self, sidebar):
        _translate = QtCore.QCoreApplication.translate
        sidebar.setWindowTitle(_translate("sidebar", "Form"))
        self.pushButton_train.setText(_translate("sidebar", "训练"))
        self.pushButton_history.setText(_translate("sidebar", "历史"))
        self.pushButton_analysis.setText(_translate("sidebar", "统计"))
