import sys
from design import *
from PyQt5.QtWidgets import QMainWindow, QApplication
from connection import rapsodiadb


class Novo(QMainWindow, Ui_MainWindow):
    def __init__(self, parent = None):
        super().__init__(parent)
        super().setupUi(self)
        self.conexao = rapsodiadb()
        self.actionCadastrar.triggered.connect(self.cadastrarWid)
        self.actionEmail.triggered.connect(lambda: self.stackedWidget.setCurrentWidget(self.update))
        self.actionRegistrar.triggered.connect(lambda: self.stackedWidget.setCurrentWidget(self.pay))
        self.actionPesquisar.triggered.connect(lambda: self.stackedWidget.setCurrentWidget(self.search))
        self.actionExcluir.triggered.connect(lambda: self.stackedWidget.setCurrentWidget(self.delete_2))
        self.actionCursos.triggered.connect(lambda: self.stackedWidget.setCurrentWidget(self.cursos))
        self.registerc.clicked.connect(self.insert_course)
        self.list_course.clicked.connect(self.list_coursei)
        self.pushButton.clicked.connect(self.register)
        self.comboBox_2.addItems(('id','Nome'))
        self.pushButton_4.clicked.connect(self.list_student)
        
        for tup in self.conexao.combo():
            tup = map(lambda a: str(a), tup)
            self.comboBox.addItem('-'.join(tup))   
            
    def cadastrarWid(self):
        self.stackedWidget.setCurrentWidget(self.register_2)
        self.comboBox.clear()
        for tup in self.conexao.combo():
            tup = map(lambda a: str(a), tup)
            self.comboBox.addItem('-'.join(tup))
            
    
    def insert_student(self):
        self.conexao.insert_coursedb(self.course_name.text(), self.workload.text(), self.mounths.text())
        self.course_name.setText(''), self.workload.setText(''), self.mounths.setText('')
        
    
    
    def insert_course(self):
        self.conexao.insert_coursedb(self.course_name.text(), self.workload.text(), self.mounths.text())
        self.course_name.setText(''), self.workload.setText(''), self.mounths.setText('')
        
    def register(self):
        course = str()
        for i in self.comboBox.currentText():
            if i == '-':
                break
            course +=i
            
        self.conexao.insert_studentdb(self.lineEdit.text(), self.lineEdit_3.text(), self.lineEdit_4.text())
        self.conexao.insert_student_coursedb(self.dateEdit.text(), int(course))
        self.lineEdit.setText(''), self.lineEdit_3.setText(''), self.lineEdit_4.setText('')
           
    
    def list_coursei(self):
        texto = str()
        form = {1:'Id: ', 2: 'Nome: ', 3:'Carga horária: ', 4:'Quantidade de meses: '}
        controle = 1
        for linha in self.conexao.list_coursedb():
            for dado in linha:
               if controle == 4:
                    texto += form[controle] +  str(dado)  + '<br>---------------------------<br><br>'  
               else:
                    texto += form[controle] +  str(dado) + '<br>'
               controle +=1
            controle = 1     

        self.textBrowser.setHtml("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
f"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\" bgcolor=\"#f0f0f0\">\n<FONT COLOR='#787878'>{texto}</FONT>"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>")
        
    def list_student(self):
        texto = str()
        form = {1:'Id: ', 2: 'Nome: ', 3:'Email: ', 4:'Telefone: ', 5:'Data de Vencimento: ', 6:'Parcelas Pagas: ', 7:'Curso Inscrito: '}
        controle = 1
        for linha in self.conexao.list_studentdb(self.comboBox_2.currentText(), self.lineEdit_7.text()):
            for dado in linha:
                if controle == 7:
                    texto += form[controle] +  str(dado)  + '<br>---------------------------<br><br>'  
                else:
                    texto += form[controle] +  str(dado) + '<br>'
                controle +=1
            controle = 1     

        self.textBrowser.setHtml("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
f"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\" bgcolor=\"#f0f0f0\">\n<FONT COLOR='#787878' size = 4>{texto}</FONT>"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>")   
    
        
                    
if __name__ == '__main__':
    qt = QApplication(sys.argv)
    novo = Novo()
    novo.show()
    qt.exec_()