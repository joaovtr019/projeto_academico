from dados.dados_projeto import conectar_com_banco
conn, cursor = conectar_com_banco()

def registrar_diario(numero_aula):
    cursor.execute("""
        SELECT a.num, a.nome 
        FROM alunos a
        JOIN aulas au ON a.numero_turma = au.numero_turma
        WHERE au.num = ?
    """, (numero_aula,))
    alunos = cursor.fetchall()

    for aluno in alunos:
        print(f"Aluno: {aluno[1]}")
        np1 = float(input("Digite a nota NP1: "))
        np2 = float(input("Digite a nota NP2: "))
        pim = float(input("Digite a nota do PIM: "))

        media = (np1 * 4 + np2 * 4 + pim * 2) / 10

        cursor.execute("""
            INSERT OR REPLACE INTO diario (numero_aula, numero_aluno, nota_np1, nota_np2, nota_pim, media_final, presente)
            VALUES (?, ?, ?, ?, ?, ?, 'Sim')
        """, (numero_aula, aluno[0], np1, np2, pim, media))
    conn.commit()
    print("Notas e médias registradas com sucesso!")

def consultar_notas_aluno(id_usuario):
    cursor.execute("""
        SELECT a.nome, d.nota_np1, d.nota_np2, d.nota_pim, d.media_final
        FROM diario d
        JOIN alunos a ON d.numero_aluno = a.num
        JOIN usuarios u ON a.nome = u.user_aluno
        WHERE u.num = ?
    """, (id_usuario,))
    notas = cursor.fetchall()

    if notas:
        print("Suas Notas:")
        for n in notas:
            print(f"Aluno: {n[0]}")
            print(f"NP1: {n[1]} | NP2: {n[2]} | PIM: {n[3]} | MÉDIA FINAL: {n[4]:.2f}")
            print("-")
    else:
        print("Nenhuma nota registrada para este aluno ainda.")

