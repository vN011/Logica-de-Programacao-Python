
import os
os.system ("cls")

# Entrada.
nota = int(input("Digite Uma Nota: "))

# Processamento.
if nota >= 0 and nota <= 10:
# Saída.
    print (f"\nSua nota é: {nota}")
else:
    print(f"\nA nota deve estar entr os Números: 0 e 10: ")