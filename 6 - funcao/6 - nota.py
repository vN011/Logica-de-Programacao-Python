import os
os.system("cls")

qtd = 3
vetor_nota = []

def media(vetor_nota):
    resultado = sum(vetor_nota) / qtd
    print(f"Sua média é: {resultado}")
    return

print(" - Solicitando Dados - ")
for i in range(qtd):
    nota = float(input(f"Digite a {i+1}° Nota: "))
    vetor_nota.append(nota)

print("\n - Exibindo Dados - ")
media(vetor_nota)