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
        
        consulta = 'INSERT OR IGNORE INTO cursoaluno (datavenc, fidaluno, fidcurso) VALUES (?, ?, ?)'       
        self.cursor.execute(consulta, (datavenc, fidaluno, fidcurso))
        self.conn.commit()
        
    
    def insert_coursedb(self, nomecurso, cargahr, qtdmes):

        consulta = 'INSERT OR IGNORE INTO curso (nomecurso, cargahr, qtdmes) VALUES (?, ?, ?)'
        self.cursor.execute(consulta, (nomecurso, cargahr, qtdmes))
        self.conn.commit()
    
    def list_coursedb(self):
        self.cursor.execute('SELECT * FROM curso')

        return self.cursor.fetchall()    