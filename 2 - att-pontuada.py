import os
os.system ("cls")

# Entrada.
nome = input("Informe seu Nome: ")
sexo = input("Informe seu Sexo: ")
estado_civil = input("Informe seu Estado Civil: ")

# Processamento.
if sexo == "Feminino" and estado_civil == "Casada":
    tempo = input("Informe o tempo de Casamento: ")

else:
    exit() # Fim do Programa

# Saída.
print(f"\nSeu Nome é: ", nome)
print(f"\nSeu Sexo é: ", sexo)
print(f"\nSeu Estado civil é: ", estado_civil)
print(f"\nSeu Tempo de Casamento é: ", tempo)


