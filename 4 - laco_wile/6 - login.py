import os
import time
os.system("cls")

login = ("vNs")
senha = ("123")


while True:
    l = input("Digite seu Login: ")
    s = input("Digite sua Senha: ")


    if l == login and s == senha:
        print(f"\nBem Vindo - {login}!")
        break


    else:
        print("Login ou senha Inválidos!")
        print("Tente novamente!.")
        input("Pressione uma tecla para continuar.")
        os.system("cls")





















if login == "Vinicius" and senha == "vns123":
    print(f"\nBem Vindo!")