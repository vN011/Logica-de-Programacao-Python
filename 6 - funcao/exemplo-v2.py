import os
os.system("cls")

# Criando uma Função.
def cabecalho():
    print("\n")
    print("="*15)
    print("      Senai")
    print("="*15)

# Usando a Função.
cabecalho()
nome = input("Digite seu Nome: ")

# Usando a Função.
cabecalho()
idade = int(input("Digite sua Idade : "))

# Usando a Função.
cabecalho()
print(f"Nome: {nome}")
print(f"Idade: {idade}")

