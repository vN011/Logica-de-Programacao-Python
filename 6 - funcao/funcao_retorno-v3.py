import os
os.system("cls")

# Função com parâmetros e com retorno.
def calcular_notas(nota1, nota2):
    resultado = (nota1 + nota2) / 2
    return resultado

def verificar_resultado(media):
    if media >= 7:
        resultado = "Você está Aprovado! "
    else:
        resultado = "Você está em Recuperação! "
    return resultado

print(" = Solicitando Notas = ")
nota1 = float(input(f"Informe a Primeira Nota: "))
nota2 = float(input(f"Informe a Segunda Nota: "))

# Usando a Função com parâmetros e com retorno.
# Inserindo o retorno na variável soma.
media = calcular_notas(nota1,nota2)
situacao = verificar_resultado(media)

print(" = Exibindo Notas = ")
print(f"Média: {media}")
print(f"Resultado: {situacao}")


