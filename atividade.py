# Atividade - Otimizar, documentar e ajustar o código abaixo:
a = 1000
b = 0
c = 0

while c != 4:
    print("\n===== CAIXA ELETRÔNICO =====")
    print("1 - Consultar saldo")
    print("2 - Depositar")
    print("3 - Sacar")
    print("4 - Sair")

    c = int(input("\nEscolha uma opção: "))

    if c == 1:
        print(f"\nSaldo: R$ {a}")

    if c == 2:
        d = float(input("Digite o valor:\nR$"))
        if d < 0:
            print("Valor inválido.")
        else:
            a += d
            print(f"\nR$ {d} foram depositados na sua conta.")
            print(f"Saldo atual: R$ {a}")

    if c == 3:
        s = float(input("Digite o valor:\nR$"))
        if s > a:
            print("Saque inválido.")
        else:
            a -= s
            print(f"\nR$ {s} foram sacados da sua conta.")
            print(f"Saldo atual: {a}")
    
    if c == 4:
        break