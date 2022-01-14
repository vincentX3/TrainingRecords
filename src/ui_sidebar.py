# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\ui\sidebar.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_sidebar(object):
    def setupUi(self, sidebar):
        sidebar.setObjectName("sidebar")
        sidebar.resize(400, 705)
        self.verticalLayoutWidget = QtWidgets.QWidget(sidebar)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(70, 100, 271, 481))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.pushButton_train = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_train.setObjectName("pushButton_train")
        self.verticalLayout_2.addWidget(self.pushButton_train)
        self.pushButton_history = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_history.setObjectName("pushButton_history")
        self.verticalLayout_2.addWidget(self.pushButton_history)
        self.pushButton_analysis = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_analysis.setObjectName("pushButton_analysis")
        self.verticalLayout_2.addWidget(self.pushButton_analysis)

        self.retranslateUi(sidebar)
        QtCore.QMetaObject.connectSlotsByName(sidebar)

    def retranslateUi(self, sidebar):
        _translate = QtCore.QCoreApplication.translate
        sidebar.setWindowTitle(_translate("sidebar", "Form"))
        self.pushButton_train.setText(_translate("sidebar", "训练"))
        self.pushButton_history.setText(_translate("sidebar", "历史"))
        self.pushButton_analysis.setText(_translate("sidebar", "统计"))

