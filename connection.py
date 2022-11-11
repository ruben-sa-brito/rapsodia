import sqlite3



class rapsodiadb:
    def __init__(self):
        self.conn = sqlite3.connect('db_graf.db')
        self.cursor = self.conn.cursor()

    def combo(self):
        self.cursor.execute('SELECT idcurso, nomecurso FROM curso')

        return self.cursor.fetchall()
    
    def insert_studentdb(self, nome, email, telefone):

        consulta = 'INSERT OR IGNORE INTO aluno (nome, email, telefone) VALUES (?, ?, ?)'
        self.cursor.execute(consulta, (nome, email, telefone))
        self.conn.commit()
        
    def insert_student_coursedb(self, datavenc, fidcurso): 
        fidaluno = str()
        for tup in self.cursor.execute('SELECT MAX(idaluno) FROM aluno').fetchall():
            for i in tup:
                fidaluno = i 
        
        consulta = 'INSERT OR IGNORE INTO cursoaluno (datavenc, fidaluno, fidcurso, parcpg) VALUES (?, ?, ?, ?)'       
        self.cursor.execute(consulta, (datavenc, fidaluno, fidcurso, 0))
        self.conn.commit()
    
    def payments(self, idcurso):
        fidaluno = str()
        for tup in self.cursor.execute('SELECT MAX(idaluno) FROM aluno').fetchall():
            for i in tup:
                fidaluno = i
        for tup in self.cursor.execute(f'SELECT qtdmes FROM curso WHERE idcurso = {idcurso}').fetchall():
            for i in tup:
                qtdmonths = i
                
                

        for i in range(qtdmonths):
            consulta = 'INSERT OR IGNORE INTO pagamentos (parcela, pagamento, fidaluno) VALUES (?, ?, ?)'
            self.cursor.execute(consulta, (i+1, 0, fidaluno))
            self.conn.commit()    
          
    def insert_coursedb(self, nomecurso, cargahr, qtdmes):

        consulta = 'INSERT OR IGNORE INTO curso (nomecurso, cargahr, qtdmes) VALUES (?, ?, ?)'
        self.cursor.execute(consulta, (nomecurso, cargahr, qtdmes))
        self.conn.commit()
    
    def list_coursedb(self):
        self.cursor.execute('SELECT * FROM curso')

        return self.cursor.fetchall()
    
    def list_studentdb(self, param, value):
        aluno = list()
        
        if param == 'id':
            self.cursor.execute(f'SELECT idaluno, nome, email, telefone, datavenc, nomecurso FROM aluno JOIN cursoaluno ON aluno.idaluno = cursoaluno.fidaluno JOIN curso ON cursoaluno.fidcurso = curso.idcurso WHERE "idaluno" = {int(value)}')
            for a in self.cursor.fetchall():
                aluno.append(a)
           
            aluno.append(self.cursor.execute(f'SELECT pagamento FROM aluno JOIN pagamentos ON aluno.idaluno = pagamentos.fidaluno WHERE "idaluno" = {int(value)}'))
            
            return aluno
        
        elif param == 'Nome':
            self.cursor.execute(f'SELECT idaluno FROM aluno WHERE "nome" like  "%{value}%"')
            ids = self.cursor.fetchall()
            
            for tup in ids:
                
                for i in tup: 
                    self.cursor.execute(f'SELECT idaluno, nome, email, telefone, datavenc, nomecurso FROM aluno JOIN cursoaluno ON aluno.idaluno = cursoaluno.fidaluno JOIN curso ON cursoaluno.fidcurso = curso.idcurso WHERE "idaluno" = {i}')
                    
                    for a in self.cursor.fetchall():
                        aluno.append(a)
                    
                    self.cursor.execute(f'SELECT pagamento FROM aluno JOIN pagamentos ON aluno.idaluno = pagamentos.fidaluno WHERE "idaluno" = {i}')
                    payments = list()
                    for a in self.cursor.fetchall():
                        payments.append(a)
                    
                    aluno.append(payments)
                    
                       
            
            return aluno 
    
    def register_paymentsdbtest(self, idaluno, parcela):
        try:
            consulta = self.cursor.execute(f'SELECT pagamento FROM pagamentos  WHERE fidaluno = {int(idaluno)} AND parcela = {int(parcela)} ')
            exist = None
            for a in consulta:
                for b in a:
                    exist = b
            if exist == 1:
                return 1
            elif exist == None:
                return 0
            else:
                return 2
        except:
            return
    
    def register_paymentsdb(self, idaluno, parcela):
        
        
            registro = f'UPDATE pagamentos SET pagamento = 1 WHERE fidaluno = {int(idaluno)} AND parcela = {int(parcela)} '
            self.cursor.execute(registro)
            self.conn.commit()           
    
    def update_studentdb(self, idaluno, values):
        
        att = f'UPDATE aluno SET {values} WHERE idaluno = {idaluno}'
        
        
        self.cursor.execute(att)
        self.conn.commit()
            
        
        
    def select_aluno(self, idaluno):
        consulta = self.cursor.execute(f'SELECT nome FROM aluno WHERE idaluno = {int(idaluno)}')
        for a in consulta:
            for b in a:
                return b
            
    def select_aluno_exists(self, idaluno):
        
            consulta =self.cursor.execute(f'SELECT nome FROM aluno WHERE idaluno = {int(idaluno)}')
            for a in consulta:
                for b in a:
                    if b == None:
                        return False
                    else:
                        return True        
        
                    
   
               