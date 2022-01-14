# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\ui\analysis.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_analysis(object):
    def setupUi(self, analysis):
        analysis.setObjectName("analysis")
        analysis.resize(1106, 756)
        self.label = QtWidgets.QLabel(analysis)
        self.label.setGeometry(QtCore.QRect(480, 380, 108, 24))
        self.label.setObjectName("label")

        self.retranslateUi(analysis)
        QtCore.QMetaObject.connectSlotsByName(analysis)

    def retranslateUi(self, analysis):
        _translate = QtCore.QCoreApplication.translate
        analysis.setWindowTitle(_translate("analysis", "Form"))
        self.label.setText(_translate("analysis", "analysis"))


