import os
import time
os.system("cls")

print(f"\n=== Menu do Restaurante ===")
print(f"\n ( 1 )  R$ 25.00 - Picanha ")
print(f"\n ( 2 )  R$ 20.00 - Lasanha ")
print(f"\n ( 3 )  RS 18.00 - Strogonoff ")
print(f"\n ( 4 )  R$ 15.00 - Bife Acebolado ")
print(f"\n ( 5 )  R$ 5.00 - Pão com Ovo ")

while True:
    prato = int(input(f"\nDigite o Número Do Prato Desejado: "))
    if prato < 1 or prato > 5:
        print("Prato não existente, Tente novamente em alguns segundos.")
        time.sleep(3)
        os.system("cls")


    match prato:
        case 1:
            print(f"\nO Prato: {prato}  é correspondente a Picanha, O custo Total é - R$ 25.00.")
            break
        case 2:
            print(f"\nO Prato: {prato}  é correspondente a Lasanha, O custo Total é - R$ 20.00.")
            break
        case 3:
            print(f"\nO Prato: {prato} é correspondente a Strogonoff , O custo Total é - R$ 18.00.")
            break
        case 4:
            print(f"\nO Prato: {prato}  é correspondente a Bife Acebolado , O custo Total é - R$ 15.00.")
            break
        case 5:
            print(f"\nO Prato: {prato}  é correspondente a Pão com Ovo , O custo total é - R$ 5.00.")
            break