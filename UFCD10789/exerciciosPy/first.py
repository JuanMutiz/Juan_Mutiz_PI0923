opc=0

print("Bem VINDO")
print("Prima 1 para nome do cliente")
print("Prima 2 para IBAN")
opc = input('Intrud opção:')

match opc:
    case 1:
        print("nome")
    case 2:
        print("iban")
        
    case default:
        print("error")
        
num1 = 0
num2 = 0
num3 = 0
        

if num1>num2 and num2>num3:
    print("Numero 1 é o maior Numero 2 é do meio Numero 3 é o menor")
    
'''
num1 > num2 && num2> num3: num1 ser maior num2 ser meio num 3 ser menor

num1> num3 && num3 > num2: num1 ser maior num3 ser meio num2 ser menor

num3 > num3 && num2 > num1: num3 ser maior num2 ser meio num1 ser menor

num3 > num1 && num1>num2: num3 ser maior num1 ser meio num 2 ser menor

num2 > num1 && num1 > num3: num2 ser maior num1 ser meio num3 ser menor

num2> num 3 && num3 > num2: num 2 ser maior num3 ser meio num 2 ser menor
'''

