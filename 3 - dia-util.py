import os
os.system ("cls")

# Entrada.
numero = (input("Digite um Número: "))

# Processamento.
match numero:
    case 1:
        print(f"\nO número: {numero} é um correspondente a um dia útil, Hoje é Segunda-Feira.")
    case 2:
        print(f"\nO número: {numero} é um correspondente a um dia útil, Hoje é Terça-Feira .")
    case 3:
        print(f"\nO número: {numero} é um correspondente a um dia útil, Hoje é Quarta-Feira .")
    case 4:
        print(f"\nO número: {numero} é um correspondente a um dia útil, Hoje é Quinta-feira .")
    case 5:
        print(f"\nO número: {numero} é um correspondente a um dia útil, Hoje é Sexta-Feira .")
    case 6:
        print(f"\nFinal de Semana.")
    case 7:
        print(f"\nFinal de Semana")
    case _:
        print(f"\nDia Inválido.")

print("=== Fim ==="),