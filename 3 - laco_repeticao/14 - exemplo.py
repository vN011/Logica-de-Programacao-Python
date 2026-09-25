import os
os.system("cls")

print("= Acumulando Valores em uma Variável. =")
soma = 0

print(f"\nO valor inicial da variável soma :",soma)

for i in range(3):
    soma += int(input(f"Digite um número para somar: "))

print(f"Valor final da variável soma:",soma)