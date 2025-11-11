import getpass
from dados.dados_projeto import conectar_com_banco

conn, cursor = conectar_com_banco()

def cadastrar_usuario():
    user_aluno = input("Digite o seu nome de usuário: ")
    senha = getpass.getpass("Digite a sua senha: ")
    matricula = input("Digite o seu número de matrícula(R.A): ")
    tipo = input("Você é professor ou aluno?: ").lower()
    try:
        cursor.execute(
            "INSERT INTO usuarios (user_aluno, senha, matricula, tipo) VALUES (?, ?, ?, ?)",
            (user_aluno, senha, matricula, tipo)
        )
        conn.commit()
        print("Usuário cadastrado.")
    except:
        print("Usuário ou matrícula já existem.")

def login_usuario():
    user_aluno = input("Nome de usuário: ")
    senha = getpass.getpass("Senha: ")
    cursor.execute("SELECT * FROM usuarios WHERE user_aluno=? AND senha=?", (user_aluno, senha))
    usuario = cursor.fetchone()
    if usuario:
        print(f"Bem-vindo, {user_aluno}!")
        return usuario 
    else:
        print("Usuário ou senha incorretos!")
        return None
