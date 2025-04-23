while True:
    try:
        num = int(input("Insira um número: "))
        print()

    except ValueError:
        print("\nInsira um valor válido!\n")

        continue

    for i in range(1, num):
        print(f"{num} + {i} = {num + i}")
        print(f"{num} - {i} = {num - i}")
        print(f"{num} * {i} = {num * i}")
        print(f"{num} / {i} = {num / i}")
        print()

    break