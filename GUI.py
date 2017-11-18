import sys
import threading
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QWidget, QMessageBox
import os
import Backend


class Ui_Backup(QWidget):
    def setupUi(self, Backup):
        Backup.setObjectName("Backup")
        Backup.resize(580, 460)
        Backup.setMinimumSize(QtCore.QSize(580, 460))
        Backup.setMaximumSize(QtCore.QSize(580, 460))
        font = QtGui.QFont()
        font.setPointSize(14)
        Backup.setFont(font)
        self.centralwidget = QtWidgets.QWidget(Backup)
        self.centralwidget.setObjectName("centralwidget")
        self.Heading = QtWidgets.QLabel(self.centralwidget)
        self.Heading.setGeometry(QtCore.QRect(140, 20, 400, 60))
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setPointSize(36)
        self.Heading.setFont(font)
        self.Heading.setObjectName("Heading")
        self.Originallabel = QtWidgets.QLabel(self.centralwidget)
        self.Originallabel.setGeometry(QtCore.QRect(20, 100, 130, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Originallabel.setFont(font)
        self.Originallabel.setObjectName("Originallabel")
        self.Backuplabel = QtWidgets.QLabel(self.centralwidget)
        self.Backuplabel.setGeometry(QtCore.QRect(20, 150, 130, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Backuplabel.setFont(font)
        self.Backuplabel.setObjectName("Backuplabel")
        self.originaldir = QtWidgets.QTextEdit(self.centralwidget)
        self.originaldir.setGeometry(QtCore.QRect(160, 90, 400, 40))
        self.originaldir.setObjectName("originaldir")
        self.backupdir = QtWidgets.QTextEdit(self.centralwidget)
        self.backupdir.setGeometry(QtCore.QRect(160, 140, 400, 40))
        self.backupdir.setObjectName("backupdir")
        self.logbox = QtWidgets.QTextEdit(self.centralwidget)
        self.logbox.setGeometry(QtCore.QRect(20, 200, 540, 190))
        self.logbox.setObjectName("logbox")
        self.Startservice = QtWidgets.QPushButton(self.centralwidget)
        self.Startservice.setGeometry(QtCore.QRect(20, 400, 200, 40))
        self.Startservice.clicked.connect(self.onStart)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.Startservice.setFont(font)
        self.Startservice.setAutoDefault(False)
        self.Startservice.setDefault(False)
        self.Startservice.setFlat(False)
        self.Startservice.setObjectName("Startservice")
        self.Stopservice = QtWidgets.QPushButton(self.centralwidget)
        self.Stopservice.setGeometry(QtCore.QRect(360, 400, 200, 40))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.Stopservice.setFont(font)
        self.Stopservice.setObjectName("Stopservice")
        self.Stopservice.clicked.connect(self.onStop)
        self.Originalbrowse = QtWidgets.QToolButton(self.centralwidget)
        self.Originalbrowse.setGeometry(QtCore.QRect(540, 90, 20, 40))
        self.Originalbrowse.setObjectName("Originalbrowse")
        self.Originalbrowse.clicked.connect(self.OriginalFolderSelector)
        self.Backupbrowse = QtWidgets.QToolButton(self.centralwidget)
        self.Backupbrowse.setGeometry(QtCore.QRect(540, 140, 20, 40))
        self.Backupbrowse.setObjectName("Backupbrowse")
        self.Backupbrowse.clicked.connect(self.BackupFolderSelector)
        Backup.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Backup)
        self.statusbar.setObjectName("statusbar")
        Backup.setStatusBar(self.statusbar)
        self.retranslateUi(Backup)
        QtCore.QMetaObject.connectSlotsByName(Backup)

    def errordir(self):
        QMessageBox.about(self, "Directory Error", "Please Select A Valid Folder For Backup Files And Original files")

    def retranslateUi(self, Backup):
        _translate = QtCore.QCoreApplication.translate
        Backup.setWindowTitle(_translate("Backup", "Backup"))
        self.Heading.setText(_translate("Backup", "Backup Software"))
        self.Originallabel.setText(_translate("Backup", "Original Directory:"))
        self.Backuplabel.setText(_translate("Backup", "Backup Directory:"))
        self.Startservice.setText(_translate("Backup", "Start"))
        self.Stopservice.setText(_translate("Backup", "Stop"))
        self.Originalbrowse.setText(_translate("Backup", "..."))
        self.Backupbrowse.setText(_translate("Backup", "..."))


    def onStart(self):
        try:
            testfile = os.path.join(Backup_Directory, 'Backupfolder.txt')
            Backend.loop = True
            f = open(testfile,"w")
            self.threadme()
        except:
            self.errordir()

    def onStop(self):
        Backend.loop = False

    def threadme(self):

        b = threading.Thread(name='backupProcess', target=Backend.backupProcess,args=(Original_Directory, Backup_Directory))
        b.start()

    def OriginalFolderSelector(self):
        global Original_Directory
        Original_Directory = str(QFileDialog.getExistingDirectory(self, 'Select Original Directory'))+'/'
        print(Original_Directory)
        self.originaldir.setText(Original_Directory)
        global log
        log = "Original Folder Selected : "+Original_Directory+"\n"
        self.logbox.setText(log)


    def BackupFolderSelector(self):
        global Backup_Directory
        Backup_Directory = str(QFileDialog.getExistingDirectory(self, 'Select Backup Directory'))+'/'
        print(Backup_Directory)
        self.backupdir.setText(Backup_Directory)
        global log
        log+="Backup Folder Selected : " + Backup_Directory + "\n"
        self.logbox.setText(log)




if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Backup = QtWidgets.QMainWindow()
    ui = Ui_Backup()
    ui.setupUi(Backup)
    Backup.show()
    sys.exit(app.exec_())
