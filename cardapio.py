from time import sleep

print("=" * 30)
a = "Cardápio Digital".rjust(23)
print(a)
print("=" * 30)

b = True
print("1 - Acarajé - R$ 15")
print("2 - Moqueca de Peixe - R$ 40")
print("3 - Moqueca de Camarão - R$ 50")
print("4 - Salmão Grelhado - R$ 60")
print("5 - Sair\n")
c = int(input("Digite uma opção para pedir um prato: "))

while b == True:
    if c == 1:
        print("Preparando o Acarajé...")
        sleep(0.3)
        print("Servindo o Acarajé...")
        sleep(0.3)
        print("Bom apetite !")
        b = False
    elif c == 2:
        print("Preparando a Moqueca de Peixe...")
        sleep(0.3)
        print("Servindo o Moqueca de Peixe...")
        sleep(0.3)
        print("Bom apetite !")
        b = False
    elif c == 3:
        print("Preparando a Moqueca de Camarão...")
        sleep(0.3)
        print("Servindo a Moqueca de Camarão...")
        sleep(0.3)
        print("Bom apetite !")
        b = False
    elif c == 4:
        print("Preparando o Salmão Grelhado...")
        sleep(0.3)
        print("Servindo o Salmão Gralhado...")
        sleep(0.3)
        print("Bom apetite !")
        b = False
    elif c == 5:
        exit()
    else:
        print("Opção Inválida!")