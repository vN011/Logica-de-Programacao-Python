import os
os.system("cls")

for i in range(4):
    nota = float(input(f"Informe a {i+1}° nota: "))

    media = ( nota + nota ) / 2

print(f"Sua média é: ", media)