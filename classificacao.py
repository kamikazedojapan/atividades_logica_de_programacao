c = 0
garotos = 0
garotas = 0
homens = 0
mulheres = 0
print("=" * 30)
a = "Pesquisa do IBGE".rjust(23)
print(a)
print("=" * 30)
while c < 5:
    g = input("Digite o seu gênero (m/f): ")
    if (g != "m" or g != "M" or g != "f" or g != "F"):
        print("Gênero incorreto!") 
    i = int(input("Digite sua idade: "))
    if (i < 0 or i > 122):
        print("Idade incorreta!")
    if (g == "M" or g == "m") and i < 18:
        garotos += 1
    elif (g == "F" or g == "f") and i < 18:
        garotas += 1
    elif (g == "M" or g == "m") and i >= 18:
        homens += 1
    elif (g == "F" or g == "f") and i >= 18:
        mulheres += 1
    c += 1
print("\nGarotos:", garotos)
print("Garotas:", garotas)
print("Homens:", homens)
print("Mulheres:", mulheres)