import os
os.system("cls")


while True:
    nota = float(input("Informe sua nota: "))
    if nota < 0 or nota > 10:
        print("Nota inválida, Tente novamente!")
    else:
        print(f"\nSua nota é {nota} ")
        break