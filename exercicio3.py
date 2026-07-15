#Exercicio 3 - otimizar, debugar e documentar o código: 
produtos = []
precos = []

while True:

    print("===== LOJA PYTHON =====")
    print("1 - Adicionar Produto")
    print("2 - Ver produtos")
    print("3 - Valor total de todos os produtos")
    print("4 - Encontrar produto")
    print("5 - Sair")

    opcao = input("\nEscolha uma opção: ")

    if opcao == "1":
        nome = input("Nome do produto: ")
        preco = float(input("Preço: "))

        produtos.append(nome)
        precos.append(preco)

        print("\nVenda cadastrada!\n")

    elif opcao == "2":
        if len(produtos) == 0:
            print("\nNenhuma venda cadastrada.")
        else:
            for i in range(len(produtos)):
                print(f"\n{i+1} - {produtos[i]}- R$ {precos[i]}\n")

    elif opcao == "3":
        total = 0

        for valor in precos:
            total += valor

        print(f"\nTotal vendido: R$ {total}\n")

    elif opcao == "4":
        busca = input("Digite o produto: ")

        if busca in produtos:
            indice = produtos.index(busca)

            print("Produto encontrado!")
            print("Nome:",produtos[indice])
            print("Preço: R$",precos[indice])
        else:
            print("\nProduto não encontrado.\n")

    elif opcao == "5":
        print("Encerrando...")
        break

    else:
        print("Opção inválida.")