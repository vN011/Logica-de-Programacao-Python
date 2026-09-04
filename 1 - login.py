import os
os.system ("cls")

# Entrada.
login = (input(" Digite seu Login: "))
senha = (input(" Digite sua Senha: "))

# Processamento

# Saída.
if login == "Vinicius" and senha == "vns123":
    print(f"\nBem Vindo!")

else:
    print(f"Login ou Senha Inválidos, Tente Novamente ")