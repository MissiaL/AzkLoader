# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Python\MissiaLProject\Sketches\AzkLoader\ui\DialogLog.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_DialogLog(object):
    def setupUi(self, DialogLog):
        DialogLog.setObjectName("DialogLog")
        DialogLog.resize(397, 397)
        DialogLog.setMinimumSize(QtCore.QSize(397, 397))
        DialogLog.setWindowTitle("Лог загрузки")
        self.horizontalLayout = QtWidgets.QHBoxLayout(DialogLog)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.textBrowser = QtWidgets.QTextBrowser(DialogLog)
        self.textBrowser.setObjectName("textBrowser")
        self.horizontalLayout_2.addWidget(self.textBrowser)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.pushButton = QtWidgets.QPushButton(DialogLog)
        self.pushButton.setEnabled(False)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.horizontalLayout.addLayout(self.verticalLayout)

        self.retranslateUi(DialogLog)
        QtCore.QMetaObject.connectSlotsByName(DialogLog)

    def retranslateUi(self, DialogLog):
        _translate = QtCore.QCoreApplication.translate
        self.textBrowser.setHtml(_translate("DialogLog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.pushButton.setText(_translate("DialogLog", "Готово"))

