alunos = {}

def adicionar_aluno(nome, nota):
    alunos[nome] = nota
    print(f"Aluno {nome} adicionado com nota {nota:.1f}.")


def media_turma():
    if not alunos:
        print("Nenhum aluno cadastrado.")
        return
    media = sum(alunos.values()) / len(alunos)
    print(f"\nA média da turma é: {media:.2f}")

def listar_alunos():
    if not alunos:
        print("Nenhum aluno cadastrado.")
        return
    print("\nAlunos cadastrados:")
    print("\n --- lista de alunos --- \n")
    for nome, nota in alunos.items():
        status = "Aprovado" if nota >= 6 else "Reprovado"
        print(f"{nome}: {nota:.1f} - {status}")

def menu():
    while True:
        print("\n--- Menu ---")
        print("1. Adicionar aluno")
        print("2. Listar alunos")
        print("3. Calcular média da turma")
        print("4. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Digite o nome do aluno: ")
            nota = float(input("nota (0-10): "))
            adicionar_aluno(nome, nota)
        elif opcao == "2":
            listar_alunos()
        elif opcao == "3":
            media_turma()
        elif opcao == "4":
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")

    menu()