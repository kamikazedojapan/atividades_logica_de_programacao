alunos = int(input("Digite quantos alunos tem na turma (0-40): "))
soma_notas = 0
c = 0
while c < alunos:
    if alunos >= 40:
        print("Quantidade de alunos invalida.")
        break
    else:
        nota = float(input(f"Digite a nota do {c + 1}° aluno: "))
        soma_notas += nota
        c += 1
        if alunos == c:
            break
media = soma_notas / alunos
print(f"Soma das notas: {soma_notas}")
print(f"Média das notas: {media}")