compras = []
c = 0
a = True

while a == True:
    qntd = int(input("Digite a quantidade de produtos que deseja inserir (digite 0 para sair): "))
    for i in range(qntd):
        p = input(f"{i + 1}° produto: ")
        produto = p.replace(" ", "")
        if not produto.isalpha():
            print("Produto inválido.")
            a = False
        else:
            compras.append(produto)

    if qntd == 0:
        a = False
print(f"Produtos cadastrados: {compras}")
            