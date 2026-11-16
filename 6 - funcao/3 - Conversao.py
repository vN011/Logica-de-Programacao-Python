import os
os.system("cls")

centimetros = 100
def conversao(metro):
    conta = (metro * centimetros)
    print(f" {metro} metros Convertido para {conta} Centímetros ")
    return

print(" - Solicitando Dados - ")
metro = float(input("Informe um valor em metros para ser convertido: "))

print("\n - Exibindo Dados - ")
conversao(metro)