import sqlite3

def conectar_com_banco():
    conn = sqlite3.connect('usuarios.db')
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS usuarios (
        num INTEGER PRIMARY KEY AUTOINCREMENT,
        user_aluno TEXT UNIQUE NOT NULL,
        senha TEXT NOT NULL,
        matricula TEXT UNIQUE NOT NULL,
        tipo TEXT NOT NULL
    )""")

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS turmas (
        num INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT UNIQUE NOT NULL
    )""")

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS alunos (
        num INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        matricula TEXT UNIQUE NOT NULL,
        numero_turma INTEGER,
        numero_usuario INTEGER,
        FOREIGN KEY(numero_turma) REFERENCES turmas(num)
    )""")

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS aulas (
        num INTEGER PRIMARY KEY AUTOINCREMENT,
        numero_turma INTEGER,
        numero_professor INTEGER,
        data TEXT,
        FOREIGN KEY(numero_turma) REFERENCES turmas(num),
        FOREIGN KEY(numero_professor) REFERENCES usuarios(num)
    )""")

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS diario (
        num INTEGER PRIMARY KEY AUTOINCREMENT,
        numero_aula INTEGER,
        numero_aluno INTEGER,
        nota_np1 REAL,
        nota_np2 REAL,
        nota_pim REAL,
        media_final REAL,
        presente TEXT,
        FOREIGN KEY(numero_aula) REFERENCES aulas(num),
        FOREIGN KEY(numero_aluno) REFERENCES alunos(num)
    )""")

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS atividades (
        num INTEGER PRIMARY KEY AUTOINCREMENT,
        numero_usuario INTEGER,
        titulo TEXT NOT NULL,
        descricao TEXT,
        arquivo TEXT,
        FOREIGN KEY(numero_usuario) REFERENCES usuarios(num)
    )""")

    conn.commit()
    return conn, cursor
