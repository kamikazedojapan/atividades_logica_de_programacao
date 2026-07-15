tarefas = ["Estudar", "Treinar", "Lavar louça"]

while True:
    # Exibe a lista atual de forma simples
    print(f"\nLista atual: {tarefas}")

    # Exibe o menu de opções
    print("--- MENU DE OPÇÕES ---")
    print("1. Adicionar no final ")
    print("2. Inserir no início")
    print("3. Remover pelo nome ")
    print("4. Remover o último da lista ")
    print("5. Sair")
    
    # Recebe a variável "opcao" que pede para o usuario digitar uma opção de 1 a 5.
    opcao = input("Escolha uma opção (1 a 5): ")

    # Se opcao for igual a 1, recebe a variável item, utiliza o método append() para adicionar o item na lista tarefas e mostra uma mensagem no terminal: f"{item} adicionado".
    if opcao == '1':
        item = input("Digite a nova tarefa: ")
        tarefas.append(item)
        print(f"'{item}' adicionado!")

    # Se opcao for igual a 2, recebe a variável item, utiliza o método insert() para inserir o item na lista tarefas e mostra uma mensagem no terminal: f"{item} inserido no início".
    elif opcao == '2':
        item = input("Digite a tarefa prioritária para o início: ")
        tarefas.insert(0, item)
        print(f"'{item}' inserido no início!")

    # Se opção for igual a 3, recebe variável item, se o item estiver dentro da lista, utiliza o método remove() na lista "tarefas" e mostra uma mensagem no terminal: f"{item} removido com sucesso"
    elif opcao == '3':
        item = input("Digite o nome exato da tarefa que quer remover: ")
        if item in tarefas:
            tarefas.remove(item)
            print(f"'{item}' removido com sucesso!")
        # Se caso o item não tiver dentro da lista, mostra a mensagem: "Tarefa não encontrada na lista."
        else:
            print("Tarefa não encontrada na lista.")

    # Se opção for igual a 4, se o tamanho da lista for maior do que 0, recebe variavel "removido" que utiliza o método pop() na lista e mostra uma mensagem no terminal: f"{removido} foi retirado na lista!"
    elif opcao == '4':
        if len(tarefas) > 0:
            removido = tarefas.pop()
            print(f"'{removido}' foi retirado da lista!")
        else:
            print("A lista já está vazia.")

    # Se opcao for igual a 5, mostra no terminal: "Programa encerrado!" e utiliza o break para parar o laço de repetição while
    elif opcao == '5':
        print("Programa encerrado!")
        break

    # Se opção não for um número de 1 a 5, mostra na terminal: "Opção inválida! Digite um número de 1 a 5."
    else:
        print("Opção inválida! Digite um número de 1 a 5.")