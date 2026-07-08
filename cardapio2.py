from time import sleep

print("=" * 30)
a = "Cardápio Digital".rjust(23)
print(a)
print("=" * 30)
t = 0

b = True
while b == True:
    print("1 - Acarajé - R$ 15")
    print("2 - Moqueca de Peixe - R$ 40")
    print("3 - Moqueca de Camarão - R$ 50")
    print("4 - Salmão Grelhado - R$ 60")
    print("5 - Sair\n")
    c = int(input("Digite uma opção para pedir um prato: "))
    if c == 1:
        print("\nPreparando o Acarajé...")
        sleep(0.3)
        print("Servindo o Acarajé...")
        t += 15
        print(f"Total : R${t}")
        sleep(0.3)
        print("Bom apetite !\n")
        s = input("Você deseja continuar pedindo (S/N)?\n")
        if s == "S" or s == "s":
            continue
        else:
            b = False
            
    elif c == 2:
        print("Preparando a Moqueca de Peixe...")
        sleep(0.3)
        print("Servindo o Moqueca de Peixe...")
        t += 40
        print(f"Total: R${t}")
        sleep(0.3)
        print("Bom apetite !\n")
        s = input("Você deseja continuar pedindo (S/N)?\n")
        if s == "S" or s == "s":
            continue
        else:
            b = False

    elif c == 3:
        print("Preparando a Moqueca de Camarão...")
        sleep(0.3)
        print("Servindo a Moqueca de Camarão...")
        t += 50
        print(f"Total: R${t}")
        sleep(0.3)
        print("Bom apetite !\n")
        s = input("Você deseja continuar pedindo (S/N)?\n")
        if s == "S" or s == "s":
            continue
        else:
            b = False

    elif c == 4:
        print("Preparando o Salmão Grelhado...")
        sleep(0.3)
        print("Servindo o Salmão Gralhado...")
        t += 60
        print(f"Total: R${t}")
        sleep(0.3)
        print("Bom apetite !\n")
        s = input("Você deseja continuar pedindo (S/N)?\n")
        if s == "S" or s == "s":
            continue
        else:
            b = False

    elif c == 5:
        exit()

    else:
        print("Opção Inválida!")