import os
os.system ("cls")

# Entrada>
peso = float(input("Digite seu Peso: "))
altura = float(input("Digite sua Altura: "))
imc = (altura * altura) / peso

# Processamento.

if imc < 18.5:
    print (f"\nAbaixo do peso")
elif imc >= 18.6 and 24.9:
    print(f"Peso ideal (Parabéns)")
elif imc >= 25.0 and 29.9:
    print(f"Levemente Acima do Peso")
elif imc >= 30.0 and 34.9:
    print(f"Obesidade Grau 1")
elif imc >= 35.0 and 39.9:
    print(f"Obesidade Grau 2 (Severa)")
else:

    imc > 40
    print("Obesidade Grau 3 (Mórbida)")
# Saída.
