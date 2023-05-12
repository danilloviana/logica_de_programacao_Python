"""
Faculdade de Tecnologia prof. Rubens Lara
Curso de Tecnologia em Sistemas para Internet


Algoritmos e L�gica de Programa��o
S�tima Lista de Exerc�cios - Matrizes
Prof. Jorge Luiz Chiara

Aluno: Danillo Marcos Alves Viana
Curso: Sistemas para Internet
"""
#Estrutura de controle e Repetição: while e for
#Utilizando a estrutura de controle e repetição while... e for..., construa os programas na Linguagem de Programação Python para solução dos problemas descritos abaixo.
#1. Exibir a seguinte série: 1, 2, 3, ...,50


for c in range(1,50+1):
print(c)
c=1
while c<=50:
print (c)
c=c+1


#2. Exibir a seguinte série: 1, 3, 5, 7, ..., 99


for c in range(1,99+1):
print(c)
c=1
while c<=99:
print (c)
c=c+1


#3. Exibir a seguinte série: 1, 2, 3, ..., N


n=int(input("Digite o valor de n:"))
for c in range(1,n+1,1):
print (c)
n=int(input("Digite o valalor de n:"))
c=1
while c<=n:
print (c)
c=c+1


#4. Calcular e exibir a seguinte série: 1 + 2 + 3 +...+ 50.


soma=0
for c in range (1,50+1):
soma=soma+c
print (soma)
c=1
soma=0
while c<=50:
soma=soma+c
c=c+1
print (soma)


#5. Calcular o seguinte produto: 1 x 2 x 3 x 4 x 5 (fatorial do número 5)


f=1
for c in range(1,6,1):
f=f*c
print(f)
c=1
soma=0
while c<=50:
soma=soma+c
c=c+1
print (soma)


#6. Calcular e exibir a quantidade de números pares compreendidos entre M e N, inclusive.


m = int(input("insira o valor M:"))
n = int(input("Insira o valor N:"))
mu = m
nu = 0
while mu <= n:
if mu % 2 == 0:
nu = nu + 1
mu = mu + 1
print("A quantidade total de pares entre " + str(m) + " e " + str(n) + " = " + str(nu))
print("insira o valor M:")
m = int(input())
print("Insira o valor N:")
n = int(input())
nu = 0
for m in range(m, n + 1, 1):
if m % 2 == 0:
nu = nu + 1
print("A quantidade total de pares: " + str(nu))


#7. Calcular e exibir a soma dos números pares menores que 100, inclusive.


n1 = 0
n2 = 2
while n2 <= 100:
print(n2)
n2 = n2 + 2
if n2 % 2 == 0:
n1 = n1 + 1
print("A soma total = " + str(n1))
n1 = 0
n2 = 2
for n2 in range(n2, 100 + 2, 2):
print(n2)
if n2 % 2 == 0:
n1 = n1 + 1
print("A soma total = " + str(n1))


#8. Calcular e exibir o resultado obtido por um número inteiro A elevado a um expoente inteiro B onde A e B são números digitados pelo usuário.


