alunos = []

def menu():
  print("===== Sistema de Cadastro =====")
  print("\n1 - Adicionar aluno")
  print("2 - Listar alunos")
  print("3 - Buscar alunos")
  print("4 - Remover aluno")
  print("5 - Sair")

def adicionar():
  while True:
    aluno = input("Nome do aluno: ")
    nome_sem_espaco = aluno.replace(" ", "")
    if nome_sem_espaco.isalpha():
      alunos.append(aluno)
      print("\nAluno adicionado.\n")
      break
    else:
      print("\nNome inválido.\n")
      continue
  print(f"{alunos}\n")

def listar():
  if len(alunos) > 0:
    print("\nAlunos Cadastrados:")
    for aluno in alunos:
      print(aluno)
  else:
    print("\nVocê deve ter pelo menos 1 aluno cadastrado.\n")

def buscar():
  if len(alunos) <= 0:
    print("\nNão há nenhum aluno cadastrado.\n")
  else:
    nome = input("Nome do aluno: ")
    if nome in alunos:
      print(f"{nome} é um aluno.")
      print(f"{alunos}\n")
    else:
      print(f"{nome} não é um aluno")

def remover():
  if len(alunos) <= 0:
    print("\nNão há nenhum aluno para remover.\n")
  else:
    nome = input("Nome do aluno: ")
    if nome in alunos:
      alunos.remove(nome)
    else:
      print("Aluno não encontrado no sistema.")

while True:
  menu()
  opcao = input("\nDigite uma das opções acima: ")
  if opcao == '1':
    adicionar()
  elif opcao == '2':
    listar()
  elif opcao == '3':
    buscar()
  elif opcao == '4':
    remover()
  elif opcao == '5':
    break
  else:
    print("\nOpção Inválida.\n")
    continue