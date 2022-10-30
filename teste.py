import sys
from design import *
from PyQt5.QtWidgets import QMainWindow, QApplication

class Novo(QMainWindow, Ui_MainWindow):
    def __init__(self, parent = None):
        super().__init__(parent)
        super().setupUi(self)
        self.textEdit.setDisabled(True)
        self.actionCadastrar.triggered.connect(lambda: self.stackedWidget.setCurrentWidget(self.register_2))
        self.actionEmail.triggered.connect(lambda: self.stackedWidget.setCurrentWidget(self.update))
        self.actionRegistrar.triggered.connect(lambda: self.stackedWidget.setCurrentWidget(self.pay))
        self.actionPesquisar.triggered.connect(lambda: self.stackedWidget.setCurrentWidget(self.search))
        self.actionExcluir.triggered.connect(lambda: self.stackedWidget.setCurrentWidget(self.delete_2))
        self.actionCursos.triggered.connect(lambda: self.stackedWidget.setCurrentWidget(self.cursos))
        
if __name__ == '__main__':
    qt = QApplication(sys.argv)
    novo = Novo()
    novo.show()
    qt.exec_()