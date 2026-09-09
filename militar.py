import os
os.system ("cls")

# Entrada.
sexo = (input("Digite seu Sexo: "))
idade = int(input("Digite sua Idade: "))

# Processamento.
if sexo == "Masculino" and idade >= 18:
    print(f"\nServiço Militar Obrigatório! Deve se Apresentar.")
else:

# Saída.
    print(f"\nNão deve se Apresentar")

