lista_de_pessoas = []
c = 0

while c < 3:
    nome_valido = False
    while nome_valido == False:
        nome = input("Nome: ")
        nome_sem_espaco = nome.replace(' ', '')
        if nome_sem_espaco != '' and nome_sem_espaco.isalpha():
            confirmacao_valida = False
            while confirmacao_valida == False:
                confirmacao = input("Você deseja participar da seleção de estágio? (S/N)\n")
                if confirmacao == 's' or confirmacao == 'S':
                    lista_de_pessoas.append(nome)
                    confirmacao_valida = True
                    c += 1
                elif confirmacao == 'n' or confirmacao == 'N':
                    confirmacao_valida = True
                else:
                    print("Digite apenas S ou N para confirmar.")
        else:
            print("Nome inválido. Tente novamente")
