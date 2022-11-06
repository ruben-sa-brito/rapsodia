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