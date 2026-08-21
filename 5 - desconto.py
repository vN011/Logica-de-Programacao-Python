import os

#Limpa o terminal
os.system("cls")

print("= Solicitando Dados =")
valor = float(input("Digite um Valor ="))

# Calculando
# Desconto 10%
desconto = valor * 0.10
valor_com_desconto = valor - desconto

print("\n= Exibindo Dados =")
print("Valor com Desconto de 10%: ", valor_com_desconto)
