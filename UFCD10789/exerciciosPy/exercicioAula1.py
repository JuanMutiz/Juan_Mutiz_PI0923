num1=6
num2=5
num3=7

if num1 < num2 and num1 < num3:
    smallest = num1
    if num2 < num3:
        middle, largest = num2, num3
    else:
        middle, largest = num3, num2
elif num2 < num1 and num2 < num3:
    smallest = num2
    if num1 < num3:
        middle, largest = num1, num3
    else:
        middle, largest = num3, num1
else:
    smallest = num3
    if num1 < num2:
        middle, largest = num1, num2
    else:
        middle, largest = num2, num1
        

print(f"Smallest: {smallest}, Middle: {middle}, Largest: {largest}")