'''
1. Lista de compras

Crie um programa que permita cadastrar itens em uma lista de compras.

Requisitos:

O programa deve:

Criar uma lista vazia chamada compras.
Pedir para o usuário digitar produtos.
Adicionar cada produto na lista usando append().
Parar quando o usuário digitar "sair".
Mostrar todos os itens cadastrados no final.
'''

compras = []
valor = []
while True:
    print('=' * 35)
    print(('Lista de compras').center(35))
    print('=' * 35)
    print("1 - Adicionar uma compra na lista")
    print("2 - Ver a lista")
    print("3 - Editar uma compra na lista")
    print("4 - Remover uma compra na lista")
    print("5 - Sair")
    e = int(input("\nEscolha uma opção: "))
    if e == 1:
        produto = input("\nItem: ")
        p = produto.replace(" ", "")
        if not p.isalpha():
            print("Valor inválido.")
            break
        else:
            compras.append(p)
            preco = float(input('Preço: '))
            valor.append(preco)
    if e == 2:
        print('=' * 35)
        print(('Lista').center(35))
        print('=' * 35)

        print(f"{'Compra':<20} {'Valor':>12}")
        print('-' * 35)

        for c in range(len(compras)):
            print(f"{compras[c]:<20} R$ {valor[c]:>10.2f}")

        print('\n')
    if e == 3:
        posicao = int(input("Qual a posição do item que você deseja editar: "))
        novo = input("Digite o novo item: ")

        compras[posicao - 1] = novo
    
    if e == 4:
        posicao = int(input("Qual a posição do item que você deseja editar: "))
        
        compras.pop(posicao - 1)
    if e == 5:
        exit()