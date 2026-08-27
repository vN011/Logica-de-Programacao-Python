import os
os.system ("cls")

# Entrada.
primeiro_numero = float(input("Digite o Primeiro número: "))
segundo_numero = float(input("Digite o Segundo número: "))

# Processamento.
soma = (primeiro_numero + segundo_numero)
media = (soma / 2)
produto = (primeiro_numero * segundo_numero)

if primeiro_numero > segundo_numero:
    maior = max (primeiro_numero) 
    menor = min (segundo_numero)
else: 
    maior = segundo_numero
    menor = primeiro_numero
# Saída. 
print(f"\nMédia: {media}")
print(f"\nSoma: {soma}")
print(f"\nProduto: {produto}")
print(f"\nMaior Número: {maior}")
print(f"\nMenor Número: {menor}")