import random

lista = []
multip3 = []
for i in range(10):
    n = random.randint(3, 30)
    lista.append(n)
    if n % 3 == 0:
        multip3.append(n)
print(lista)
print(multip3)
