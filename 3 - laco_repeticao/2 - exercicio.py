import os
os.system ("cls")

print("= Tabuada =")

print(f"\n- Soma -")
numero = int(input("Digite um número: "))
for i in range(1, 11):
    print (f"{numero} + {i} = {numero + i} ")

print(f"\n- Subtração -")
numero = int(input(f"\nDigite um número: "))
for i in range(1, 11):
    print (f"{numero} - {i} = {numero - i} ")


print(f"\n- Multiplicação -")
numero = int(input(f"\nDigite um número: "))
for i in range(1, 11):
    print (f"{numero} * {i} = {numero * i} ")


print(f"\n- Divisão -")
numero = int(input(f"\nDigite um número: "))
for i in range(1, 11):
    print (f"{numero} / {i} = {numero / i} ")



































