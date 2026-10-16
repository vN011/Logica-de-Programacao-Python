import os
os.system("cls")

num_vetores = []
soma = 0
negativo = 0
for i in range(5):
    numero = int(input(f"Digite o {i+1}° Número: "))
    num_vetores.append(numero)
    if numero > 0:
        soma = sum(num_vetores)
    else:
        negativo += 1

print(f"Números Negativos: {negativo}")
print(f"Soma dos números Positivos: {soma}")