# coding=utf-8

import logging
import os
import re
import shutil
import subprocess as sp
import traceback

from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt, QDateTime, pyqtSignal, QDir, QThread
from PyQt5.QtWidgets import QMainWindow, QApplication, QDialog, QMessageBox, QFileDialog

import replacer
from configurator import Configurator
from db import getDbShemaList
from forms.formheadwindow import Ui_MainWindow
from forms.formlog import Ui_DialogLog
from forms.formsettings import Ui_DialogAzk
from forms.formshemalist import Ui_DialogShemaList
from forms.formversionlist import Ui_DialogReports


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
        self.config = Configurator()
        self.setupUi(self)
        self.pushButtonLoading.setDisabled(True)

        self.comboBoxDatabase.activated.connect(self.showFbPathButton)
        self.pushButtonShemaList.clicked.connect(self.showTableShemaList)
        self.toolButtonPath.clicked.connect(self.browse)
        self.pushButtonLoading.clicked.connect(self.downloading)
        self.lineEditVersionDownload.textChanged.connect(self.activatePushButtonLoading)
        self.lineEditPath.textChanged.connect(self.activatePushButtonLoading)
        self.lineEditReport.textChanged.connect(self.activatePushButtonLoading)
        self.pushButtonReport.clicked.connect(self.viewReports)
        self.pushButtonVersion.clicked.connect(self.viewVersion)

        self.table = TreeShemaForm(self)
        self.table.setTextToAzkFormLabel.connect(self.setTextToAzkFormLabel)

        self.reportDialog = DialogReports(self)
        self.reportDialog.setTextToLineEditReport.connect(self.setTextlineEditReport)

        self.DialogLog = DialogLog(self)

        self.versiondict = {}
        self.reportdict = {}

        self.pathReport1 = self.config.getoption('azkfin', 'report1')
        self.pathReport2 = self.config.getoption('azkfin', 'report2')
        self.pathVersion1 = self.config.getoption('azkfin', 'path1')
        self.pathVersion2 = self.config.getoption('azkfin', 'path2')
        self.extr = self.config.getoption('dialog', '7z')

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
        directory = QFileDialog.getExistingDirectory(self, "Выберите папку", QDir.currentPath())
        if directory:
            self.lineEditPath.setText(directory)

    def activatePushButtonLoading(self):
        if self.comboBoxDatabase.currentText() == 'Oracle':
            if self.lineEditPath.displayText() and self.lineEditVersionDownload.displayText():
                self.pushButtonLoading.setDisabled(False)
            if self.lineEditReport.displayText():
                self.pushButtonLoading.setDisabled(False)
        else:
            if self.lineEditVersionDownload.displayText():
                self.pushButtonLoading.setDisabled(False)

    def viewReports(self):
        d = re.compile('\A\d.*')
        files1 = [os.path.join(self.pathReport1, f) for f in os.listdir(self.pathReport1) if re.search(d, f)]
        for file in files1:
            reports = os.listdir(file)
            for report in reports:
                self.reportdict[report] = os.path.join(file, report)
        r = re.compile('\Arep.*')
        files2 = [f for f in os.listdir(self.pathReport2) if re.search(r, f)]
        for report in files2:
            self.reportdict[report] = os.path.join(self.pathReport2, report)
        self.reportDialog.treeWidget.clear()
        for num, key in enumerate(self.reportdict):
            item_1 = QtWidgets.QTreeWidgetItem(self.reportDialog.treeWidget)
            self.reportDialog.treeWidget.insertTopLevelItem(num, item_1.setText(0, key))
            self.reportDialog.treeWidget.insertTopLevelItem(num,
                                                            item_1.setText(1, os.path.normpath(self.reportdict[key])))
        self.reportDialog.treeWidget.sortByColumn(0, Qt.DescendingOrder)
        self.reportDialog.treeWidget.headerItem().setText(0, "Версия отчета")
        self.reportDialog.show()

    def setTextlineEditReport(self):
        item = self.reportDialog.treeWidget.currentItem()
        version = item.text(0)
        reportPath = item.text(1)
        if self.reportDialog.treeWidget.headerItem().text(0) == 'Версия отчета':
            self.lineEditReport.setText(reportPath)
        else:
            self.lineEditVersionDownload.setText(version)
        self.reportDialog.hide()
        self.reportDialog.treeWidget.clear()

    def viewVersion(self):
        d = re.compile('\A\d\.')
        files1 = [os.path.join(self.pathVersion1, f) for f in os.listdir(self.pathVersion1) if re.search(d, f)]

        for folder in files1:
            versions = [f for f in os.listdir(folder) if re.search(d, f)]
            for version in versions:
                self.versiondict[version] = os.path.join(folder, version)
        files2 = [f for f in os.listdir(self.pathVersion2) if re.search(d, f)]
        for folder in files2:
            self.versiondict[folder] = os.path.join(self.pathVersion2, folder)
        self.reportDialog.treeWidget.clear()
        for num, key in enumerate(self.versiondict):
            item_1 = QtWidgets.QTreeWidgetItem(self.reportDialog.treeWidget)
            self.reportDialog.treeWidget.insertTopLevelItem(num, item_1.setText(0, key))
            self.reportDialog.treeWidget.insertTopLevelItem(num,
                                                            item_1.setText(1, os.path.normpath(self.versiondict[key])))
        self.reportDialog.treeWidget.sortByColumn(0, Qt.DescendingOrder)
        self.reportDialog.treeWidget.headerItem().setText(0, "Версия сборки")
        self.reportDialog.show()

    def downloading(self):
        shema = None
        password = None
        port = None
        report = None
        version = self.lineEditVersionDownload.text().strip()
        path = self.lineEditPath.text().strip()
        files = []
        if self.checkBoxServer.isChecked():
            files.append('server.zip')
        if self.checkBoxClient.isChecked():
            files.append('client.zip')
        if self.checkBoxWebServer.isChecked():
            files.extend(['apache-tomcat-6.0.29_BFT-1.0.zip', 'azk.war'])
        if self.lineEditPort.displayText():
            port = self.lineEditPort.text().strip()
        if self.lineEditShemaPassword.displayText():
            password = self.lineEditShemaPassword.text().strip()
        if self.lineEditShemaName.displayText():
            shema = self.lineEditShemaName.text().strip()
        if self.lineEditReport.displayText():
            report = self.lineEditReport.text().strip()
        self.DialogLog.textBrowser.clear()
        self.DialogLog.show()
        homefolder = os.path.join(self.lineEditPath.text(), version)
        if files:
            if version:
                if self.versiondict:
                    if version in self.versiondict:
                        headfolder = self.versiondict[version]
                        files = [os.path.join(headfolder, i) for i in files]
                    else:
                        headfolder = self.checkPathVersion(version)
                        files = [os.path.join(headfolder, i) for i in files]
                else:
                    self.checkPathVersion(version)
                    headfolder = self.checkPathVersion(version)
                    files = [os.path.join(headfolder, i) for i in files]

        if report is not None:
            report = report.replace("\\", "/")
            files.append(report)
        if not version:
            files = []
            files.append(report)
            destination = os.path.join(homefolder, os.path.basename(report))
            self.DialogLog.startLoadVersion(files, destination, self.extr)
        else:
            destination = homefolder
            self.DialogLog.startLoadVersion(files, destination, self.extr, shema, password, port, report=True)

    def checkPathVersion(self, version):
        versionFolder = '.'.join(version.split('.')[:2])
        path1 = os.path.join(self.pathVersion1, versionFolder, version)
        path2 = os.path.join(self.pathVersion2, version)
        if os.path.isdir(path1):
            headfolder = path1
            return headfolder
        elif os.path.isdir(path2):
            headfolder = path2
            return headfolder
        else:
            QMessageBox.warning(self, 'Сообщение', 'Версия {} не найдена!'.format(version))
            return

    def textadd(self):
        self.DialogLog.plainTextEdit.setPlainText('FFFFFFFFFFF')


