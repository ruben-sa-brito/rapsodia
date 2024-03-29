import sys
from design import *
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QApplication
from connection import rapsodiadb
import re 
from dialog import Dialog
from datetime import datetime, timedelta
from generate import generate
regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'


class Novo(QMainWindow, Ui_MainWindow):
    def __init__(self, parent = None):
        super().__init__(parent)
        super().setupUi(self)
        self.setWindowFlag(Qt.WindowMaximizeButtonHint, False)
        self.setFixedSize(531, 614)
        self.conexao = rapsodiadb()
        self.actionCadastrar.triggered.connect(self.cadastrarWid)
        self.actionEmail.triggered.connect(lambda: self.stackedWidget.setCurrentWidget(self.update))
        self.actionRegistrar.triggered.connect(lambda: self.stackedWidget.setCurrentWidget(self.pay))
        self.actionPesquisar.triggered.connect(lambda: self.stackedWidget.setCurrentWidget(self.search))
        self.actionExcluir.triggered.connect(lambda: self.stackedWidget.setCurrentWidget(self.delete_2))
        self.actionCursos.triggered.connect(lambda: self.stackedWidget.setCurrentWidget(self.cursos))
        self.actionGerar_carn_s.triggered.connect(lambda: self.stackedWidget.setCurrentWidget(self.generatePage))
        self.registerc.clicked.connect(self.insert_course)
        self.list_course.clicked.connect(self.list_coursei)
        self.pushButton.clicked.connect(self.register)
        self.pushButtonPay.clicked.connect(self.register_payments)
        self.comboBox_2.addItems(('id','Nome'))
        self.pushButton_4.clicked.connect(self.list_student)
        self.pushButton_2.clicked.connect(self.update_student)
        self.list_paym.clicked.connect(self.list_payments)
        self.list_late.clicked.connect(self.list_latef)
        self.delA.clicked.connect(self.del_student)
        self.updatec.clicked.connect(self.update_course)
        self.pushButton_3.clicked.connect(self.generate_pay)
        self.lineDiscount.setVisible(False)
        self.checkBox.clicked.connect(self.discountBox)
        self.lineDiscount.setPlaceholderText('Digite o novo valor')
        
        for tup in self.conexao.combo():
            tup = map(lambda a: str(a), tup)
            self.comboBox.addItem('-'.join(tup))   
            
    def cadastrarWid(self):
        
        self.stackedWidget.setCurrentWidget(self.register_2)
        self.comboBox.clear()
        for tup in self.conexao.combo():
            tup = map(lambda a: str(a), tup)
            self.comboBox.addItem('-'.join(tup))
    
    def insert_course(self): #insere registros de cursos no banco de dados
        if len(self.course_name.text().replace(' ','')) == 0:
            message.invalid_name()
        else:    
            try:
                int(self.mounths.text())
                int(self.workload.text())
                int(self.lineEdit_2.text())
            except:
                message.general_error()
            else:        
        
                self.conexao.insert_coursedb(self.course_name.text(), self.workload.text(), self.lineEdit_2.text() ,self.mounths.text())
                self.course_name.setText(''), self.workload.setText(''), self.mounths.setText(''), self.lineEdit_2.setText('')
                message.sucess_register()
   
    def update_course(self): #atualiza registros de cursos no banco de dados
        values = list()
        
        try:
            ida = int(self.lineEdit_9.text())
        except:
            message.general_error()
        else:         
            if self.conexao.select_course_exists(ida):
                if message.confirm_box_upd(self.conexao.select_course(ida)):
                    nome = self.course_name.text()
                    cargahoraria = self.workload.text()
                    valor = self.lineEdit_2.text()
                    meses = self.mounths.text()
                    if len(nome.replace(' ','')) != 0:
                        
                        values.append('nomecurso = '+"'"+nome+"'")
                    
                    try:
                        if len(cargahoraria.replace(' ','')) != 0:
                            float(cargahoraria)
                            values.append('cargahr = '+"'"+cargahoraria+"'")     
                    except:
                        message.general_error() 
                    
                    try:
                        if len(valor.replace(' ','')) != 0:
                            float(valor)
                            values.append('valorparc = '+"'"+valor+"'")     
                    except:
                        message.general_error()
                    
                    try:
                        if len(meses.replace(' ','')) != 0:
                            int(meses)
                            values.append('qtdmes = '+"'"+meses+"'")     
                    except:
                        message.general_error()        
                    
                    if len(values) == 0:
                        pass
                    else:
                        values = ', '.join(values)       
                        self.conexao.update_coursedb(ida, values)
                        self.course_name.setText(''), self.workload.setText(''), self.mounths.setText(''), self.lineEdit_2.setText('')
                        message.att_success()
            else:
                message.not_found()   
           
    def register(self): #insere registro de alunos no banco de dados
        
        
           
        if len(self.lineEdit.text().replace(' ','')) == 0:
            
            message.invalid_name()       
        
        elif int(self.dateEdit.text()[0:2]) >= 28:
            message.invalid_day()
                
        else:   
             
            if  len(self.lineEdit_3.text().replace(' ',''))>0:
                if not (re.search(regex, self.lineEdit_3.text())):
                    message.invalid_email()
                    return
                
            course = str()
            for i in self.comboBox.currentText():
                if i == '-':
                    break
                course +=i
               
            try:
                int(self.lineEdit_4.text())
            except:
                message.general_error()
            else:        
                if self.checkBox.isChecked():
                    if self.lineDiscount.text().replace(' ','') == 0:
                        message.general_error()
                    else:
                        try:
                            check = float(self.lineDiscount.text().replace(' ',''))    
                              
                            self.conexao.insert_studentdb(self.lineEdit.text(), self.lineEdit_3.text(), self.lineEdit_4.text())
                            self.conexao.insert_student_coursedb(self.dateEdit.text(), int(course), check)
                            self.conexao.payments(course)
                            self.lineEdit.setText(''), self.lineEdit_3.setText(''), self.lineEdit_4.setText(''), self.lineDiscount.setText('')
                            message.sucess_register()
                        except:
                            message.general_error()
                else:
                    check = False
                    self.conexao.insert_studentdb(self.lineEdit.text(), self.lineEdit_3.text(), self.lineEdit_4.text())
                    self.conexao.insert_student_coursedb(self.dateEdit.text(), int(course), check)
                    self.conexao.payments(course)
                    self.lineEdit.setText(''), self.lineEdit_3.setText(''), self.lineEdit_4.setText(''), self.lineDiscount.setText('')
                    message.sucess_register()               
                          
    def discountBox(self):
        if self.checkBox.isChecked():
            self.lineDiscount.setVisible(True)
        if not self.checkBox.isChecked():  
            self.lineDiscount.setVisible(False)  
    
    def list_coursei(self):
        texto = str()
        form = {1:'Id: ', 2: 'Nome: ', 3:'Carga horária: ', 4:'Quantidade de meses: ', 5: 'Valor da mensalidade: '}
        controle = 1
        for linha in self.conexao.list_coursedb():
            for dado in linha:
               if controle == 5:
                    texto += form[controle] +  str(dado)  + '<br>---------------------------<br><br>'  
               else:
                    texto += form[controle] +  str(dado) + '<br>'
               controle +=1
            controle = 1     

        self.textBrowser.setHtml(f"<body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\" bgcolor=\"#f0f0f0\">\n<FONT COLOR='#787878'>{texto}</FONT>")
        
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

            self.textBrowser.setHtml(f"<body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\" bgcolor=\"#f0f0f0\">\n<FONT COLOR='#787878' size = 4>{texto}</FONT>")   
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
    
    def update_student(self):
        values = list()
        
        try:
            ida = int(self.lineEdit_6.text())
        except:
            message.general_error()
        else:         
            if self.conexao.select_aluno_exists(ida):
                if message.confirm_box_upd(self.conexao.select_aluno(ida)): 
                    
                    nome =self.lineEdit.text()
                    email = self.lineEdit_3.text()
                    telefone = self.lineEdit_4.text()
                    
                            
                    if len(nome) != 0: 
                        values.append('nome = '+"'"+nome+"'")    
                        
                    if len(email) != 0:
                        if not (re.search(regex, email)):
                            
                            message.invalid_email_upd()
                        else:
                            values.append('email = '+"'"+email+"'")  
                    
                    if len(telefone) != 0:
                        values.append('telefone = '+"'"+telefone+"'")
                    if len(values) == 0:
                        pass
                    else:
                
                        values = ', '.join(values)
                        self.conexao.update_studentdb(ida, values)    
                        message.att_success()
                        self.lineEdit.setText(''), self.lineEdit_3.setText(''), self.lineEdit_4.setText('')
                        
            else:
                message.not_found()                
    
    def del_student(self):
        
        try:
            int(self.idadel.text())
        except:
            message.general_error()
        else:    
            if self.conexao.select_aluno_exists(self.idadel.text()):
                
                if message.confirm_box_del(self.conexao.select_aluno(self.idadel.text())):
                    self.conexao.del_studentdb(int(self.idadel.text()))
                    message.del_success()
                else:
                    pass
            else:
                message.general_error()
                            
    def list_latef(self):
        
        list_atrasados = list() 
         
        for tup in self.conexao.list_latedb():
            
            
            for tup2 in self.conexao.select_coursedb(tup[0]):
                pag = 0
                hoje = datetime.now()
                hoje = datetime(year = hoje.year, month = hoje.month, day = hoje.day )
                
                data_venc = datetime(year = int(tup2[1][6:10]), month = int(tup2[1][3:5]), day = int(tup2[1][0:2]))
                
                if data_venc >= hoje:
                    break
                else:
                    pag += 1
                data_c = data_venc
                if tup2[2] != 1:
                    
                    
                    while True:
                        data_c += timedelta(days=1)    
                        
                        if data_c.day == data_venc.day:
                            pag += 1
                            
                        if pag == tup2[0]:
                            break    
                        
                        if data_c == hoje:
                            break
                    if tup[2] < pag:
                        
                        list_atrasados.append([tup[0], tup[1], pag-tup[2]]) 
                    
                    pag = 0
        texto = str()
        form = {1: 'id: ', 2: 'Nome: ', 3:'Parcelas atrasadas: '}
        controle = 1
        for aluno in list_atrasados:
            for dado in aluno:
                if controle == 3:
                    texto += form[controle] +  str(dado)  + '<br>---------------------------<br><br>'  
                else:
                    texto += form[controle] +  str(dado) + '<br>'
                controle +=1
            controle = 1     

        self.textBrowser.setHtml(f"<body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\" bgcolor=\"#f0f0f0\">\n<FONT COLOR='#787878'>{texto}</FONT>")                   
    
    def list_payments(self):
        date = self.dateEdit_2.text()
        total_pay = 0
        total_value = 0
        
        for tup in self.conexao.select_paymentsdb():
            if tup[0] and tup[1] is not None:
                if tup[0][0:4] == date[3:8] and tup[0][5:7] == date[0:2]:
                    total_pay +=1
                     
                    total_value += tup[1]
        
        texto = f'Neste mês foram realizados {total_pay} pagamentos, com um valor total de {total_value}'        
        self.textBrowser.setHtml(f"<body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\" bgcolor=\"#f0f0f0\">\n<FONT COLOR='#787878' size = 4>{texto}</FONT>")                       
    
    def generate_pay(self):
        try:
            int(self.lineEditidAlGen.text())
        except:
            message.general_error() 
        else:
            if self.conexao.select_aluno_exists(self.lineEditidAlGen.text()):       
                if message.confirm_box_carnê(self.conexao.select_aluno(self.lineEditidAlGen.text())) == 0:
                        
                        
                        gen = list()
                        for tup in self.conexao.select_aluno_carnê(int(self.lineEditidAlGen.text())):
                            for i in tup:
                                gen.append(i) 
                        
                        carne = generate(gen[1]) 
                        carne.generate_parcs(gen[0], gen[1], gen[2], gen[3], gen[4])
                        message.general_message('Carnê gerado com sucesso \n Verifique a pasta pdfs no diretório do programa.')
            else:
                message.not_found()                   

        
                                         
                        
if __name__ == '__main__':
    qt = QApplication(sys.argv)
    novo = Novo()
    message = Dialog(novo)
    message.init_message()
    novo.show()
    qt.exec_()