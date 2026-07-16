c = True

def menu_opcoes():
    print("======= Calculadora =======")
    print("1 - Soma")
    print("2 - Diferença")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("5 - Sair")

def soma():
    n1 = float(input("1° Número: "))
    n2 = float(input("2° Número: "))
    soma = n1 + n2
    print(f"\nSoma: {soma}")
    return soma

def diferenca():
    n1 = float(input("1° Número: "))
    n2 = float(input("2° Número: "))
    diferenca = n1 - n2
    print(f"\nDiferença: {diferenca}")
    return diferenca

def multiplicacao():
    n1 = float(input("1° Número: "))
    n2 = float(input("2° Número: "))
    multiplicacao = n1 * n2
    print(f"\nMultiplicação: {multiplicacao}")
    return multiplicacao

def divisao():
    n1 = float(input("1° Número: "))
    n2 = float(input("2° Número: "))
    divisao = n1 / n2
    print(f"\nDivisão: {divisao}")
    return divisao

def confirmacao():
    confirmacao = input("Deseja continuar (s/n): ").lower()
    if confirmacao != "s" and confirmacao != 'n':
        print("Opção inválida.")
    elif confirmacao == 's':
        return
    else:
        c = False


while c == True:
    menu_opcoes()
    opcao = input("\nDigite uma opção: ")
    if opcao == '1':
        soma()
        confirmacao()
    elif opcao == '2':
        diferenca()
        confirmacao()
    elif opcao == '3':
        multiplicacao()
        confirmacao()
    elif opcao == '4':
        divisao()
        confirmacao()
    elif opcao == '5':
        exit()