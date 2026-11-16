import os
os.system("cls")


vetor_nota = []

def calcular_notas(vetor_nota):
    return sum(vetor_nota) / len(vetor_nota)

def mostrar_notas(lista_notas):
    print("\n - Exibindo Notas - ")
    for nota in lista_notas:
        print(f"Nota: {nota} ")
        

def status_do_aluno(media):
    if media >= 7:
        resultado = "Aprovado"
    else:
        resultado = "Reprovado"
    return resultado

lista_notas = []

print(" - Solicitando Notas - ")
for i in range(2):
    while True:
        nota = float(input(f"Digite a {i+1}° Nota: "))
        if nota >= 0 and nota <= 10:
            lista_notas.append(nota)
            break
        else:
            print("Nota inválida, tente novamente!\n")

media = calcular_notas(lista_notas)
status_do_aluno = status_do_aluno(media)

print("\n- Exibindo Resultados - ")
mostrar_notas(lista_notas)
print(f"Média : {media} ")
print(f"Situação do Aluno: {status_do_aluno} ")