import os
os.system ("cls")

# Entrada.
print(f"\nDigite M para Masculino")
print(f"\nDigite F para Feminino")

sexo = str(input(f"\nInforme seu Sexo: ")).upper()
altura = float(input(f"\nDigite sua Altura: "))
peso_m = (72.7 * altura) - 58
peso_f = (62.1 * altura) - 44.7

# Processamento
match sexo:
    case "M":
        print(f"\nSeu peso Ideal é: ", peso_m)
    case "F":
        print(f"\nSeu peso Ideal é: ", peso_f)
# Saída