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
            self.cursor.execute(consulta, (i, 0, fidaluno))
            self.conn.commit()    
        
    
    def insert_coursedb(self, nomecurso, cargahr, qtdmes):

        consulta = 'INSERT OR IGNORE INTO curso (nomecurso, cargahr, qtdmes) VALUES (?, ?, ?)'
        self.cursor.execute(consulta, (nomecurso, cargahr, qtdmes))
        self.conn.commit()
    
    def list_coursedb(self):
        self.cursor.execute('SELECT * FROM curso')

        return self.cursor.fetchall()
    
    def list_studentdb(self, param, value):
        
        if param == 'id':
            self.cursor.execute(f'SELECT idaluno, nome, email, telefone, datavenc, nomecurso FROM aluno JOIN cursoaluno ON aluno.idaluno = cursoaluno.fidaluno JOIN curso ON cursoaluno.fidcurso = curso.idcurso WHERE "idaluno" = {int(value)}')
            aluno =self.cursor.fetchall()
            aluno.append(self.cursor.execute(f'SELECT pagamento FROM aluno JOIN pagamentos ON aluno.idaluno = pagamentos.fidaluno WHERE "idaluno" = {int(value)}'))
            print(aluno)
            return aluno
        
        elif param == 'Nome': 
            self.cursor.execute(f'SELECT idaluno, nome, email, telefone, datavenc, pagamento, nomecurso FROM aluno JOIN cursoaluno ON aluno.idaluno = cursoaluno.fidaluno JOIN curso ON cursoaluno.fidcurso = curso.idcurso JOIN pagamentos ON aluno.idaluno = pagamentos.fidaluno WHERE "nome" like  "%{value}%"')

            return self.cursor.fetchall() 
    
   
               