
n = int(input("Digite um número: "))
cont = 0
total = 1
while cont <= n:
    cont = cont + 1
    total = total * cont
print("O fatorial de " + str(n) + " é: " + str(total))



n = int(input("Digite um número: "))
total = 1
for cont in range(1, n + 1, 1):
    total = total * cont
print("O fatorial de " + str(n) + " é: " + str(total))
