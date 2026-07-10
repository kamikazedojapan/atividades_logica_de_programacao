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

# Exercício 2 (Nível Intermediario): Média de Notas Enunciado: Dada a lista
# notas = [7, 8.5, 9, 5]. Crie uma variável soma = 0. Construa um loop for que
# passe por cada nota e a some à variável principal. Ao fim, calcule a média.
soma = 0
notas = [7, 8.5, 9, 5]
for nota in notas:
    soma += nota
media = soma / len(notas)
print(f"Média: {media:.1f}")

# Exercício 3 (Nível Desafio): Múltiplos de 5 Enunciado: Escreva um código 
# usando o loop for com a função range() que passe por todos os números do 1 
# até o 50, e imprima apenas os números que são múltiplos de 5. 
for c in range(5, 51, 5):
    print(c)