import sqlite3


class rapsodiadb:
    def __init__(self):
        self.conn = sqlite3.connect('db_graf.db')
        self.cursor = self.conn.cursor()

    def combo(self):
        self.cursor.execute('SELECT nomecurso FROM curso')

        return self.cursor.fetchall()
        
    
    def insert_coursedb(self, nomecurso, cargahr, qtdmes):

        consulta = 'INSERT OR IGNORE INTO curso (nomecurso, cargahr, qtdmes) VALUES (?, ?, ?)'
        self.cursor.execute(consulta, (nomecurso, cargahr, qtdmes))
        self.conn.commit()
    
    def list_coursedb(self):
        self.cursor.execute('SELECT * FROM curso')

        return self.cursor.fetchall()    