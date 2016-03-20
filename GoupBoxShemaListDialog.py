# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Python\MissiaLProject\Sketches\gui\GoupBoxShemaListDialog.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_DialogShemaList(object):
    def setupUi(self, DialogShemaList):
        DialogShemaList.setObjectName("DialogShemaList")
        DialogShemaList.setWindowModality(QtCore.Qt.NonModal)
        DialogShemaList.resize(841, 694)
        DialogShemaList.setMinimumSize(QtCore.QSize(841, 694))
        font = QtGui.QFont()
        font.setPointSize(14)
        DialogShemaList.setFont(font)
        DialogShemaList.setWindowTitle("Список схем")
        DialogShemaList.setToolTip("")
        DialogShemaList.setStatusTip("")
        DialogShemaList.setWhatsThis("")
        DialogShemaList.setAccessibleName("")
        DialogShemaList.setAccessibleDescription("")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(DialogShemaList)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.gridLayoutShemaList = QtWidgets.QGridLayout()
        self.gridLayoutShemaList.setObjectName("gridLayoutShemaList")
        self.groupBoxShemaList = QtWidgets.QGroupBox(DialogShemaList)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.groupBoxShemaList.setFont(font)
        self.groupBoxShemaList.setToolTip("")
        self.groupBoxShemaList.setStatusTip("")
        self.groupBoxShemaList.setWhatsThis("")
        self.groupBoxShemaList.setAccessibleName("")
        self.groupBoxShemaList.setAccessibleDescription("")
        self.groupBoxShemaList.setTitle("select * from user$ ")
        self.groupBoxShemaList.setObjectName("groupBoxShemaList")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBoxShemaList)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayoutShemaList = QtWidgets.QHBoxLayout()
        self.horizontalLayoutShemaList.setObjectName("horizontalLayoutShemaList")
        self.treeWidgetShemaList = QtWidgets.QTreeWidget(self.groupBoxShemaList)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.treeWidgetShemaList.setFont(font)
        self.treeWidgetShemaList.setAlternatingRowColors(True)
        self.treeWidgetShemaList.setAnimated(False)
        self.treeWidgetShemaList.setAllColumnsShowFocus(False)
        self.treeWidgetShemaList.setObjectName("treeWidgetShemaList")
        self.treeWidgetShemaList.headerItem().setText(0, "Имя схемы")
        self.treeWidgetShemaList.headerItem().setText(1, "Версия")
        self.treeWidgetShemaList.headerItem().setText(2, "Дата создания")
        self.treeWidgetShemaList.header().setCascadingSectionResizes(True)
        self.treeWidgetShemaList.header().setDefaultSectionSize(318)
        self.treeWidgetShemaList.header().setHighlightSections(False)
        self.treeWidgetShemaList.header().setMinimumSectionSize(60)
        self.treeWidgetShemaList.header().setStretchLastSection(True)
        self.horizontalLayoutShemaList.addWidget(self.treeWidgetShemaList)
        self.verticalLayout_2.addLayout(self.horizontalLayoutShemaList)
        self.gridLayoutShemaList.addWidget(self.groupBoxShemaList, 0, 0, 1, 1)
        self.horizontalLayout_2.addLayout(self.gridLayoutShemaList)

        self.retranslateUi(DialogShemaList)
        QtCore.QMetaObject.connectSlotsByName(DialogShemaList)

    def retranslateUi(self, DialogShemaList):
        _translate = QtCore.QCoreApplication.translate
        self.treeWidgetShemaList.setSortingEnabled(True)

