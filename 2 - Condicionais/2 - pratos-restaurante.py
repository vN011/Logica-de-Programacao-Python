import os
os.system ("cls")

# Entrada.
print(f"\n=== Menu ===")
print(f"\n ( 1 ) Picanha ")
print(f"\n ( 2 ) Lasanha ")
print(f"\n ( 3 ) Strogonoff ")
print(f"\n ( 4 ) Bife Acebolado ")
print(f"\n ( 5 ) Pão com Ovo ")

numero = int(input(f"\nDigite o Número Do Prato Desejado: "))
# Processamento.

match numero:
    case 1:
        print(f"\nO Prato: {numero}  um correspondente a Picanha, O custo Total é - R$ 25.00.")
    case 2:
        print(f"\nO Prato: {numero}  um correspondente a Lasanha, O custo Total é - R$ 20.00.")
    case 3:
        print(f"\nO Prato: {numero} um correspondente a Strogonoff , O custo Total é - R$ 18.00.")
    case 4:
        print(f"\nO Prato: {numero}  um correspondente a Bife Acebolado , O custo Total é - R$ 15.00.")
    case 5:
        print(f"\nO Prato: {numero}  um correspondente a Pão com Ovo , O custo total é - R$ 5.00.")