Observação: Não utilize A**B ou AˆB.
a = int(input("Digite o valor de A”))
b = int(input("Digite o valor de B" ))
e = 1
c = 1
while c <= b:
e = e * a
c = c + 1
print(e)
a = int(input("Digite o valor de A"))
b = int(input("Digite o valor de B"))
e = 1
for c in range(1, b + 1, 1):
e = e * a
print(e)


#9.Faça um algoritmo para:


Calcular e exibir o valor da expressão:
y = (x+1) + (x+2) + (x+3) + (x+4) + (x+5) + … (x+100) onde x é um número inteiro digitado pelo usuário.
y = 0
termos1 = 1
termos2 = 0
termos3 = 0
x = int(input("Insira um número"))
while termos1 <= 100:
termos2 = x + termos2
termos3 = termos3 + 1
y = termos2 + y
termos1 = termos1 + 1
print("O valor de y é: " + str(y))
y = 0
termos1 = 1
termos2 = 0
termos3 = 0
x = int(input("Insira um número"))
for termos1 in range(1, 100 + 1, 1):
termos2 = x + termos2
termos3 = termos3 + 1
y = termos2 + y
print("O valor de y é: " + str(y))


#10- Exibir os 20 primeiros números da sequência 3, 9, 27, 81, ... Em seguida, altere o algoritmo para calcular e exibir a soma dos números contidos nessa sequência.


n1 = 1
adicao = 0
mult = 3
while n1 <= 20:
print(mult)
mult = mult * 3
adicao = adicao + mult
n1 = n1 + 1
print("Total:" + str(adicao))
n1 = 1
adicao = 0
mult = 3
for n1 in range(1, 20 + 1, 1):
print(mult)
mult = mult * 3
adicao = adicao + mult
print("Total:" + str(adicao))


#11. Exibir os n primeiros termos da sequência 1, 1, 2, 3, 5, 8, 13, 21, 34, …, onde n é um número inteiro digitado pelo usuário.


n1 = 1
n2 = 1
atual = 1
c=1
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
c = 0
n1 = 1
n2 = 1
atual = 1
m = int(input("Digite o valor do m: "))
print(str(n1) + " ", end='', flush=True)
print(n2)
for m in range(m, 0 + 1, 1):
m = int(input("Digite o valor do m: "))
for c in range(c, m + 1, 1):
n1 = n2
n2 = atual
atual = n1 + n2
print(" " + str(atual), end='', flush=True)


#12. Calcular e exibir o fatorial de um número inteiro, qualquer.


n = int(input("Digite um número: "))
total = 1
for cont in range(1, n + 1, 1):
total = total * cont
print("O fatorial de " + str(n) + " é: " + str(total))
n = int(input("Digite um número: "))
cont = 0
total = 1
while cont <= n:
cont = cont + 1
total = total * cont
print("O fatorial de " + str(n) + " é: " + str(total))


#13. Calcular e exibir o valor da expressão y = 1*x+2*x+3*x+4*x+5*x+…+20*x, onde x é um número inteiro digitado pelo usuário.

c=1
somatermos = 0
multx = 0
x = int(input("Digite um número qualquer: "))
for x in range(x, 0 + 1, 1):
x = int(input("Digite um número maior que 0 "))
for termos in range(1, 20 + 1, 1):
multx = c * x
somatermos = somatermos + multx
c = c + 1
print("A soma do produto é: " + str(somatermos))
c = 1
somatermos = 0
termos = 1
multx = 0
x = int(input("Digite um número qualquer: "))
while x <= 0:
x = int(input("Digite um número maior que 0 "))
while termos <= 20:
multx = c * x
somatermos = somatermos + multx
c = c + 1
termos = termos + 1
print("A soma do produto é: " + str(somatermos))

#14. O valor aproximado de PI pode ser calculado usando-se a série:

s = 0
n = 1
for c in range(1, 1 + 1, 1):
s = s + 1 / (n * 3)
n = n + 2
raiz = s * 32
pix = raiz ** (float(1) / 3)
print("O valor de pi é: " + str(pix))
s = 0
c = 1
n = 1
while c <= 1:
s = s + 1 / (n * 3)
n = n + 2
c = c + 1
raiz = s * 32
pix = raiz ** (float(1) / 3)
print("O valor de pi é: " + str(pix))


#15. Construa um algoritmo que verifique se um dado número inteiro é primo.


n = int(input("Digite o numero n: "))
quant = 0
c = 1
while c <= n:
if n % c == 0:
quant = quant + 1
c = c + 1
if quant == 2:
print("O numero" + str(n) + " é primo!")
else:
print("O numero" + str(n) + "NÃO é primo!")
n = int(input("Digite o numero n: "))
quant = 0
for c in range(1, n + 1, 1):
if n % c == 0:
quant = quant + 1
c = c + 1
if quant == 2:
print("O numero" + str(n) + " é primo!")
else:
print("O numero" + str(n) + "NÃO é primo!")

#16. Faça um algoritmo para somar os números pares compreendidos entre 1 e 100 e ao

final imprimir o resultado
soma = 0
n = 2
while n <= 100:
print(n)
n = n + 2
if n % 2 == 0:
soma = soma + 1
print("Soma: " + str(soma))
soma = 0
for n in range(2, 100 + 1, 1):
print(n)
n = n + 2
if n % 2 == 0:
soma = soma + 1
print("Soma: " + str(soma))

#17- Somatório: Construa os algoritmos que calculem os seguintes somatórios:

k = 1
i = 5
soma = 0
while k >= i:
pot = k ** 2
soma = soma + pot
k = k + 1
print("Somatória" + str(soma))
k = 1
soma = 0
n = int(input("Digite o n: "))
i = n
while n <= 0:
n = int(input("Digite um número maior que zero: "))
i = n
while k <= n:
soma = soma + k
k = k + 1
print("Somatório" + str(soma))

#18-Tabela: Exibir as seguintes séries 1, 2, 3, 4, 5 e 1, 2, 3 no formato de tabela.
#1 1 1 2 1 3 1 4 1 5
#2 1 2 2 2 3 2 4 2 5
#3 1 3 2 3 3 3 4 3 5

for i in range(1,6,1):
for j in range(1,4,1):
print(i,j,end=" ")
print()
i=1
while i<=5:
j=1
while j<=3:
print(i,j,end=" ")
j=j+1
print()
i=i+1

#19-Tabela: Exibir as seguintes séries 1, 2, 3, 4, 5 e 1, 2, 3, 4, 5 no formato de tabela.
#1 1 1 2 1 3 1 4 1 5
#2 1 2 2 2 3 2 4 2 5
#3 1 3 2 3 3 3 4 3 5
#4 1 4 2 4 3 4 4 4 5
#5 1 5 2 5 3 5 4 5 5

for i in range(1,6,1):
for j in range(1,6,1):
print(i,j,end=" ")
print()
i=1
while i<=5:
j=1
while j<=5:
print(i,j,end=" ")
j=j+1
print()
i=i+1

#20-Exibir a tabuada da multiplicação de um número inteiro solicitado pelo usuário. Por exemplo, para o número 5, temos: 5 x 1 = 5 5 x 2 = 10 ... 5 x 10 = 50

mult = 1
n = int(input("Digite um numero: "))
for c in range(0, 9 + 1, 1):
mult = n * c
print("Os resultados da tabuada são: " + str(n) + "x" + str(c) + "=" + str(mult))
c = 0
mult = 1
n = int(input("Digite um numero: "))
while c <= 9:
c = c + 1
mult = n * c
print("Os resultados da tabuada são: " + str(n) + "x" + str(c) + "=" + str(mult))