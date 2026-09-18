import os
os.system ("cls")

# Solicitando Dados.
primeiro_numero = int(input("Digite o primeiro número: "))
segundo_numero = int(input("Digite o segundo número: "))

# Processando Dados.

soma = (primeiro_numero + segundo_numero)
produto = (primeiro_numero * segundo_numero)
media = (primeiro_numero + segundo_numero) / 2

if primeiro_numero == segundo_numero:
    print ("Os números (Primeiro e Segundo) são iguais!")

else:

    maior = max(primeiro_numero, segundo_numero)

    menor = min(segundo_numero, primeiro_numero)

    print(f"Maior: {maior}")

    print(f"Menor: {menor}")
# Mostrando os resultados.
print(f"\nSoma: {soma}")
print(f"\nProduto: {produto}")
print(f"\nMédia: {media}")




