import os
os.system("cls")

qtd_pares = 0
qtd_impares = 0
soma_pares = 0
soma_geral = 0

while True:
    numero = int(input("Digite um número inteiro positivo (0 para encerrar): "))
    
    if numero == 0:
        break
    
    if numero > 0:
        soma_geral += numero
        
        if numero % 2 == 0:
            qtd_pares += 1
            soma_pares += numero
        else:
            qtd_impares += 1

total_numeros = qtd_pares + qtd_impares

print("\n--- RESULTADOS ---")
print("Quantidade de números pares:", qtd_pares)
print("Quantidade de números ímpares:", qtd_impares)

if qtd_pares > 0:
    media_pares = soma_pares / qtd_pares
    print("Média dos valores pares:", media_pares)
else:
    print("Média dos valores pares: Nenhum número par foi digitado.")

if total_numeros > 0:
    media_geral = soma_geral / total_numeros
    print("Média geral dos números lidos:", media_geral)
else:
    print("Média geral: Nenhum número válido foi digitado.")