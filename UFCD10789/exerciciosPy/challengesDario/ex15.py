for i in range(256):
    print(f"Código ASCII: {i}")

    if (i + 1) % 21 == 0:
        escolha = input("ENTER para continuar ou 's' para sair: ")
        if escolha == 's' or escolha  == 'S':
            print("Saindo")
            break