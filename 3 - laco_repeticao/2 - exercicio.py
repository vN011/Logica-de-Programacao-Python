import os
os.system ("cls")

print("= Tabuada =")

print("Soma")
numero = int(input("Digite um número: "))
for i in range(1, 11):
    print (f"{numero} + {i} = {numero + i} ")

print("Subtração")
numero = int(input(f"\nDigite um número: "))
for i in range(1, 11):
    print (f"{numero} - {i} = {numero - i} ")


print("Multiplicação")
numero = int(input(f"\nDigite um número: "))
for i in range(1, 11):
    print (f"{numero} * {i} = {numero * i} ")


print("Divisão")
numero = int(input(f"\nDigite um número: "))
for i in range(1, 11):
    print (f"{numero} / {i} = {numero / i} ")



































