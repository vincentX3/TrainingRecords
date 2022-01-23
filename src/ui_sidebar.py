# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\ui\sidebar.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QLabel

from ui_macro import *


class Ui_sidebar(object):
    def setupUi(self, sidebar):
        sidebar.setObjectName("sidebar")
        sidebar.resize(SIDEBAR_WIDTH, HEIGHT)

        self.verticalLayout = QtWidgets.QVBoxLayout(sidebar)
        self.verticalLayout.setObjectName("verticalLayout")

        self.label_title = QLabel()
        self.label_title.setText("变强")
        self.label_title.setObjectName("label_title")
        self.label_title.setStyleSheet("font-family:'汉仪尚巍手书W'; font-size: 64px;")
        self.label_title.setAlignment(Qt.AlignCenter)
        self.label_icon = QLabel()
        # self.label_icon.setPixmap(QtGui.QPixmap("../res/onepunch.png").scaled(self.label_icon.width(),
        #                                                                       self.label_icon.height(),
        #                                                                       Qt.KeepAspectRatioByExpanding))
        self.label_icon.setPixmap(QtGui.QPixmap("../res/Saitama-PNG-Clipart.png").scaled(200, 200, Qt.KeepAspectRatio))
        self.label_icon.setAlignment(Qt.AlignCenter)

        self.pushButton_train = QtWidgets.QPushButton(sidebar)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../res/muscle.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_train.setIcon(icon)
        self.pushButton_train.setFlat(False)
        self.pushButton_train.setObjectName("pushButton_train")

        self.pushButton_history = QtWidgets.QPushButton(sidebar)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../res/history.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_history.setIcon(icon1)
        self.pushButton_history.setObjectName("pushButton_history")

        self.pushButton_analysis = QtWidgets.QPushButton(sidebar)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../res/analysis.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_analysis.setIcon(icon2)
        self.pushButton_analysis.setObjectName("pushButton_analysis")

        self.pushButton_settings = QtWidgets.QPushButton(sidebar)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("../res/setting.png"),QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_settings.setIcon(icon4)
        self.pushButton_settings.setObjectName("pushButton_settings")

        self.verticalLayout.addWidget(self.label_title)
        # self.verticalLayout.addStretch(1)
        self.verticalLayout.addWidget(self.label_icon)
        self.verticalLayout.addWidget(self.pushButton_train)
        self.verticalLayout.addWidget(self.pushButton_history)
        self.verticalLayout.addWidget(self.pushButton_analysis)
        self.verticalLayout.addWidget(self.pushButton_settings)
        self.verticalLayout.addStretch(1)

        self.retranslateUi(sidebar)
        QtCore.QMetaObject.connectSlotsByName(sidebar)

    def retranslateUi(self, sidebar):
        _translate = QtCore.QCoreApplication.translate
        sidebar.setWindowTitle(_translate("sidebar", "Form"))
        self.pushButton_train.setText(_translate("sidebar", "训练"))
        self.pushButton_history.setText(_translate("sidebar", "历史"))
        self.pushButton_analysis.setText(_translate("sidebar", "统计"))
        self.pushButton_settings.setText(_translate("sidebar", "设置"))
