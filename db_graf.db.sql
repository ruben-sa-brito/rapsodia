BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "aluno" (
	"idaluno"	INTEGER NOT NULL UNIQUE,
	"nome"	TEXT NOT NULL COLLATE NOCASE,
	"email"	TEXT COLLATE NOCASE,
	"telefone"	TEXT COLLATE NOCASE,
	PRIMARY KEY("idaluno" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "cursoaluno" (
	"idcursoaluno"	INTEGER NOT NULL UNIQUE,
	"datavenc"	TEXT COLLATE NOCASE,
	"conc"	INTEGER COLLATE NOCASE,
	"valorparc"	INTEGER COLLATE NOCASE,
	"fidaluno"	INTEGER,
	"fidcurso"	INTEGER,
	PRIMARY KEY("idcursoaluno" AUTOINCREMENT),
	FOREIGN KEY("fidcurso") REFERENCES "curso"("idcurso"),
	FOREIGN KEY("fidaluno") REFERENCES "aluno"("idaluno")
);
CREATE TABLE IF NOT EXISTS "curso" (
	"idcurso"	INTEGER NOT NULL UNIQUE,
	"nomecurso"	TEXT NOT NULL COLLATE NOCASE,
	"cargahr"	REAL,
	"qtdmes"	INTEGER,
	"valorparc"	INTEGER,
	PRIMARY KEY("idcurso" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "pagamentos" (
	"id"	INTEGER NOT NULL UNIQUE,
	"parcela"	INTEGER,
	"pagamento"	INTEGER,
	"fidaluno"	INTEGER,
	"data"	TEXT,
	"valor"	REAL,
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("fidaluno") REFERENCES "aluno"("idaluno")
);
COMMIT;
