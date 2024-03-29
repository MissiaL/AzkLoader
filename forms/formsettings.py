# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Python\MissiaLProject\Sketches\AzkLoader\ui\azkFinForm.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_DialogAzk(object):
    def setupUi(self, DialogAzk):
        DialogAzk.setObjectName("DialogAzk")
        DialogAzk.resize(397, 567)
        font = QtGui.QFont()
        font.setPointSize(14)
        DialogAzk.setFont(font)
        DialogAzk.setWindowTitle("Настройка выкачивания")
        DialogAzk.setToolTip("")
        DialogAzk.setStatusTip("")
        DialogAzk.setWhatsThis("")
        DialogAzk.setAccessibleName("")
        DialogAzk.setAccessibleDescription("")
        self.HeadLayout = QtWidgets.QGridLayout(DialogAzk)
        self.HeadLayout.setObjectName("HeadLayout")
        self.gridLayoutLineEditFbPath = QtWidgets.QGridLayout()
        self.gridLayoutLineEditFbPath.setObjectName("gridLayoutLineEditFbPath")
        self.HeadLayout.addLayout(self.gridLayoutLineEditFbPath, 7, 1, 1, 1)
        self.gridLayout_13 = QtWidgets.QGridLayout()
        self.gridLayout_13.setObjectName("gridLayout_13")
        self.lineEditShemaPassword = QtWidgets.QLineEdit(DialogAzk)
        self.lineEditShemaPassword.setObjectName("lineEditShemaPassword")
        self.gridLayout_13.addWidget(self.lineEditShemaPassword, 0, 0, 1, 1)
        self.HeadLayout.addLayout(self.gridLayout_13, 10, 1, 1, 1)
        self.gridLayout_15 = QtWidgets.QGridLayout()
        self.gridLayout_15.setObjectName("gridLayout_15")
        self.labelPort = QtWidgets.QLabel(DialogAzk)
        self.labelPort.setObjectName("labelPort")
        self.gridLayout_15.addWidget(self.labelPort, 0, 0, 1, 1)
        self.HeadLayout.addLayout(self.gridLayout_15, 11, 0, 1, 1)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.labelWhatDownload = QtWidgets.QLabel(DialogAzk)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.labelWhatDownload.setFont(font)
        self.labelWhatDownload.setToolTip("Необходимо выбрать компоненты, которые будут выкачены в папку")
        self.labelWhatDownload.setStatusTip("")
        self.labelWhatDownload.setWhatsThis("")
        self.labelWhatDownload.setAccessibleName("")
        self.labelWhatDownload.setAccessibleDescription("")
        self.labelWhatDownload.setObjectName("labelWhatDownload")
        self.gridLayout_3.addWidget(self.labelWhatDownload, 0, 0, 1, 1)
        self.HeadLayout.addLayout(self.gridLayout_3, 4, 0, 1, 1)
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.checkBoxServer = QtWidgets.QCheckBox(DialogAzk)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.checkBoxServer.setFont(font)
        self.checkBoxServer.setToolTip("")
        self.checkBoxServer.setStatusTip("")
        self.checkBoxServer.setWhatsThis("")
        self.checkBoxServer.setAccessibleName("")
        self.checkBoxServer.setAccessibleDescription("")
        self.checkBoxServer.setText("Сервер")
        self.checkBoxServer.setChecked(True)
        self.checkBoxServer.setObjectName("checkBoxServer")
        self.gridLayout_4.addWidget(self.checkBoxServer, 1, 0, 1, 1)
        self.checkBoxWebServer = QtWidgets.QCheckBox(DialogAzk)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.checkBoxWebServer.setFont(font)
        self.checkBoxWebServer.setToolTip("")
        self.checkBoxWebServer.setStatusTip("")
        self.checkBoxWebServer.setWhatsThis("")
        self.checkBoxWebServer.setAccessibleName("")
        self.checkBoxWebServer.setAccessibleDescription("")
        self.checkBoxWebServer.setText("Web сервер")
        self.checkBoxWebServer.setShortcut("")
        self.checkBoxWebServer.setObjectName("checkBoxWebServer")
        self.gridLayout_4.addWidget(self.checkBoxWebServer, 1, 2, 1, 1)
        self.checkBoxClient = QtWidgets.QCheckBox(DialogAzk)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.checkBoxClient.setFont(font)
        self.checkBoxClient.setToolTip("")
        self.checkBoxClient.setStatusTip("")
        self.checkBoxClient.setWhatsThis("")
        self.checkBoxClient.setAccessibleName("")
        self.checkBoxClient.setAccessibleDescription("")
        self.checkBoxClient.setText("Клиент")
        self.checkBoxClient.setShortcut("")
        self.checkBoxClient.setChecked(True)
        self.checkBoxClient.setObjectName("checkBoxClient")
        self.gridLayout_4.addWidget(self.checkBoxClient, 1, 1, 1, 1)
        self.HeadLayout.addLayout(self.gridLayout_4, 4, 1, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.labelVersionDownload = QtWidgets.QLabel(DialogAzk)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.labelVersionDownload.setFont(font)
        self.labelVersionDownload.setToolTip("Необходимо указать версию. Например 2.39.109")
        self.labelVersionDownload.setStatusTip("")
        self.labelVersionDownload.setWhatsThis("")
        self.labelVersionDownload.setAccessibleName("")
        self.labelVersionDownload.setAccessibleDescription("")
        self.labelVersionDownload.setObjectName("labelVersionDownload")
        self.gridLayout_2.addWidget(self.labelVersionDownload, 0, 0, 1, 1)
        self.HeadLayout.addLayout(self.gridLayout_2, 0, 0, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.lineEditVersionDownload = QtWidgets.QLineEdit(DialogAzk)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineEditVersionDownload.setFont(font)
        self.lineEditVersionDownload.setText("")
        self.lineEditVersionDownload.setObjectName("lineEditVersionDownload")
        self.gridLayout.addWidget(self.lineEditVersionDownload, 0, 0, 1, 1)
        self.HeadLayout.addLayout(self.gridLayout, 0, 1, 1, 1)
        self.gridLayout_7 = QtWidgets.QGridLayout()
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.labelPath = QtWidgets.QLabel(DialogAzk)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.labelPath.setFont(font)
        self.labelPath.setToolTip("Путь к папке. Например: C:\\soft\\sborki")
        self.labelPath.setStatusTip("")
        self.labelPath.setWhatsThis("")
        self.labelPath.setAccessibleName("")
        self.labelPath.setAccessibleDescription("")
        self.labelPath.setObjectName("labelPath")
        self.gridLayout_7.addWidget(self.labelPath, 0, 0, 1, 1)
        self.HeadLayout.addLayout(self.gridLayout_7, 5, 0, 1, 1)
        self.pushButtonLoading = QtWidgets.QPushButton(DialogAzk)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButtonLoading.setFont(font)
        self.pushButtonLoading.setObjectName("pushButtonLoading")
        self.HeadLayout.addWidget(self.pushButtonLoading, 12, 1, 1, 1)
        self.gridLayout_16 = QtWidgets.QGridLayout()
        self.gridLayout_16.setObjectName("gridLayout_16")
        self.lineEditPort = QtWidgets.QLineEdit(DialogAzk)
        self.lineEditPort.setObjectName("lineEditPort")
        self.gridLayout_16.addWidget(self.lineEditPort, 0, 0, 1, 1)
        self.HeadLayout.addLayout(self.gridLayout_16, 11, 1, 1, 1)
        self.gridLayout_10 = QtWidgets.QGridLayout()
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.comboBoxDatabase = QtWidgets.QComboBox(DialogAzk)
        self.comboBoxDatabase.setObjectName("comboBoxDatabase")
        self.comboBoxDatabase.addItem("")
        self.comboBoxDatabase.addItem("")
        self.gridLayout_10.addWidget(self.comboBoxDatabase, 1, 0, 1, 1)
        self.HeadLayout.addLayout(self.gridLayout_10, 6, 1, 1, 1)
        self.gridLayout_6 = QtWidgets.QGridLayout()
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.lineEditPath = QtWidgets.QLineEdit(DialogAzk)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineEditPath.setFont(font)
        self.lineEditPath.setToolTip("")
        self.lineEditPath.setStatusTip("")
        self.lineEditPath.setWhatsThis("")
        self.lineEditPath.setAccessibleName("")
        self.lineEditPath.setAccessibleDescription("")
        self.lineEditPath.setInputMask("")
        self.lineEditPath.setText("")
        self.lineEditPath.setPlaceholderText("")
        self.lineEditPath.setObjectName("lineEditPath")
        self.gridLayout_6.addWidget(self.lineEditPath, 0, 0, 1, 1)
        self.toolButtonPath = QtWidgets.QToolButton(DialogAzk)
        self.toolButtonPath.setObjectName("toolButtonPath")
        self.gridLayout_6.addWidget(self.toolButtonPath, 0, 1, 1, 1)
        self.HeadLayout.addLayout(self.gridLayout_6, 5, 1, 1, 1)
        self.gridLayout_14 = QtWidgets.QGridLayout()
        self.gridLayout_14.setObjectName("gridLayout_14")
        self.labelShemaPassword = QtWidgets.QLabel(DialogAzk)
        self.labelShemaPassword.setObjectName("labelShemaPassword")
        self.gridLayout_14.addWidget(self.labelShemaPassword, 0, 0, 1, 1)
        self.HeadLayout.addLayout(self.gridLayout_14, 10, 0, 1, 1)
        self.gridLayout_9 = QtWidgets.QGridLayout()
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.labelDatabase = QtWidgets.QLabel(DialogAzk)
        self.labelDatabase.setObjectName("labelDatabase")
        self.gridLayout_9.addWidget(self.labelDatabase, 0, 0, 1, 1)
        self.HeadLayout.addLayout(self.gridLayout_9, 6, 0, 1, 1)
        self.gridLayout_11 = QtWidgets.QGridLayout()
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.labelShemaName = QtWidgets.QLabel(DialogAzk)
        self.labelShemaName.setObjectName("labelShemaName")
        self.gridLayout_11.addWidget(self.labelShemaName, 0, 0, 1, 1)
        self.HeadLayout.addLayout(self.gridLayout_11, 8, 0, 1, 1)
        self.gridLayout_8 = QtWidgets.QGridLayout()
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.gridLayout_12 = QtWidgets.QGridLayout()
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.lineEditShemaName = QtWidgets.QLineEdit(DialogAzk)
        self.lineEditShemaName.setObjectName("lineEditShemaName")
        self.gridLayout_12.addWidget(self.lineEditShemaName, 0, 0, 1, 1)
        self.gridLayout_8.addLayout(self.gridLayout_12, 0, 0, 1, 1)
        self.HeadLayout.addLayout(self.gridLayout_8, 8, 1, 1, 1)
        self.gridLayoutLabelFbPath = QtWidgets.QGridLayout()
        self.gridLayoutLabelFbPath.setObjectName("gridLayoutLabelFbPath")
        self.HeadLayout.addLayout(self.gridLayoutLabelFbPath, 7, 0, 1, 1)
        self.gridLayoutShemaList = QtWidgets.QGridLayout()
        self.gridLayoutShemaList.setObjectName("gridLayoutShemaList")
        self.pushButtonShemaList = QtWidgets.QPushButton(DialogAzk)
        self.pushButtonShemaList.setObjectName("pushButtonShemaList")
        self.gridLayoutShemaList.addWidget(self.pushButtonShemaList, 0, 0, 1, 1)
        self.HeadLayout.addLayout(self.gridLayoutShemaList, 9, 1, 1, 1)
        self.gridLayout_18 = QtWidgets.QGridLayout()
        self.gridLayout_18.setObjectName("gridLayout_18")
        self.pushButtonReport = QtWidgets.QPushButton(DialogAzk)
        self.pushButtonReport.setObjectName("pushButtonReport")
        self.gridLayout_18.addWidget(self.pushButtonReport, 0, 0, 1, 1)
        self.HeadLayout.addLayout(self.gridLayout_18, 3, 1, 1, 1)
        self.gridLayout_17 = QtWidgets.QGridLayout()
        self.gridLayout_17.setObjectName("gridLayout_17")
        self.label = QtWidgets.QLabel(DialogAzk)
        self.label.setToolTip("Можно не указывать")
        self.label.setObjectName("label")
        self.gridLayout_17.addWidget(self.label, 0, 0, 1, 1)
        self.HeadLayout.addLayout(self.gridLayout_17, 2, 0, 1, 1)
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.lineEditReport = QtWidgets.QLineEdit(DialogAzk)
        self.lineEditReport.setObjectName("lineEditReport")
        self.gridLayout_5.addWidget(self.lineEditReport, 0, 0, 1, 1)
        self.HeadLayout.addLayout(self.gridLayout_5, 2, 1, 1, 1)
        self.gridLayout_19 = QtWidgets.QGridLayout()
        self.gridLayout_19.setObjectName("gridLayout_19")
        self.pushButtonVersion = QtWidgets.QPushButton(DialogAzk)
        self.pushButtonVersion.setObjectName("pushButtonVersion")
        self.gridLayout_19.addWidget(self.pushButtonVersion, 0, 0, 1, 1)
        self.HeadLayout.addLayout(self.gridLayout_19, 1, 1, 1, 1)

        self.retranslateUi(DialogAzk)
        QtCore.QMetaObject.connectSlotsByName(DialogAzk)

    def retranslateUi(self, DialogAzk):
        _translate = QtCore.QCoreApplication.translate
        self.labelPort.setToolTip(_translate("DialogAzk", "Можно не указывать"))
        self.labelPort.setText(_translate("DialogAzk", "Порт"))
        self.labelWhatDownload.setText(_translate("DialogAzk", "Выкачиваем"))
        self.labelVersionDownload.setText(_translate("DialogAzk", "Версия сборки"))
        self.labelPath.setText(_translate("DialogAzk", "Путь"))
        self.pushButtonLoading.setText(_translate("DialogAzk", "Скачать"))
        self.comboBoxDatabase.setItemText(0, _translate("DialogAzk", "Oracle"))
        self.comboBoxDatabase.setItemText(1, _translate("DialogAzk", "Firebird"))
        self.toolButtonPath.setText(_translate("DialogAzk", "..."))
        self.labelShemaPassword.setToolTip(_translate("DialogAzk", "Можно не указывать"))
        self.labelShemaPassword.setText(_translate("DialogAzk", "Пароль"))
        self.labelDatabase.setText(_translate("DialogAzk", "Тип бд"))
        self.labelShemaName.setToolTip(_translate("DialogAzk", "Можно не указывать"))
        self.labelShemaName.setText(_translate("DialogAzk", "Имя схемы"))
        self.pushButtonShemaList.setText(_translate("DialogAzk", "Список схем"))
        self.pushButtonReport.setText(_translate("DialogAzk", "Список отчетов"))
        self.label.setText(_translate("DialogAzk", "Путь к отчетам"))
        self.pushButtonVersion.setText(_translate("DialogAzk", "Список версий"))

