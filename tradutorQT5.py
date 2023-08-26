#pip install PyQt5
#pip install PyQt5Designer
#pip install translate

#Para executar o Designer
#no terminal digite : designer.exe

#Para converter de arquivo ui para python , digite no terminal :
#pyuic5 -x arquivo.ui -o saida(nome_arquivo_python).py


from PyQt5 import QtCore, QtGui, QtWidgets
from translate import Translator


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.TextEditOrigem = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.TextEditOrigem.setGeometry(QtCore.QRect(50, 60, 231, 451))
        self.TextEditOrigem.setObjectName("TextEditOrigem")
        self.btnTradutor = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.tradutor())
        self.btnTradutor.setGeometry(QtCore.QRect(350, 240, 75, 41))
        self.btnTradutor.setObjectName("btnTradutor")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(160, 10, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(570, 10, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.TextEditPortuguese = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.TextEditPortuguese.setGeometry(QtCore.QRect(510, 60, 231, 451))
        self.TextEditPortuguese.setObjectName("TextEditPortuguese")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btnTradutor.setText(_translate("MainWindow", "Tradutor"))
        self.label.setText(_translate("MainWindow", "Ingles"))
        self.label_2.setText(_translate("MainWindow", "Portuguese"))


    def tradutor(self):
        texto = str(self.TextEditOrigem.toPlainText())
        obj = Translator(from_lang="english" , to_lang="portuguese")
        res = obj.translate(texto)
        self.TextEditPortuguese.setPlainText(res)
        
        
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
