import os
import time
os.system("cls")

print("Realize o cadastro para fazer login.")

usuario = (input(f"\nDigite um nome de usuário: "))
senha = (input("Digite a senha para realizar login: "))
print(f"\nCadastro realizado!")
input("Pressione qualquer tecla para realizar login.")
time.sleep(3)
os.system("cls")


print("Bem vindo!")
print(f"\nRealize login para acessar o site. ")
while True:
    l = input("Digite seu Login: ")
    s = input("Digite sua Senha: ")


    if l == usuario and s == senha:
        print(f"\nBem Vindo - {usuario}!")
        break


    else:
        print("Login ou senha Inválidos!")
        print("Tente novamente!.")
        input("Pressione uma tecla para continuar.")
        os.system("cls")
