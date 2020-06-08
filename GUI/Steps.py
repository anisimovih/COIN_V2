# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Steps.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(437, 347)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.group_box_left = QtWidgets.QGroupBox(Form)
        self.group_box_left.setObjectName("group_box_left")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.group_box_left)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout.addWidget(self.group_box_left)
        self.group_box_right = QtWidgets.QGroupBox(Form)
        self.group_box_right.setObjectName("group_box_right")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.group_box_right)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout.addWidget(self.group_box_right)
        self.verticalLayout_4.addLayout(self.horizontalLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.group_box_left.setTitle(_translate("Form", "Составляющие:"))
        self.group_box_right.setTitle(_translate("Form", "GroupBox"))
