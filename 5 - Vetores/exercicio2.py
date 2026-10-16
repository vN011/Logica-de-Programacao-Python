import os
os.system("cls")


vetor_numeros = []
quantidade = 5

print("- Solicitando Dados -")
for i in range(quantidade):
    numero = int(input(f"Digite o {i+1}° Número: "))
    
    if numero < 0:
        numero = 0
        
        vetor_numeros.append(numero)
    
print("- Exibindo Dados -")
for posicao, numero in enumerate(vetor_numeros, start=1):
    print(f"{posicao}°: {numero}")