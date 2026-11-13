import os
os.system("cls")

# Função sem retorno e sem parâmetros
def logo_senai():
    os.system("cls")
    print("="*15)
    print(" Senai - Bahia ")
    print("="*15)

# Função sem retorno e com parâmetros
def mostrar_dados(nome,idade):
    print(f"{nome} tem {idade} anos.")

# Função sem retorno e sem parâmetros
logo_senai()
print("\n - Solicitando Dados - ")
nome = input("Digite seu Nome: ")
idade = input("Informe sua Idade: ")

logo_senai()
print("\n - Exibindo Dados - ")
# Função sem retorno e com parâmetros.
mostrar_dados(nome,idade)
