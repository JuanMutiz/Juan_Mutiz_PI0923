nomes = []

while True:
    print("\nMenu:")
    print("1. Introduzir nomes")
    print("2. Listar nomes")
    print("3. Parar o programa")

    opcao = input("\nEscolha uma opção (1, 2, 3): ")

    match opcao:
        case '1':
            nome = input("Digite o nome para adicionar à lista: ")
            nomes.append(nome)
        case '2':
            if nomes:
                print("\nNomes na lista:")
                for nome in nomes:
                    print(nome)
            else:
                print("\nA lista está vazia.")
        case '3':
            print("Programa finalizado.")
            break