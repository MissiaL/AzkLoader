# coding=utf-8

import logging
import traceback

from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt, QDateTime, pyqtSignal, QDir
from PyQt5.QtWidgets import QMainWindow, QApplication, QDialog, QMessageBox, QFileDialog

from GoupBoxShemaListDialog import Ui_DialogShemaList
from azk import Ui_MainWindow
from azkFinForm import Ui_DialogAzk
from configurator import Configurator
from db import getDbShemaList


class MainForm(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self.config = Configurator()
        self.setupUi(self)
        self.AzkForm = AzkForm(self)
        self.azkButton.clicked.connect(self.showAzkFinForm)
        self.AzkForm.lineEditPath.setText(self.config.getoption('dialog', 'path'))
        self.AzkForm.lineEditPort.setText(self.config.getoption('dialog', 'port'))

    def showAzkFinForm(self):
        self.AzkForm.show()

    def exception_hook(self, type_, value, tb):
        logging.error('Unhandled top level exception:\n%s', ''.join(traceback.format_exception(type_, value, tb)))
        QMessageBox.critical(self, "Ошибка", "{}".format(''.join(traceback.format_exception(type_, value, tb))))


class AzkForm(QDialog, Ui_DialogAzk):
    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        self.setupUi(self)
        self.pushButtonLoading.setDisabled(True)

        self.comboBoxDatabase.activated.connect(self.showFbPathButton)
        self.pushButtonShemaList.clicked.connect(self.showTableShemaList)
        self.toolButtonPath.clicked.connect(self.browse)
        self.pushButtonLoading.clicked.connect(self.downloading)
        self.lineEditVersionDownload.textChanged.connect(self.activatePushButtonLoading)
        self.lineEditPath.textChanged.connect(self.activatePushButtonLoading)

        self.table = TreeShemaForm(self)
        self.table.setTextToAzkFormLabel.connect(self.setTextToAzkFormLabel)

    def showFbPathButton(self):
        """
        Данный метод отвечает за формирование опций
        в зависисмости от типа выбранной базы данных
        """
        index = self.comboBoxDatabase.currentIndex()
        allLayouts = [name for name in self.HeadLayout.children()]
        print(len(allLayouts))
        if index:
            self.labelFbPath = QtWidgets.QLabel()
            self.labelFbPath.setObjectName("labelFbPath")
            self.labelFbPath.setText("Путь к бд")
            if self.labelFbPath not in self.gridLayoutLabelFbPath.children():
                self.gridLayoutLabelFbPath.addWidget(self.labelFbPath, 0, 0, 1, 1)

            self.lineEditFbPath = QtWidgets.QLineEdit()
            self.lineEditFbPath.setObjectName("lineEditFbPath")
            if self.lineEditFbPath not in self.gridLayoutLineEditFbPath.children():
                self.gridLayoutLineEditFbPath.addWidget(self.lineEditFbPath, 0, 0, 1, 1)
            self.labelShemaName.setText("Пользователь")
            self.lineEditShemaName.clear()
            self.lineEditShemaPassword.clear()

            self.pushButtonShemaList.hide()

        else:
            for i in reversed(range(self.gridLayoutLabelFbPath.count())):
                self.gridLayoutLabelFbPath.itemAt(i).widget().deleteLater()
            for i in reversed(range(self.gridLayoutLineEditFbPath.count())):
                self.gridLayoutLineEditFbPath.itemAt(i).widget().deleteLater()
            self.labelShemaName.setText("Имя схемы")
            self.pushButtonShemaList.show()

    def showTableShemaList(self):

        self.table.loadOracleShemasInfo()
        self.table.show()

    def setTextToAzkFormLabel(self):
        item = self.table.treeWidgetShemaList.currentItem()
        shema = item.text(0)
        version = item.text(1)
        self.lineEditShemaName.setText(shema)
        self.lineEditShemaPassword.setText(shema)
        self.lineEditVersionDownload.setText(version)
        self.table.hide()

    def browse(self):
        directory = QFileDialog.getExistingDirectory(self, "Выберите папку",
                                                     QDir.currentPath())
        if directory:
            self.lineEditPath.setText(directory)

    def activatePushButtonLoading(self):
        if self.comboBoxDatabase.currentText() == 'Oracle':
            if self.lineEditPath.displayText() and self.lineEditVersionDownload.displayText():
                self.pushButtonLoading.setDisabled(False)
        else:
            if self.lineEditVersionDownload.displayText():
                self.pushButtonLoading.setDisabled(False)

    def downloading(self):
        shema = None
        password = None
        port = None
        server = False
        client = False
        webserver = False
        version = self.lineEditVersionDownload.text().strip()
        path = self.lineEditPath.text().strip()
        if self.checkBoxServer.isChecked():
            server = True
        if self.checkBoxClient.isChecked():
            client = True
        if self.checkBoxWebServer.isChecked():
            webserver = True
        if self.lineEditPort.displayText():
            port = self.lineEditPort.text().strip()
        if self.lineEditShemaPassword.displayText():
            password = self.lineEditShemaPassword.text().strip()
        if self.lineEditShemaName.displayText():
            shema = self.lineEditShemaName.text().strip()


class TreeShemaForm(QDialog, Ui_DialogShemaList):
    setTextToAzkFormLabel = pyqtSignal()

    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        self.setupUi(self)
        self.treeWidgetShemaList.itemDoubleClicked.connect(self.setTextToAzkFormLabel)

    def loadAllMessages(self, item, column):
        print('dasdasd')

    def loadOracleShemasInfo(self):
        self.treeWidgetShemaList.clear()
        self.config = Configurator()
        server, sid, user, password = self.config.getdbparam()
        print(server, sid, user, password)
        for num, cur in enumerate(getDbShemaList(server, sid, user, password)):
            name = cur[0]
            version = cur[1]
            date = QDateTime(cur[2]).toString('yyyy-MM-dd')

            item_0 = QtWidgets.QTreeWidgetItem(self.treeWidgetShemaList)
            self.treeWidgetShemaList.insertTopLevelItem(num, item_0.setText(0, name))
            self.treeWidgetShemaList.insertTopLevelItem(num, item_0.setText(1, version))
            self.treeWidgetShemaList.insertTopLevelItem(num, item_0.setText(2, date))
        self.treeWidgetShemaList.sortByColumn(0, Qt.AscendingOrder)


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    ui = MainForm()
    sys.excepthook = ui.exception_hook
    ui.show()
    sys.exit(app.exec_())
