from PyQt5.QtWidgets import  QMessageBox

class Dialog:
    def __init__(self, novo):
        self.message = QMessageBox(novo)
        
    def invalid_mounth(self):
        self.message.setText('Quantidade de meses precisa ser um numero')
        self.message.setWindowTitle('Mensagem')
        self.message.setIcon(QMessageBox.Information)
        self.message.exec_()    
        
    def sucess_register(self):
        self.message.setText('Cadastrado com sucesso')
        self.message.setWindowTitle('Mensagem')
        self.message.setIcon(QMessageBox.Information)
        self.message.exec_()
        
    def sucess_payment(self):
        self.message.setText('Pagamento registrado com sucesso')
        self.message.setWindowTitle('Mensagem')
        self.message.setIcon(QMessageBox.Information)
        self.message.exec_()
    
    def not_found(self):
        self.message.setText('Registro não encontrado')
        self.message.setWindowTitle('Aviso')
        self.message.setIcon(QMessageBox.Warning)
        self.message.exec_()
    
    def confirm_box(self, text):
       
        n = self.message.question(self.message, 'Aviso','Deseja registrar o pagamento do(a) aluno(a):\n ' +text, QMessageBox.Yes | QMessageBox.No)
        self.message.question
           
        if n == self.message.Yes:
            return 0
        else:
            return 1
    
    def confirm_box_upd(self, text):
       
        n = self.message.question(self.message, 'Aviso','Deseja atualizar o registro do(a) aluno(a):\n ' +text, QMessageBox.Yes | QMessageBox.No)
        self.message.question
           
        if n == self.message.Yes:
            return True
        else:
            return False
    
    def confirm_box_del(self, text):
       
        n = self.message.question(self.message, 'Aviso','Deseja excluir o registro do(a) aluno(a):\n ' +text, QMessageBox.Yes | QMessageBox.No)
        self.message.question
           
        if n == self.message.Yes:
            return True
        else:
            return False              
        
    def payment_exists(self):
        self.message.setText('Pagamento já registrado')
        self.message.setWindowTitle('Aviso')
        self.message.setIcon(QMessageBox.Warning)
        self.message.exec_()  
        
    def invalid_email(self):
        self.message.setText('Digite um email válido')
        self.message.setWindowTitle('Aviso')
        self.message.setIcon(QMessageBox.Warning)
        self.message.exec_()
    
    def invalid_email_upd(self):
        self.message.setText('Digite um email válido, seu email nao foi alterado')
        self.message.setWindowTitle('Aviso')
        self.message.setIcon(QMessageBox.Warning)
        self.message.exec_()
    
    def invalid_name(self):
        self.message.setText('Campo nome nao pode ficar vazio')
        self.message.setWindowTitle('Aviso')
        self.message.setIcon(QMessageBox.Warning)
        self.message.exec_()
    
    def general_error(self):
        self.message.setText('Ops algo deu errado :(')
        self.message.setWindowTitle('Warning')
        self.message.setIcon(QMessageBox.Warning)
        self.message.exec_()
    
    def del_success(self):
        self.message.setText('Registro excluído')
        self.message.setWindowTitle('Mensagem')
        self.message.setIcon(QMessageBox.Information)
        self.message.exec_()
        
    def att_success(self):
        self.message.setText('Cadastro atualizado')
        self.message.setWindowTitle('Mensagem')
        self.message.setIcon(QMessageBox.Information)
        self.message.exec_() 
    
    def invalid_day(self):
        self.message.setText('Dia de vencimento inválido, escolha um valor menor que 28.')
        self.message.setWindowTitle('Erro')
        self.message.setIcon(QMessageBox.Warning)
        self.message.exec_()   
    
    def init_message(self):
        self.message.setText('Antes de usar o sistema verifique se a data do computador está correta.')
        self.message.setWindowTitle('ATENÇÃO!')
        self.message.setIcon(QMessageBox.Information)
        self.message.exec_()
    
    def confirm_box_carnê(self, text):
       
        n = self.message.question(self.message, 'Aviso','Deseja gerar o carnê do(a) aluno(a):\n ' +text, QMessageBox.Yes | QMessageBox.No)
        self.message.question
           
        if n == self.message.Yes:
            return 0
        else:
            return 1 
    
    def general_message(self, text):
        self.message.setText(text)
        self.message.setWindowTitle('Mensagem')
        self.message.setIcon(QMessageBox.Information)
        self.message.exec_()                        