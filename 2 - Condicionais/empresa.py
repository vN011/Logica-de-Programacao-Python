import os
os.system ("cls")

# Entrada.
matricula = int(input("Informe sua Matrícula: "))
idade = int(input("Digite sua Idade: "))
tempo_trabalho = int(input("Digite Quanto tempo você Trabalhou: "))

# Processamento.
if idade >= 65 and tempo_trabalho >= 30:
    print(f"\nRequerer Aposentadoria!")
else:
    print(f"\nNão Requerer Aposentadoria.")

# Saída.
print(f"\nSua Matrícula é: ", matricula)
print(f"\nSua Idade é: ", idade)
print(f"\nSeu Tempo de Trabalho é: ", tempo_trabalho)
