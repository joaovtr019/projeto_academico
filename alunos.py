from dados.dados_projeto import conectar_com_banco
conn, cursor = conectar_com_banco()

def cadastrar_aluno_na_turma():
    nome = input("Nome do aluno: ")
    matricula = input("Digite o R.A: ")
    cursor.execute("SELECT num, nome FROM turmas")
    turmas = cursor.fetchall()
    for turmas in turmas:
        print(f"{turmas[0]} - {turmas[1]}")
    numero_turma = int(input("Digte o numero da turma: "))
    try:
        cursor.execute(
            "INSERT INTO alunos (nome, matricula, numero_turma) VALUES (?, ?, ?)",
            (nome, matricula, numero_turma)
        )
        conn.commit()
        print("Aluno cadastrado.")
    except:
        print("Erro. matrícula já existe ou o valor é inválido.")
