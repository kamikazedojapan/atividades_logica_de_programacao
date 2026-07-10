# Exercício 1 (Nível Básico): Lista de Amigos Enunciado: Crie uma lista vazia
# chamada amigos. Use o comando input() para pedir o nome de 3 colegas. Use
# o método append() para guardar os nomes. Ao final, imprima a lista.
amigos = []

for c in range(3):
    while True:
        nome = input("Nome: ").strip()

        nome_validado = nome.replace(" ", "")
        
        if nome_validado.isalpha():
            amigos.append(nome_validado)
            break
        
        print('Nome inválido.')

print('\nNomes: ')
for amigo in amigos:
    print(amigo)