num = int(input("Digite um numero de 1 a 13:"))

if num % 2 == 0 and num != 2:
    print("nao primo")
elif num%3 == 0 and num != 3:
    print("nao primo")
    
else:
    print("é meu primo")