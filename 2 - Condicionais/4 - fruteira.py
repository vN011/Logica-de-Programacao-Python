import os
os.system ("cls")

# Entrada.
print ("""
Frutas      Até 5 Kg          Acima de 5Kg
Morango	  R$ 2,50 por Kg	R$ 2,20 por  Kg
Maçã	  R$ 1,80 por Kg	R$ 1,50 por  Kg
""")
kg_morango = 2.50
kg_maca = 1.80
kg5_morango = 2.20
kg5_maca = 1.50
qtd1 = int(input("Quantos kilos de morango você irá Comprar?: "))
qtd2 = int(input("Quantos kilos de maçã você irá Comprar?: "))
if qtd1 <= 5:
    print("O valor total a ser pago é pelos Moran: ", kg_morango * qtd1 )
elif qtd2 <= 5:
    print("O valor total a ser pago é: ", kg_maca * qtd2 )

if qtd1 >= 5:
    print("O valor a ser pago é: ", kg5_morango)
elif qtd2 >= 5:
    print("O valor a ser pago é:", kg5_maca)



# Processamento.



# Saída