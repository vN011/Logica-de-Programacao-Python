import os
os.system ("cls")

# Entrada.
numero = float(input("Digite o Primeiro número: "))
segundo_numero = float(input("Digite o Segundo número: "))
terceiro_numero = float(input("Digite o Terceiro número: "))

# Processamento.
media = (numero + segundo_numero + terceiro_numero) / 3

if media >= 7:
    resultado = "aprovado"
else:
    resultado = "reprovado"

    #Saída.
print(" Fim do Programa.")