class TreeShemaForm(QDialog, Ui_DialogShemaList):
    setTextToAzkFormLabel = pyqtSignal()

    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        self.setupUi(self)
        self.treeWidgetShemaList.itemDoubleClicked.connect(self.setTextToAzkFormLabel)

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


class DialogReports(QDialog, Ui_DialogReports):
    setTextToLineEditReport = pyqtSignal()

    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        self.setupUi(self)
        self.treeWidget.itemDoubleClicked.connect(self.setTextToLineEditReport)


class ThreadCopy(QThread):
    signal = pyqtSignal(str)
    buttonEnable = pyqtSignal(bool)

    def __init__(self, files, destination, extr, shema=None, password=None, port=None, report=False):
        QThread.__init__(self)
        self.files = files
        self.destination = destination
        self.extr = extr
        self.report = report
        self.shema = shema
        self.password = password
        self.port = port

    def __del__(self):
        self.wait()

    def run(self):
        self.startcopy(self.files, self.destination)
        os.chdir(self.destination)
        self.startextract(self.extr)
        self.configurator()
        self.buttonEnable.emit(False)

    def startcopy(self, files, destination):
        for file in files:
            self.signal.emit('Выкачиваем {0} в {1}...\n'.format(os.path.normpath(file), destination))
            shutil.copy(file, destination)
        self.signal.emit('Выкачивание завершено\n')

    def startextract(self, extr):
        files = os.listdir('.')
        for file in files:
            if file == 'server.zip':
                self.signal.emit('Извлекаем {}...\n'.format(file))
                sp.call(extr + ' x ' + file)
                self.signal.emit('Извлечение завершено\n')
        for file in files:
            if file == 'client.zip':
                self.signal.emit('Извлекаем {}...\n'.format(file))
                sp.call(extr + ' x ' + file + ' -oclient' + ' -y')
                self.signal.emit('Извлечение завершено\n')
        for file in files:
            if self.report:
                if 'report' in file:
                    self.signal.emit('Извлекаем {}...\n'.format(file))
                    sp.call(extr + ' x ' + file + ' -y')
                    self.signal.emit('Извлечение завершено\n')
        for file in files:
            if self.report:
                if 'apache' in file:
                    self.signal.emit('Извлекаем {}...\n'.format(file))
                    sp.call(extr + ' x ' + file + ' -y')
                    self.signal.emit('Извлечение завершено\n')
        for file in files:
            if self.report:
                if 'azk.war' in file:
                    tomcat = os.path.join(os.getcwd(), 'apache-tomcat-6.0.29_BFT-1.0\\webapps')
                    self.signal.emit('Переносим {0} в {1}...\n'.format(file, tomcat))
                    shutil.move(file, tomcat)

    def configurator(self):
        files = os.listdir('.')
        if 'Azk2Server.properties' in files:
            self.signal.emit('Настраиваем конфиг...\n')
            if self.shema is not None:
                self.signal.emit('Устанавливаем логин пароль {} в Azk2Server.properties...\n'.format(self.shema))
                replacer.replaceAzkConfig(self.shema)
            if self.port is not None:
                self.signal.emit('Устанавливаем порт {} в StartServer.bat...\n'.format(self.port))
                replacer.replaceServerPort(self.port)
                os.chdir('client')
                self.signal.emit('Устанавливаем порт {} в Azk2Clnt.ini...\n'.format(self.port))
                replacer.replaceClientPort(self.port)
            self.signal.emit('Настройка завершена...\n')


