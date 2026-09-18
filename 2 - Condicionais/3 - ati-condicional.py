import os
os.system ("cls")

# Solicitando os Dados.
idade = int(input("Digite sua Idade: "))

# Processando os Dados
if idade < 16:
    print("Não apto ao Voto!.")

elif idade < 18:
    print("Voto Opcional.")

elif idade <= 65:
    print("Voto Obrigatório!.")
else:
    print("Não é obrigado a Votar!.")



