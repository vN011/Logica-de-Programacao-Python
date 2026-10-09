import os
os.system("cls")

vetor_nome = []

for i in range(4):
    nome = str(input(f"Digite o {i+1} nome: "))
    vetor_nome.append(nome) # Inserindo a nota no vetor de notas.

for i in range(4):
    print(f"Nota: {vetor_nome[i]}")


