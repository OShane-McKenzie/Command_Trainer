from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
import json
from questions import *

class CustomPlainTextEdit(QtWidgets.QPlainTextEdit):
    returnPressed = QtCore.pyqtSignal()

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Return or event.key() == QtCore.Qt.Key_Enter:
            self.returnPressed.emit()
        else:
            super().keyPressEvent(event)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setFixedSize(800, 600)
        MainWindow.setAutoFillBackground(True)
        self.questionBank = Questions()
        self.thisQuestionIndex = 0
        self.question_list = self.questionBank.getQuestions("questions.json")
        self.text = self.question_list[self.thisQuestionIndex]["question"]
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.plainTextEdit = CustomPlainTextEdit(self.centralwidget)
        #self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(70, 300, 651, 111))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.plainTextEdit.setFont(font)
        self.plainTextEdit.setAutoFillBackground(False)
        self.plainTextEdit.setBackgroundVisible(False)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 90, 751, 181))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setAutoFillBackground(False)
        self.label.setText("")
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.label.setStyleSheet("background-color: white;")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(620, 420, 94, 40))
        self.pushButton.setObjectName("pushButton")
        self.pushButton2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton2.setGeometry(QtCore.QRect(70, 420, 94, 40))
        self.pushButton2.setObjectName("pushButton2")
        self.pushButton.clicked.connect(lambda: self.submit())
        self.pushButton2.clicked.connect(lambda: self.restart())
        self.plainTextEdit.returnPressed.connect(self.pushButton.click)
        
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 20, 281, 51))
        self.label_2.setAutoFillBackground(False)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(640, 20, 111, 61))
        self.label_3.setAutoFillBackground(False)
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 30))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menuFile.addSeparator()
        self.menuFile.addSeparator()
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.label.setText(self.text)
        self.label_2.setText(self.questionBank.progress)
    def submit(self):
        self.questionBank.check_commands(self.plainTextEdit.toPlainText(),self.thisQuestionIndex)
        if self.questionBank.isQuizEnd==False:
            self.thisQuestionIndex = self.thisQuestionIndex + 1
            text = self.question_list[self.thisQuestionIndex]["question"]
            self.label.setText(text)
            self.label_2.setText(self.questionBank.progress)
            
        else:
            self.label_2.setText(self.questionBank.progress)
            self.label_3.setText(self.questionBank.total)
        
        if self.questionBank.isCorrectAnswer == True:
            self.plainTextEdit.setPlainText("")
        else:
            self.plainTextEdit.setPlainText(self.questionBank.correction)

    def restart(self):
        self.questionBank.restart()
        self.thisQuestionIndex = 0
        self.question_list = self.questionBank.getQuestions("questions.json")
        self.text = self.question_list[self.thisQuestionIndex]["question"]
        self.plainTextEdit.setPlainText("")
        self.label.setText(self.text)
        self.label_2.setText(self.questionBank.progress)
        self.label_3.setText("")
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Command Trainer"))
        self.pushButton.setText(_translate("MainWindow", "Submit"))
        self.pushButton2.setText(_translate("MainWindow", "Restart"))
        self.label_2.setText(_translate("MainWindow", "Progress: "))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.menuAbout.setTitle(_translate("MainWindow", "About"))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(window)
    window.show()
    sys.exit(app.exec_())