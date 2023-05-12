"""
Faculdade de Tecnologia prof. Rubens Lara
Curso de Tecnologia em Sistemas para Internet


Algoritmos e L�gica de Programa��o
S�tima Lista de Exerc�cios - Matrizes
Prof. Jorge Luiz Chiara

Aluno: Danillo Marcos Alves Viana
Curso: Sistemas para Internet
"""

"""Para cada um dos exercícios, abaixo, construa o correspondente programa utilizando a linguagem Python

1. Construa um aplicativo que verifique e mostre ao usuário qual combustível compensa utilizar em um automóvel “flex”. Sabe-se que a relação entre o preço do álcool e o preço da gasolina é 0,7."""


palcool=float (input ("Digite o preço do alcool: "))
pgasolina= float (input ("Digite o preço da gasolina: "))
razao= palcool/pgasolina
if razao >= 0.7:
print("Abasteça Gasolina")
else:
print("Abasteça Álcool")


"""2. Maior entre dois números: Ler dois números inteiros, quaisquer e mostrar na tela uma mensagem indicando qual é o maior, ou se são iguais."""
n1=float (input("Digite o primeiro número: "))
n2=float (input("Digite o segundo número: "))
if n1>n2:
print("O número ",n1," é maior e que o número ",n2)
else:
print("O número ", n2," é maior que o número ",n1)


"""3. Maior entre três números: Ler três números diferentes e mostrar na tela uma mensagem indicando qual é o maior."""
n1= float (input ("Insira N1: "))
n2= float (input ("Insira N2: "))
n3= float (input ("Insira N3: "))
if n1>n2 and n1>n3:
print("O maior é: ",n1)
else:
if n2>n1 and n2>n3:
print("O maior é",n2)
else:
print("O maior é: ",n3)


"""4. Divisão: Ler dois números e efetuar uma divisão, mas somente se o divisor for diferente de zero; quando isto ocorrer, é mostrada uma mensagem de erro apropriada."""
n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))
if n1 > 0 and n2 > 0:
razao = n1 / n2
print("O Resultado da divisão é " + str(razao))
else:
print("Esta operação não pode ser realizada")


"""5. Equação do segundo grau - Ler os coeficientes a, b e c de uma equação de segundo grau e, antes de calcular as raízes, calcular o valor de delta. Se este for negativo, informar que a equação não tem solução real. Se for zero, mostrar a única raiz. Se positivo, mostra as duas raízes."""
import math
a=float (input("Digite o valor de a: "))
b=float (input("Digite o valor de b: "))
c=float (input("Digite o valor de c: "))
delta=b**2-4*a*c
if delta<0:
print(" Essa operação não tem solução real!")
else:
if delta==0:
x1=(-b+math.sqrt(delta)/(2*a))
print("Valor de X1=",x1)
else:
x1=(-b+math.sqrt(delta)/(2*a))
print("Valor de X1=",x1)
x2=(-b+math.sqrt(delta)/(2*a))
print("Valor de X2=",x2)


"""6. Triângulo: Dados 3 valores inteiros A, e C, digitados pelo usuário, verificar se representam um triângulo. Lembre-se que, se A, B e C são lados de um triângulo se e somente se, as medidas dos lados atendem à seguinte expressão: (A<B+C) e (C<A+B) e (B<A+C)."""
Em caso positivo,
• exibir sua classificação quanto aos lados (eqüilátero, isósceles ou escaleno) e seu perímetro.
• Calcular e exibir seu perímetro.
• Calcular e exibir sua área.
Lembre-se que para calcular a área do triângulo, use a fórmula de Herão: Area=sqrt(sp*(sp-A)*(sp-B)*(sp-C)) onde sp=(A+B+C)/2
import math
a= int(input ("Digite o lado A"))
b= int(input ("Digite o lado B"))
c= int(input ("Digite o lado C"))
if a < b + c and c < a + b and b < a + c:
print("Representam um triângulo")
perimetro = a + b + c
sp = float(perimetro) / 2
area = math.sqrt(sp * (sp - a) * (sp - b) * (sp - c))
print(" Área= ",area, " Perímetro= ",perimetro, " Sp= ",sp)
if a == b and a == c:
print("Triangulo equilátero")
else:
if a == b or b == c or a == c:
print("Triangulo isóseles")
else:
print("Triangulo escaleno")
else:
print("Não representam um triângulo")


