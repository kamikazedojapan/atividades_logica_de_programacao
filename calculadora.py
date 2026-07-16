c = True

def menu_opcoes():
    print("======= Calculadora =======")
    print("1 - Soma")
    print("2 - Diferença")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("5 - Sair")

def soma(n1, n2):
    soma = n1 + n2
    print(f"\nSoma: {soma}")
    return soma

def diferenca(n1, n2):
    diferenca = n1 - n2
    print(f"\nDiferença: {diferenca}")
    return diferenca

def multiplicacao(n1, n2):
    multiplicacao = n1 * n2
    print(f"\nMultiplicação: {multiplicacao}")
    return multiplicacao

def divisao(n1, n2):
    divisao = n1 / n2
    print(f"\nDivisão: {divisao}")
    return divisao

def confirmacao():
    confirmacao = input("\nDeseja continuar (s/n): ").lower()
    print('\n')
    if confirmacao != "s" and confirmacao != 'n':
        print("Opção inválida.")
    elif confirmacao == 's':
        return
    else:
        c = False


while c == True:
    menu_opcoes()
    opcao = input("\nDigite uma opção: ")
    numero1 = float(input("\n1° Número: "))
    numero2 = float(input("2° Número: "))
    if opcao == '1':
        soma(numero1, numero2)
        confirmacao()
    elif opcao == '2':
        diferenca(numero1, numero2)
        confirmacao()
    elif opcao == '3':
        multiplicacao(numero1, numero2)
        confirmacao()
    elif opcao == '4':
        divisao(numero1, numero2)
        confirmacao()
    elif opcao == '5':
        exit()