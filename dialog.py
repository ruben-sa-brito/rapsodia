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
    
    def invalid_name(self):
        self.message.setText('Campo nome nao pode ficar vazio')
        self.message.setWindowTitle('Aviso')
        self.message.setIcon(QMessageBox.Warning)
        self.message.exec_()
    
    def general_error(self):
        self.message.setText('ERROR')
        self.message.setWindowTitle('Warning')
        self.message.setIcon(QMessageBox.Warning)
        self.message.exec_()         