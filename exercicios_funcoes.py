# 1. Crie uma função linja que imprima 40 '='
def linha():
  print('=' * 40)
linha()

# 2. Crie boas_vindas(nome) que exiba uma saudação.
def boas_vindas(n):
  print(f"Seja bem-vindo, {n}!")
boas_vindas("Márcio")

# 2.1 Crie a função acima utilizando input.
""" def boas_vindas1():
  nome = input('Nome: ')
  print(f'Seja bem-vindo, {nome}!')
boas_vindas1()

# 2.2 Faça a mesma função só que agora utilizando return
def boas_vindas2():
  n = input('Nome: ')
  return f"Seja bem-vindo {n}!"

mensagem = boas_vindas2()
print(mensagem) """

# 3. Crie maior(a, b) que informe o maior valor.
def maior(a, b):
  n1 = int(a)
  n2 = int(b)
  if n1 > n2:
    print(f"O maior valor é {n1}.")
  elif n1 < n2:
    print(f"O maior valor é {n2}.")
  else:
    print('Os dois valores são iguais.')

maior(0, 1)

# 4. Crie calcular_media(n1, n2, n3) usando return.
def calcular_media(n1, n2, n3):
  nota1 = float(n1)
  nota2 = float(n2)
  nota3 = float(n3)
  media = (nota1 + nota2 + nota3) / 3
  return f'A média dos 3 números é igual a {media:.2f}'

print(calcular_media(7, 6, 9))

# 5. Crie par_ou_impar(numero).
def par_ou_impar(n):
  if n % 2 == 0:
    print("O número é par.")
  else:
    print("O número é impar.")
par_ou_impar(47)

# 6. Crie uma calculadora com funções para somar, subtrair, multiplicar e dividir.
# calculadora.py

# 7. Crie uma função mostrar_lista(lista)
def mostrar_lista(lista):
  for item in lista:
    print(item)

nome = ["Márcio", "Pedro", "Julio"]
mostrar_lista(nome)