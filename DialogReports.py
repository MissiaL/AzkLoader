# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Python\MissiaLProject\Sketches\AzkLoader\ui\DialogReports.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_DialogReports(object):
    def setupUi(self, DialogReports):
        DialogReports.setObjectName("DialogReports")
        DialogReports.resize(841, 694)
        DialogReports.setMinimumSize(QtCore.QSize(841, 694))
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(DialogReports)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.treeWidget = QtWidgets.QTreeWidget(DialogReports)
        self.treeWidget.setObjectName("treeWidget")
        self.treeWidget.header().setVisible(True)
        self.treeWidget.header().setCascadingSectionResizes(True)
        self.treeWidget.header().setDefaultSectionSize(300)
        self.treeWidget.header().setHighlightSections(False)
        self.treeWidget.header().setMinimumSectionSize(350)
        self.verticalLayout_2.addWidget(self.treeWidget)
        self.horizontalLayout_3.addLayout(self.verticalLayout_2)
        self.horizontalLayout_2.addLayout(self.horizontalLayout_3)

        self.retranslateUi(DialogReports)
        QtCore.QMetaObject.connectSlotsByName(DialogReports)

    def retranslateUi(self, DialogReports):
        _translate = QtCore.QCoreApplication.translate
        DialogReports.setWindowTitle(_translate("DialogReports", "Список версий"))
        self.treeWidget.setSortingEnabled(True)
        self.treeWidget.headerItem().setText(0, _translate("DialogReports", "Версия"))
        self.treeWidget.headerItem().setText(1, _translate("DialogReports", "Путь"))

