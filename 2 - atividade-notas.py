import os
os.system ("cls")

# Entrada.
nome = str(input("Digite Seu Nome: "))
primeira_nota = float(input("Digite a Primeira Nota: "))
segunda_nota = float(input("Digite a Segunda Nota: "))

media = (primeira_nota + segunda_nota) /2

# Processamento.
if media >= 9:
    print(f"\nAprovado! sua média foi: {media}")

elif media >= 7.5 and media < 9:
    print(f"Aprovado! sua média foi: {media}")

elif media >= 6 and media < 7.5:
    print(f"Aprovado! sua média foi: {media}")
elif media >= 4 and media < 6:
    print(f"Reprovado! sua média foi: {media}")
else:
    print(f"Reprovado! sua média foi: {media}")

# Saída.
print(f"\nMaior ou igual a 9: Conceito = A)")
print(f"Maior ou igual a 7.5 e menor que 9: Conceito = B)")
print(f"Maior ou igual a 6 e menor que 7.5: Conceito = C)")
print(f"Maior ou igual a 4 e menor que 6: Conceito = D)")
print(f"Menor que 4: Conceito = E)")