"""7. Ano bissexto - Um ano é bissexto se for divisível por 4 exceto os séculos, que são bissextos se forem múltiplos de 400. Escreva um programa que determina se um ano é bissexto."""
ano= int(input("Digite o ano"))
if ano % 100 == 0:
if ano % 400 == 0:
print("O ano é bisexto")
else:
print("O ano não é bisexto")
else:
if ano % 4 == 0:
print("O ano é bisexto")
else:
print("O ano não é bisexto")


"""8. Triângulo no plano cartesiano: Dados as coordenadas x e y, digitados pelo
usuário, de cada um dos 3 vértices de um triângulo qualquer, no plano
cartesiano, calcular e exibir:
1. Tamanho dos lados A, B e C
2. Área do triângulo
3. Perímetro do triângulo.
Onde 2 2 d = (x2- x1) +(y2 - y1) """


import math
print("Digite entradas B: ")
xA = float(input("Digite XA "))
yA = float(input("Digite YA "))
print("Digite entradas B: ")
xB = float(input("Digite XB: "))
yB = float(input("Digite YB: "))
print("Digite entradas C: ")
xC = float(input("Digite XC: "))
yC = float(input("Digite YC: "))
dAB = math sqrt((xA - xC) ** 2 + (yA - yB) ** 2)
dAC = math sqrt((xA - xC) ** 2 + (yA - yC) ** 2)
dBC = math sqrt((xB - xC) ** 2 + (yB - yC) ** 2)
if dAB < dBC + dAC and dAC < dAB + dBC and dAB < dAC + dBC:
print("TRIÂNGULO")
per = dAB + dBC + dAC
sp = per / 2
area = math sqrt(sp * (sp - dAB) * (sp - dBC) * (sp - dAC))
print("Perímetro: " + str(per) + chr(13) + " Área: " + str(area))


"""9. Suponha que um caixa disponha apenas de notas de 1, 10 e 100 reais.
Considerando que alguém está pagando uma compra, escreva um algoritmo
que mostre o número mínimo de notas que o caixa deve fornecer como
troco. Mostre também: o valor da compra, o valor do troco e a quantidade de
cada tipo de nota do troco. Suponha que o sistema monetário não utilize
moedas."""


compra = float(input("Digite o valor da compra"))
pagamento = float(input("Digite o valor do pagamento"))
troco = pagamento - compra
if troco == 0:
print(" Não terá troco")
else:
if troco == 100:
nota10 = troco - 10
nota1 = troco % 10
print("Notas de 10= " + str(nota10))
print("Notas de 1= " + str(nota1))
else:
nota100 = troco / 100
nota10 = float(troco % 100) / 10
nota1 = float(troco % 100) / 1
print("Notas de 100= " + str(nota100))
print("Notas de 10= " + str(nota10))
print("Notas de 1= " + str(nota1))


"""10. Dado o valor do salário de um empregado, calcular e exibir o valor pago ao Imposto de Renda, considerando:
Salário em R$
Valor do Imposto
Salário < 100
Isento
100 ≤ Salário < 500
10%
500 ≤ Salário < 2000
18%
Salário ≥ 2000
25% """
salario = float(input("Digite o salário"))
if salario >= 100:
if salario >= 100 and salario < 500:
salario = salario * 0.1
print("Salário (10%): " + str(salario))
else:
if salario >= 500 and salario < 2000:
salario = salario * (float(18) / 100)
print("Salário (18%): " + str(salario))
else:
salario = salario * (float(100) / 25)
print("Salário (25%): " + str(salario))
else:
print("Isento