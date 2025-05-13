while True:
    try:
        num = int(input("Insira um número: "))
        print()
        if num <= 1:
            print("Por favor, insira um número maior que 1.\n")
            continue
    except ValueError:
        print("\nInsira um valor válido.\n")
        continue

    operacoes = 0

    for i in range(1, num):
        print(f"{num} + {i} = {num + i}")
        operacoes += 1

        print(f"{num} - {i} = {num - i}")
        operacoes += 1

        print(f"{num} * {i} = {num * i}")
        operacoes += 1

        print(f"{num} / {i} = {num / i:.2f}")
        operacoes += 1

    print(f"\nTotal de operações efetuadas: {operacoes}")
    break
