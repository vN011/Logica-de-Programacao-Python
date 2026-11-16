import os
os.system("cls")

qtd = 3
vetor_nota = []

def calcular_notas(vetor_nota):
    return sum(vetor_nota) / len(vetor_nota)

def mostrar_resultados(media, vetor_notas):
    print("\n - Exibindo Dados - ")
    for nota in vetor_nota:
        print(f"Nota: {nota} ")

    print(f"Média: {media} ")

print(" - Solicitando Dados - ")
for i in range(qtd):
    nota = float(input(f"Digite a {i+1}° Nota: "))
    vetor_nota.append(nota)


media = calcular_notas(vetor_nota)

mostrar_resultados(media, vetor_nota)