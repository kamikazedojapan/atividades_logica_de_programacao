c = 0
soma_idade = 0
ba = 0
pessoas = int(input("Quantas pessoas vão participar da pesquisa? (0-100): "))

while c < pessoas:
    if pessoas < 0 or pessoas > 100:
        print("Quantidade inválida.")
        break
    else:
        idade = int(input("Idade: "))
        if idade < 0 or idade > 120:
            print("Idade inválida.")
            soma_idade = 0
            break
        else:
            soma_idade += idade

        e = input("Estado (utilize somente as duas siglas): ").upper()
        estado = e.replace(" ","")
        if len(estado) > 2 or not estado.isalpha():
            print("Estado incorreto.")
            soma_idade = 0
            break
        else:
            if estado == 'BA':
                ba += 1
        c += 1
media = soma_idade / pessoas

print(f"{ba} baianos participaram da pesquisa")
print(f"Média da idade: {abs(media)}")