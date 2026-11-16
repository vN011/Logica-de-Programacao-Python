import os
os.system("cls")


def inflacao(preco):
    if preco < 100:
        resultado = (preco * 0.10) + preco
        print(f"O valor do seu produto é: {resultado} ")
    else:
        resultado = (preco *0.20) + preco
        print(f"O valor do seu produto é: {resultado} ")
    return

print(" - Solicitando Dados - ")
preco = float(input("Informe o preço do Produto que deseja Comprar: "))

(" - Exibindo Dados - ")
inflacao(preco)