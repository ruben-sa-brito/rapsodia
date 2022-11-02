import sys
from design import *
from PyQt5.QtWidgets import QMainWindow, QApplication
from connection import rapsodiadb


class Novo(QMainWindow, Ui_MainWindow):
    def __init__(self, parent = None):
        super().__init__(parent)
        super().setupUi(self)
        self.conexao = rapsodiadb()
        self.textEdit.setDisabled(True)
        self.actionCadastrar.triggered.connect(lambda: self.stackedWidget.setCurrentWidget(self.register_2))
        self.actionEmail.triggered.connect(lambda: self.stackedWidget.setCurrentWidget(self.update))
        self.actionRegistrar.triggered.connect(lambda: self.stackedWidget.setCurrentWidget(self.pay))
        self.actionPesquisar.triggered.connect(lambda: self.stackedWidget.setCurrentWidget(self.search))
        self.actionExcluir.triggered.connect(lambda: self.stackedWidget.setCurrentWidget(self.delete_2))
        self.actionCursos.triggered.connect(lambda: self.stackedWidget.setCurrentWidget(self.cursos))
        self.registerc.clicked.connect(self.insert_course)
        self.list_course.clicked.connect(self.list_coursei)
        self.pushButton.clicked.connect(self.register)
        for tup in self.conexao.combo():
            for n in tup:
                self.comboBox.addItem(n)
            
        
        
            
        
    
    def insert_course(self):
        self.conexao.insert_coursedb(self.course_name.text(), self.workload.text(), self.mounths.text())
        self.course_name.setText(''), self.workload.setText(''), self.mounths.setText('')
        
    def register(self):
        print(type(self.dateEdit.text()))
           
    
    def list_coursei(self):
        texto = str()
        form = {1:'Id: ', 2: 'Nome: ', 3:'Carga horária: ', 4:'Quantidade de meses: '}
        controle = 1
        for linha in self.conexao.list_coursedb():
            for dado in linha:
               if controle == 4:
                    texto += form[controle] +  str(dado)  + '\n---------------------------\n\n'  
               else:
                    texto += form[controle] +  str(dado) + '\n'
               controle +=1
            controle = 1     

        self.textEdit.setText(texto)     
        
        
                    
if __name__ == '__main__':
    qt = QApplication(sys.argv)
    novo = Novo()
    novo.show()
    qt.exec_()