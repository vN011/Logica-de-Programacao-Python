import os
os.system("cls")

lista_produtos = []


def mostrar_dados(lista_produtos):
    for i in range(3):
        print(f"{i+1} - {lista_produtos[i]}")


def solicitando_dados():
    for i in range(3):
        produto = input("Digite o nome do produto: ")
        lista_produtos.append(produto)

print("- Solicitando - ")
solicitando_dados()

print("\n - Exibindo Dados - ")
mostrar_dados(lista_produtos)