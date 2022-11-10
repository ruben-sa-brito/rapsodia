import sys
from design import *
from PyQt5.QtWidgets import QMainWindow, QApplication
from connection import rapsodiadb
import re 
from dialog import Dialog
regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'


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
        self.pushButtonPay.clicked.connect(self.register_payments)
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
    
    def insert_course(self):
        try:
            int(self.mounths.text())
        except:
            message.invalid_mounth()
        else:        
       
            self.conexao.insert_coursedb(self.course_name.text(), self.workload.text(), self.mounths.text())
            self.course_name.setText(''), self.workload.setText(''), self.mounths.setText('')
            message.sucess_register()
           
    def register(self):
           
        if len(self.lineEdit.text().replace(' ','')) == 0:
            
            message.invalid_name()
            
        elif not (re.search(regex, self.lineEdit_3.text())):
            
            message.invalid_email()         
                
        else:    
            
            course = str()
            for i in self.comboBox.currentText():
                if i == '-':
                    break
                course +=i
                
            self.conexao.insert_studentdb(self.lineEdit.text(), self.lineEdit_3.text(), self.lineEdit_4.text())
            self.conexao.insert_student_coursedb(self.dateEdit.text(), int(course))
            self.conexao.payments(course)
            self.lineEdit.setText(''), self.lineEdit_3.setText(''), self.lineEdit_4.setText('')
            
            message.sucess_register()       
    
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
        
        try:
            texto = str()
            form = {1:'Id: ', 2: 'Nome: ', 3:'Email: ', 4:'Telefone: ', 5:'Data de vencimento: ', 6:'Curso Inscrito: ', 7:'Parcelas Pagas: '}
            controle = 1
            controle2  = 1
            pay = 0
            for linha in self.conexao.list_studentdb(self.comboBox_2.currentText(), self.lineEdit_7.text()):
                if controle2 % 2 !=0:
                    
                    for dado in linha:
                        texto += form[controle] +  str(dado) + '<br>'
                        controle +=1        
                else:
                    
                    for tup in linha:
                        for i in tup: 
                            
                            if i == 1:
                                pay +=1
                                
                    texto += form[7] +  str(pay) + '<br>---------------------------<br><br>' 
                    pay = 0
                    
                controle2 += 1            
                controle = 1     

            self.textBrowser.setHtml("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
    "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
    "p, li { white-space: pre-wrap; }\n"
    f"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\" bgcolor=\"#f0f0f0\">\n<FONT COLOR='#787878' size = 4>{texto}</FONT>"
    "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>")   
        except:
            pass
            
    def register_payments(self):
        
        consulta = self.conexao.register_paymentsdbtest(self.id_alunop.text(), self.parcela.text())
        
        if consulta == 1:
            message.payment_exists()
        elif consulta == 0:
            message.not_found()
        elif consulta == 2:
            if message.confirm_box(self.conexao.select_aluno(self.id_alunop.text())) == 0:
                self.conexao.register_paymentsdb(self.id_alunop.text(), self.parcela.text())  
                message.sucess_payment()
        elif consulta == 3:
            pass    
        else:
            message.general_error()        
            
        self.id_alunop.setText(''), self.parcela.setText('')
        
                        
if __name__ == '__main__':
    qt = QApplication(sys.argv)
    novo = Novo()
    novo.show()
    message = Dialog(novo)
    qt.exec_()