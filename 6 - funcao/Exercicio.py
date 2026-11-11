import os
os.system("cls")

def logo_senai():
    print("\n")
print("="*15)
print(" SENAI - BAHIA ")
print("="*15)

def mostrar_dados(nome,email,telefone):
    print(f"{nome} tem o email: {email}, e o telefone {telefone} ")

print("- Solicitando Dados -")
nome = input("Digite seu Nome: ")
email = input("Digite seu Email: ")
telefone = input("Digite seu Telefone: ")

print("\n - Exibindo Dados -")
mostrar_dados(nome,email,telefone)
