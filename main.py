import getpass
from usuarios.usuarios import cadastrar_usuario, login_usuario
from turmas.turmas import cadastrar_turma
from turmas.alunos import cadastrar_aluno_na_turma
from aulas.aulas import registrar_aula
from aulas.diario import registrar_diario
from aulas.diario import consultar_notas_aluno
from atividades.atividades import cadastrar_atividade, consultar_atividades
from dados.dados_projeto import conectar_com_banco

conn, cursor = conectar_com_banco()

def menu_professor(usuario):
    while True:
        print(f"Menu do Professor ({usuario[1]})")
        print("1. Cadastrar turma")
        print("2. Cadastrar aluno na Turma")
        print("3. Registrar aula")
        print("4. Diário (notas e presenças)")
        print("5. Cadastrar atividade")
        print("6. Consultar atividades")
        print("7. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_turma()
        elif opcao == "2":
            cadastrar_aluno_na_turma()
        elif opcao == "3":
            registrar_aula(usuario[0])
        elif opcao == "4":
            numero_aula = int(input("Digite o número da aula: "))
            registrar_diario(numero_aula)
        elif opcao == "5":
            cadastrar_atividade(usuario[0])
        elif opcao == "6":
            consultar_atividades()
        elif opcao == "7":
            print("Saindo do menu do professor...")
            break
        else:
            print("Opção inválida.")


def menu_aluno(usuario):
    while True:
        print(f"Menu do Aluno ({usuario[1]})")
        print("1. Ver perfil")
        print("2. Consultar atividades")
        print("3. Consultar notas")
        print("4. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            print(f"Usuário: {usuario[1]}")
            print(f"Matrícula (R.A): {usuario[3]}")
        elif opcao == "2":
            consultar_atividades()
        elif opcao == "3":
            consultar_notas_aluno(usuario[0])
        elif opcao == "4":
            print("Você saiu do menu do aluno.")
            break
        else:
            print("Opção inválida.")


def menu_principal():
    while True:
        print("Sistema UNIP")
        print("1. Cadastrar usuário")
        print("2. Login")
        print("3. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_usuario()
        elif opcao == "2":
            usuario = login_usuario()
            if usuario:
                tipo = usuario[4].lower()
                if tipo == "professor":
                    menu_professor(usuario)
                elif tipo == "aluno":
                    menu_aluno(usuario)
                else:
                    print("Tipo de usuário inválido.")
        elif opcao == "3":
            print("Saindo do sistema.")
            break
        else:
            print("Opção inválida.")


if __name__ == "__main__":
    menu_principal()
