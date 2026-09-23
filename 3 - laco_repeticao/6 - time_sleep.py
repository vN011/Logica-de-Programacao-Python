import os
import time
os.system ("cls")

num1 = int(input("Digite um Número: "))
for i in range(num1,0,-1):
    print(i)
    time.sleep(1)
print(f"\nFim!")