class DialogLog(QDialog, Ui_DialogLog):
    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        self.setupUi(self)
        self.textBrowser.setDisabled(True)
        self.pushButton.clicked.connect(self.closeWindow)

    def writeLog(self, text):
        self.textBrowser.insertPlainText(text)

    def buttonEnable(self, b):
        self.textBrowser.setDisabled(b)
        self.pushButton.setEnabled(True)

    def closeWindow(self):
        self.hide()

    def startLoadVersion(self, files, destination, extr, shema=None, password=None, port=None, report=False):
        self.thread = ThreadCopy(files, destination, extr, shema=shema, password=password, port=port, report=report)
        self.thread.signal.connect(self.writeLog)
        self.thread.buttonEnable.connect(self.buttonEnable)
        self.checkDir(destination)
        self.thread.start()

    def checkDir(self, destination):
        if not os.path.isdir(destination):
            self.writeLog('Создаем папку {}\n'.format(os.path.normpath(destination)))
            os.makedirs(destination)
        else:
            reply = QMessageBox.question(self, 'Внимание', "Папка уже создана. Удалить папку?",
                                         QMessageBox.Yes | QMessageBox.No,
                                         QMessageBox.Yes)
            if reply == QMessageBox.Yes:
                shutil.rmtree(destination)
                os.makedirs(destination)
            else:
                self.hide()
                return


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    ui = MainForm()
    sys.excepthook = ui.exception_hook
    ui.show()
    sys.exit(app.exec_())
