num = int(input("Insira um numero:"))
if (num % 2 == 0 and num != 2) or (num % 3== 0 and num != 3):
    print("numero não é primo")
else:
    print("numero é primo")