from dados.dados_projeto import conectar_com_banco
conn, cursor = conectar_com_banco()

def cadastrar_turma():
    nome = input("Qual o nome da turma: ")
    try:
        cursor.execute("INSERT INTO turmas (nome) VALUES (?)", (nome,))
        conn.commit()
        print("Turma cadastrada.")
    except:
        print("Essa turma já existe. Tente novamente.")
