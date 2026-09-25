import os
os.system("cls")

for i in range(3):
    nota = float(input(f"Informe a {i+1}° nota: "))

    media = ( nota + nota ) / 2

print(f"Sua média é: ", media)

if media >= 7:
    print(f"Você foi Aprovado! Sua média é: ", media)
elif media >= 4 and media <= 6:
    print(f"Você está em Recuperação! Sua média é: ", media)
else:
    print(f"Você foi Reprovado! Sua média é: ", media)

