import os
os.system ("cls")
# Limpa o Terminal.

# Entrada.
print("= Solicitando Dados =")
salario_informado = float(input("Digite o valor do seu Salário: "))

# Processando Dados.

print("= Exibindo Dados =")
salario_minimo = 1621
quantidade_de_salarios = salario_informado / salario_minimo

# Saída.
print("\n= Exibindo Dados =")
print("Quantidade De Salários: ", quantidade_de_salarios)
