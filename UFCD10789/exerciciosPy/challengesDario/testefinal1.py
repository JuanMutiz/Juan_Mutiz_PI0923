def primo(n: int):
    if n < 2:
        return False
    for d in range(2, int(n ** 0.5) + 1):
        if n % d == 0:
            return False
    return True

def contDivisores(n: int):
    total = 0
    for d in range(1, n + 1):
        if n % d == 0:
            total += 1
    return total

def contPerfeitos(lim: int):
    perfeitos = 0
    for val in range(1, lim + 1):
        soma = 0
        for f in range(1, val):
            if val % f == 0:
                soma += f
        if soma == val:
            perfeitos += 1
    return perfeitos

valor = int(input("Digite um número: "))
cont = 0

for atual in range(valor, 0, -1):
    if cont != 0 and cont % 10 == 0:
        op = input("Deseja continuar? S ou N: ")
        if op == 'N':
            break

    div = contDivisores(atual)
    perf = contPerfeitos(atual)
    print(f"O número {atual} tem {div} divisores, com {perf} números perfeitos,", end=" ")
    
    if primo(atual):
        print("e é primo.")
    else:
        print("e não é primo.")
    
    cont += 1

while True:
    print("\nCalculadora")
    print("Operações disponíveis:")
    print("\t+")
    print("\t-")
    print("\t*")
    print("\t/")
    print("\t. - tabuada\n")

    op = input("Escolha a operação: ")
    if op in "+-*/.":
        break

if op == ".":
    n = int(input("Digite o número para a tabuada: "))
    linha = 1
    while linha <= 10:
        if linha != 1 and linha % 20 == 1:
            seguir = input("Deseja continuar? S ou N: ")
            if seguir == 'N':
                break
        print(f"{n} x {linha} = {n * linha}")
        linha += 1
else:
    a = int(input("Digite o primeiro número: "))
    b = int(input("Digite o segundo número: "))

    if op == "+":
        resultado = a + b
    elif op == "-":
        resultado = a - b
    elif op == "*":
        resultado = a * b
    elif op == "/":
        if b != 0:
            resultado = a / b
        else:
            print("Erro: divisão por zero!")
            resultado = None

    if resultado is not None:
        print(f"{a} {op} {b} = {resultado}")
