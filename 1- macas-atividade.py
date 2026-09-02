import os
os.system ("cls")

# Entrada.
macas = float(input("Digite a quantidade de Maçãs desejadas: "))

# Processamento
maior = 1.00
menor = 1.30
total_1 = macas * maior
total_2 = macas * menor
# Saída.
if macas >= 12:
    print(f"\nO Valor Total é de R$:  {total_1}")
else:
    print(f"\nO Valor Total é de R$:  {total_2}")
