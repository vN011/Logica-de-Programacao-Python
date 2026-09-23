import os
os.system("cls")

pares = 0
impares = 0


for i in range(5):
    n = int(input("Digite um Número: "))
    if n % 2 == 0:
        pares = pares + 1
    else:
        impares = impares + 1

print(f"\nA quantidade de Pares é : ",pares)
print(f"\nA quantidade de Impares é : ",impares)

print(f"\nFim!")