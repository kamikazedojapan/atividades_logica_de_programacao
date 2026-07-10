# Exemplo 1: Iterando sobre uma lista
# Neste exemplo, o laço for percorre cada elemento da lista “frutas” 
# e atribui o valor de cada elemento à variável “fruta”. 
# Em seguida, imprimimos a variável “fruta” na tela.

print('Exemplo 1:')
frutas = ['maça', 'banana', 'laranja']
for fruta in frutas:
    print(fruta)
print('\n')

# Exemplo 2: Iterando sobre um intervalo numérico.
# Utilizamos a função range() para gerar uma sequência de números. 
# Neste exemplo, o laço for itera sobre os números de 1 a 5 e imprime cada número na tela.
print('Exemplo 2:')
for i in range(6):
    print(i)
print('\n')

# Após o término normal do laço for em Python, quando todas as iterações foram concluídas, 
# executamos a instrução else. Este exemplo imprime os números de 0 a 4 e, em seguida, 
# imprime a mensagem “Laço concluído!”.
print('Exemplo 3:')
for i in range(5, 0, -1):
    print(i)
else:
    print('Laço concluído!')
print('\n')

# A instrução “break” é uma forma eficiente de evitar a execução de iterações desnecessárias 
# em situações em que modificamos a condição de saída da iteração em algum ponto do laço. 
# Neste exemplo, o laço for percorre a lista “frutas” e imprime cada elemento até que 
# encontremos a palavra “melão”. Nesse momento, interrompemos o laço.
print('Exemplo 4:')
frutas = ['maça', 'banana', 'uva', 'abacaxi', 'melão', 'goiaba']
for fruta in frutas:
    if fruta == 'melão':
        break
    print(fruta)

# Utilizando a função range() em um laço for. A função range() em Python é uma forma 
# conveniente de gerar uma sequência de números em um laço for. A sintaxe básica da 
# função range() é range(start, stop, step), onde “start” é o número inicial da sequência, “stop” é o número final (não incluso) e “step” é o incremento entre os números da sequência.
print('Exemplo 5:')
for i in range(1, 10, 2):
    print(i)