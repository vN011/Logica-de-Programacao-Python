import os
os.system("cls")

lista_jogadores = []

while True:
    os.system("cls")
    print("""
- Jogadores do Bahia -
1 - Cadastrar Jogador
2 - Listar todos os Jogadores
3 - Atualizar Jogador
4 - Remover Jogador
5 - Buscar por Jogador
0 - Sair
        """)

    opcao = int(input(" Escolha uma opção: "))
    match opcao:
        case 1:
            print("- Cadastrar Jogador -")
            nome = (input("Informe o nome do Jogador: "))
            posicao = (input("Informe a posição do Jogador: "))
            camisa = int(input("Informe o número da camisa do Jogador: "))