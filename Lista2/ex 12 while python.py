Python 3.9.5 (tags/v3.9.5:0a7dcbd, May  3 2021, 17:27:52) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> c = 0
n1 = 1
n2 = 1
atual = 1
m = int(input("Digite o valor do m: "))
print(str(n1) + " ", end='', flush=True)
print(n2)
while m <= 0:
    m = int(input("Digite m maior que 0: "))
while c <= m:
    n1 = n2
    n2 = atual
    atual = n1 + n2
    c = c + 1
    # print(Expressão)
