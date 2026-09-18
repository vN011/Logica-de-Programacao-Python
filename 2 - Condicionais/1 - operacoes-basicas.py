import os
os.system ("cls")

# Entrada.
num1 = int(input("Digite o Primeiro Número: "))
num2 = int(input("Digite o Segundo Número: "))
caract = input("Digite um Caracter: ")
# Processamento.
soma = num1 + num2
subtracao = num1 - num2
multiplicacao = num1 * num2
divisao = num1 / num2

print(f"Primeiro Número: ", num1)
print(f"Segundo Número: ", num1)
print(f"Caracter: ", caract)

match caract:
    case "+":
        print("Resultado: ", soma)
    case "-":
        print("Resultado: ", subtracao)
    case "*":
        print("Resultado: ", multiplicacao)
    case "/":
        print("Resultado: ", divisao)



# Saída.