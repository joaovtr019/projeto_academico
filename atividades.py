from dados.dados_projeto import conectar_com_banco
conn, cursor = conectar_com_banco()

def cadastrar_atividade(numero_usuario):
    titulo = input("Título da atividade: ")
    descricao = input("Descrição: ")
    arquivo = input("Caminho do arquivo (opcional): ")
    cursor.execute(
        "INSERT INTO atividades (numero_usuario, titulo, descricao, arquivo) VALUES (?, ?, ?, ?)",
        (numero_usuario, titulo, descricao, arquivo)
    )
    conn.commit()
    print("\nAtividade cadastrada com sucesso!\n")

def consultar_atividades():
    cursor.execute("""
        SELECT u.user_aluno, a.titulo, a.descricao, a.arquivo
        FROM atividades a
        JOIN usuarios u ON a.numero_usuario = u.num
    """)
    atividades = cursor.fetchall()

    if atividades:
        print("Atividades Disponíveis")
        for atividade in atividades:
            print(f"Professor: {atividade[0]}")
            print(f"Título: {atividade[1]}")
            print(f"Descrição: {atividade[2]}")
            print(f"Arquivo: {atividade[3]}\n")
    else:
        print("\nNenhuma atividade cadastrada.")
