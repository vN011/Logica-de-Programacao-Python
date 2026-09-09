import os
os.system ("cls")

dia = (input("Digite o Dia da Semana: "))

match dia:

    case "Segunda":
        print(f"\nHoje é Segunda-Feira.")
    case "Terça":
        print(f"\nHoje é Terça-Feira.")
    case "Quarta":
        print(f"\nHoje é Quarta-Feira")
    case "Quinta":
        print(f"\nHoje é Quinta-Feira.")
    case "Sexta":
        print(f"\nHoje é Sexta-Feira")
    case "Sábado" | "Domingo":
        print(f"\nHoje é Fim de Semana.")
    case _:
        print(f"\nDia Inválido.")

print(dia)

print("=== Fim ==="),