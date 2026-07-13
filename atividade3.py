lista_de_pessoas = []
c = 0

while True:
  nome = input("Nome: ")
  nome_sem_espaco = nome.replace(' ', '')
  if nome_sem_espaco != '' and nome_sem_espaco.isalpha():
      while True:
          confirmacao = input("Você deseja participar da seleção de estágio? (S/N)\n")
          if confirmacao == 's' or confirmacao == 'S':
              lista_de_pessoas.append(nome)
              c += 1
              break
          elif confirmacao == 'n' or confirmacao == 'N':
              break
          else:
              print("Digite apenas S ou N para confirmar.")
          break
  else:
      print("Nome inválido. Tente novamente")
  if c == 3:
    print(f"Pessoas na lista: {c}")
    print(f"Lista de pessoas: {lista_de_pessoas}")
    break
