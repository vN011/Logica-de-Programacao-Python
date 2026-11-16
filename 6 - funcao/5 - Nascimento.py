import os
from datetime import date
os.system("cls")
ano_atual = date.today().year

def idade_usuario(ano):
    resultado = (ano_atual - ano)
    print(f"Você tem {resultado} Anos. ")
    return
print(" - Solicitando Dados - ")
ano = int(input("Informe seu Ano de Mascimento: "))


print("\n - Exibindo Dados - ")
idade_usuario(ano)