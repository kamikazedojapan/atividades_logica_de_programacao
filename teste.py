lista_nome = []
lista_idade = []
for c in range(3):
    nome = input("Nome: ")
    lista_nome.append(nome)
    idade = int(input("Idade: "))
    lista_idade.append(idade)
print('\n')
for c in range(3):
    print(f"{c+1}° pessoa:\nNome: {lista_nome[c]}\nIdade: {lista_idade[c]}\n")