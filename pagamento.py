import os
os.system ("cls")

# Entrada.
print("=== Formas de Pagamento===")
print(" ( 1 ) - Pagamento a Vista")
print(" ( 2 ) - Pagamento a Prazo")

pagamento = input(f"\nInforme a Forma de Pagamento: ")

# Processamento.

match pagamento:
    case "1":
        print(f"\nForma de Pagamento: Pagamento a Vista.")
        print(f"\nValor do Produto: R$ 100.00 ")
        print(f"\nValor do Desconto: 10%.")
        print(f"\nTotal a Pagar: R$ 90.00")

    case "2":
        print(f"\nPagamento a Prazo.")
        print(f"\nValor do Produto: R$ 100.00 ")
        print(f"\nQuantidade de Parcelas: 6x. ")
        input(f"\nDigite a Quantidade de Parcelas: ")
        print(f"\nValor por Parcela: R$ 16.66 ")
        print(f"\nTotal a Prazo: R$ 100.00 ")
