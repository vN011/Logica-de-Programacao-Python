import os
os.system ("cls")

# Entrada.
nome = (input("Digite seu Nome: "))
media = float(input("Digite sua Média Escolar: "))
faltas = int(input("Digite a quantidade de Faltas: "))

# Processamento.
if media >= 7 and faltas <= 40:

# Saída.
    print("Aprovado!")
else:
    print("Reprovado!")