import os

os.system("cls")

contator = 0
soma = 0
qtd_notas = 2

while True:
    for i in range (qtd_notas):
        nota = float(input(f"Digite sua nota: "))
    if nota < 0 or nota > 10:
            print("\nNota inválida, Tente novamente!")
            input("Pressionae qualquer tecla para continuar: ")
            os.system("cls")
    else:
            soma += nota
            contator +=1
    if contator == 1:
                break

a = input("Deseja inserir mais uma nota? S para sim ou N para não. ")

if a == "S":
    nota2 = float(input("Informe a Terceira nota: "))
    soma += nota2
    media = soma / qtd_notas
    print(f"Sua média é: {media} ")
else:
    media2 = soma / qtd_notas
print(f"Sua média é {media2}")