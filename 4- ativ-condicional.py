import os
os.system ("cls")

# Solicitando Dados.
primeiro_numero = float(input("Digite o Primeiro Número: "))
segundo_numero = float(input("Digite o Segundo Número: "))
terceiro_numero = float(input("Digite o Terceiro Número: "))

Maior = max(primeiro_numero, segundo_numero, terceiro_numero)
Menor = min(primeiro_numero, segundo_numero, terceiro_numero)

# Exibindo Dados.
print(f"\nPrimeiro Número: {primeiro_numero}")
print(f"Segundo Número: {segundo_numero}")
print(f"Terceiro Número: {terceiro_numero}")

print(f"O Maior número é:", Maior)
print(f"O Menor número é:", Menor)
#( O Uso do f(" Exemplo")Somente quando usar as chaves{}).
