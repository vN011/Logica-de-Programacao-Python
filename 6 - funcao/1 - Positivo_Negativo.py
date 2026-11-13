import os
os.system("cls")

def verificar_positivo_negativo(numero):
    if numero == 0:
        resultado = "Neutro"
        return resultado
    elif numero > 0:
        resultado = "Positivo"
        return resultado

print(" - Solicitando Dados - ")
numero = int(input("Insira um número Inteiro: "))

resultado = verificar_positivo_negativo(numero)

print(" - Exibindo Dados - ")
print(f"O número: {numero} é {resultado} ")