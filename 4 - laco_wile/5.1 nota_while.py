import os
os.system("cls")

soma = 0
qtd_notas = 2
for i in range(qtd_notas):
    while True:
        nota = float(input(f"Digite a {i+1}° nota entre 0 e 10: "))
        if nota < 0 or nota > 10:
            print("Nota inválida, Tente novamente!")
        else:
            soma = soma + nota
            break
            print()

media = soma / qtd_notas
print(f"\nMédia: ", media)
print(" = Fim! = ")