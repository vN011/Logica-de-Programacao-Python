import os


os.system("cls")

print("= Solicitando Dados =")
nome = (input("Digite seu Nome: "))
idade = int (input("Digite sua idade: "))
primeira_nota = float (input("Digite a Primeira nota: "))
segunda_nota = float (input("Digite a Segunda Nota: "))

media = (primeira_nota + segunda_nota) / 2

print("\n= Exibindo Dados =")
print("Nome: ", nome)
print("Idade: ", idade)
print("Primeira nota", primeira_nota)
print("Segunda nota", segunda_nota)
print("Média: ", media)

