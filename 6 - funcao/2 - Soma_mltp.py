import os
os.system("cls")

def realizar_soma(num1,num2):
    soma = num1 + num2
    return soma

def realizar_subtracao(num1,num2):
    subtracao = num1 - num2
    return subtracao


def realizar_multiplicacao(num1,num2):
    multiplicacao = num1 * num2
    return multiplicacao

def realizar_divisao(num1,num2):
    divisao = num1 / num2
    return divisao

print(" - Solicitando Dados - ")
num1 = float(input("Digite o Primeiro Número: "))
num2 = float(input("Digite o Segundo Número: "))

resultadoSoma = realizar_soma(num1,num2)
resultadoSubtracao = realizar_subtracao(num1,num2)
resultadoMultiplicacao = realizar_multiplicacao(num1,num2)
resultadoDivisao = realizar_divisao(num1,num2)


print("\n - Exibindo Dados - ")
print(f"Soma: {resultadoSoma} ")
print(f"Subtração: {resultadoSubtracao} ")
print(f"Multiplicação: {resultadoMultiplicacao} ")
print(f"Divisão: {resultadoDivisao} ")
