import os
import time
os.system("cls")

login_salvo = ("vNs")
senha_salva = ("123")
qtd_tentativas = 3
tentativas = 1


while True:
    if tentativas <= 3:
        print(f"Tentativa: {tentativas}")
        login = input(f"\nDigite seu Login: ")
        senha = input(f"\nDigite sua Senha: ")
        tentativas += 1

        if login == login_salvo and senha == senha_salva:
            print(f"\nBem Vindo - {login_salvo}!")
            break

        else:
            print(f"\nLogin ou senha Inválido.")
        print(f"Tente Novamente. \n")
        os.system("cls")

    else:
        print("= Fim =")
    break
