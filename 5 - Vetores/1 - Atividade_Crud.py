import os
os.system("Cls")
# Crud ?

lista_pacientes = []

while True:
    os.system("cls")
    print("""
- Cadastrando Pacientes -
1 - Cadastrar Paciente
2 - Listar todos as Pacientes
3 - Atualizar Paciente
4 - Remover Paciente
5 - Buscar por Paciente
0 - Sair
""")
    
    opcao = int(input(" Escolha uma opção: "))
    
    match opcao:
        case 1:
            # Create ( Criar, Cadastrar )
            print("- Cadastrar Paciente - ")
            nome_paciente = input("Digite o Nome e Sobrenome do Novo Paciente: ").strip().upper()
            if nome_paciente == "":
                print("O nome do Paciente deve ser inserido...")
            elif nome_paciente in lista_pacientes:
                print("Paciente já Cadastrado")
            else:
                lista_pacientes.append(nome_paciente)
                print("Paciente cadastrado com Sucesso!")
                

        case 2:
            # Read ( Filtrar, Buscar )
            print(" - Pacientes Cadastrados - ")
            for Paciente in lista_pacientes:
                print(f"- {Paciente}")
            print(f"Total: {len(lista_pacientes)}")

        case 3:
            # Update ( Atualizar )
            print("- Atualizar Paciente - ")
            nome = input("Qual Paciente deseja Atualizar? ")
            if nome in lista_pacientes:
                posicao = lista_pacientes.index(nome)
                novo = input("Novo nome: ")
                lista_pacientes[posicao] = novo
                print("Paciente Alterado com Sucesso!")
            else:
                print("Paciente não Encontrado.")

        case 4:
            # Delete ( Remover )
            print("\n- Remover Paciente - ")
            nome = input("Qual Paciente deseja Remover? ")
            if nome in lista_pacientes:
                lista_pacientes.remove(nome)
                print("Paciente Excluido com Sucesso!")
            else:
                print("Paciente não Encontrado.")

        case 5:
            # Read ( Filtrar, Buscar )
            print("\n- Encontrar Paciente - ")
            nome = input("Qual Paciente Deseja Encontrar? ")
            if nome in lista_pacientes:
                print("Paciente Encontrado!")
            else:
                print("Paciente não Encontrado.")
            

        case 0:
            print("Saindo do Programa...")
            break

        case _:
            print("Opção inválida! \n Tente novamente...")
            
    input("Pressione qualquer tecla para continuar")