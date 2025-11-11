from dados.dados_projeto import conectar_com_banco
conn, cursor = conectar_com_banco()

def registrar_aula(numero_professor):
    cursor.execute("SELECT num, nome FROM turmas")
    turmas = cursor.fetchall()
    for turma in turmas:
        print(f"{turma[0]} - {turma[1]}")
    numero_turma = int(input("Digite o número da turma: "))
    data = input("Data da aula (DD/MM/AAAA): ")
    cursor.execute(
        "INSERT INTO aulas (numero_turma, numero_professor, data) VALUES (?, ?, ?)",
        (numero_turma, numero_professor, data)
    )
    conn.commit()
    print("Aula registrada.")
