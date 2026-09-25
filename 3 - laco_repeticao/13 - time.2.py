import os
import time
os.system("cls")

n = int(input("Digite um Número: "))

for i in range(n,0,-1):
    print(i)
    time.sleep(1)
print(f"\nFim!")