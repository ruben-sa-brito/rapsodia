import sqlite3
from datetime import datetime



class rapsodiadb:
    def __init__(self):
        
        with open('dir_db.txt', 'r' ) as arquivo:
            local = arquivo.read()
            
        
            
        self.conn = sqlite3.connect(local[7:])
        self.cursor = self.conn.cursor()

    def combo(self):
        self.cursor.execute('SELECT idcurso, nomecurso FROM curso')

        return self.cursor.fetchall()
    
    def insert_studentdb(self, nome, email, telefone):

        consulta = 'INSERT OR IGNORE INTO aluno (nome, email, telefone) VALUES (?, ?, ?)'
        self.cursor.execute(consulta, (nome, email, telefone))
        self.conn.commit()
        
    def insert_student_coursedb(self, datavenc, fidcurso, check): 
        fidaluno = str()
        valorparc = str()
        for tup in self.cursor.execute('SELECT MAX(idaluno) FROM aluno').fetchall():
            for i in tup:
                fidaluno = i 
        if not check:        
            for tup in self.cursor.execute(f'SELECT valorparc FROM curso WHERE idcurso = {fidcurso}'):
                for i in tup:
                    valorparc = i
        else:
            valorparc = check            
                
        consulta = 'INSERT OR IGNORE INTO cursoaluno (datavenc, fidaluno, fidcurso, valorparc) VALUES (?, ?, ?, ?)'       
        self.cursor.execute(consulta, (datavenc, fidaluno, fidcurso, float(valorparc)))
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
          
    def insert_coursedb(self, nomecurso, cargahr, valorparc, qtdmes):

        consulta = 'INSERT OR IGNORE INTO curso (nomecurso, cargahr, valorparc, qtdmes) VALUES (?, ?, ?, ?)'
        self.cursor.execute(consulta, (nomecurso, cargahr, valorparc, qtdmes))
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
    
    def list_latedb(self):
        alunopay = list()
        mesespagos = 0
        alunos = list()
        for aluno in self.cursor.execute(f'SELECT idaluno, nome FROM aluno '):
            alunos.append(aluno)
        
        for aluno in alunos:
            aluno2 = list(aluno)
            
            for tup in self.cursor.execute(f'SELECT pagamento FROM pagamentos WHERE pagamentos.fidaluno = {aluno[0]}').fetchall():  
                if tup == (1,):
                    mesespagos +=1
            aluno2.append(mesespagos)
            alunopay.append(aluno2)
            mesespagos = 0 
            
        return alunopay
        
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
            
            valor = str()
            
            
            for tup in self.cursor.execute(f'SELECT valorparc FROM cursoaluno WHERE fidaluno = {idaluno} LIMIT 1'):
                for parc in tup:
                    valor = parc        
            
            
                    
            today = str(datetime.now())
            idcur = int()
            qtdmes = int()
            pagamentos = list()
            registro = f"UPDATE pagamentos SET pagamento = 1, data = '{today}', valor = {valor} WHERE fidaluno = {int(idaluno)} AND parcela = {int(parcela)}"
            self.cursor.execute(registro)
            self.conn.commit()
            
            for tup in self.cursor.execute(f'SELECT fidcurso FROM cursoaluno WHERE fidaluno = {int(idaluno)}'):
                for ide in tup:
                    idcur = int(ide)
                    break
            for tup in self.cursor.execute(f'SELECT qtdmes FROM curso WHERE idcurso = {idcur} '):
                for qtd in tup:
                    qtdmes = int(qtd)
                    break 
            
            for tup in self.cursor.execute(f'SELECT pagamento FROM pagamentos WHERE fidaluno = {int(idaluno)}'):
                pagamentos.append(tup[0]) 
            
            if sum(pagamentos) == qtdmes:
                self.cursor.execute(f'UPDATE cursoaluno SET conc = 1 WHERE fidaluno = {idaluno}')
                self.conn.commit()                        
    
    def update_studentdb(self, idaluno, values): #atualiza registros de estudantes no banco de dados
        
        att = f'UPDATE aluno SET {values} WHERE idaluno = {idaluno}'
        
        
        self.cursor.execute(att)
        self.conn.commit()
    
    def update_coursedb(self, idcurso, values): #atualiza registros de cursos no banco de dados
        
        att = f'UPDATE curso SET {values} WHERE idcurso = {idcurso}'
        
        
        self.cursor.execute(att)
        self.conn.commit()    
            
    def del_coursedb(self, idcurso):
        try:
            self.cursor.execute(f'DELETE FROM curso WHERE idcurso = {idcurso}')
            self.conn.commit()
        except:
            return 0 
    
    def del_studentdb(self, idaluno):
        try:
            self.cursor.execute(f'DELETE FROM pagamentos WHERE fidaluno = {idaluno}')
            self.conn.commit()
            self.cursor.execute(f'DELETE FROM cursoaluno WHERE fidaluno = {idaluno}')
            self.conn.commit()
            self.cursor.execute(f'DELETE FROM aluno WHERE idaluno = {idaluno}')
            self.conn.commit()
        except:
            return 0    
                              
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

    def select_course(self, idcurso):
        consulta = self.cursor.execute(f'SELECT nomecurso FROM curso WHERE idcurso = {int(idcurso)}')
        for a in consulta:
            for b in a:
                return b

    def select_course_exists(self, idcurso):
        consulta =self.cursor.execute(f'SELECT nomecurso FROM curso WHERE idcurso = {int(idcurso)}')
        for a in consulta:
            for b in a:
                if b == None:
                    
                    return False
                else:
                    
                    return True 

    def select_coursedb(self, idaluno):
        return self.cursor.execute(f'SELECT qtdmes, datavenc, conc FROM cursoaluno JOIN curso ON cursoaluno.fidcurso = curso.idcurso WHERE fidaluno = {idaluno}')
    
    def select_paymentsdb(self):
        return self.cursor.execute('SELECT substr(data, 0, 8), valor FROM pagamentos')                
                    
    def select_aluno_carnê(self, idaluno):
        return self.cursor.execute(f'SELECT idaluno, nome, datavenc, qtdmes, cursoaluno.valorparc FROM aluno JOIN cursoaluno ON idaluno = fidaluno JOIN curso  ON fidcurso = idcurso WHERE idaluno = {idaluno}')
               