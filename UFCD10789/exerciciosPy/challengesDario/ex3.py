notas = []

for i in range(10):
    while True:
        inserido = input(f"Insira a nota do aluno {i+1}: ")
        nota = float(inserido)
        if 0 <= nota <= 10:
            notas.append(nota)
            break
        print("Nota inválida. Tem que ser entre 0 e 10.")

media = sum(notas) / len(notas)
print("Média das notas:", media)
