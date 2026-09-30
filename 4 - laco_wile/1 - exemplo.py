import os
os.system("cls")

while True:
    n = int(input("Digite um Número entre 1 e 10: "))
    if n < 1 or n > 10:
        print("Número inválido, tente novamente!")
    else:
        print("O número está entre 1 e 10.")
# Serve para parar o laço de repetição
        break

print(" = FIM! = ")