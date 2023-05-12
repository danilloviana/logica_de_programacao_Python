"""
Faculdade de Tecnologia prof. Rubens Lara
Curso de Tecnologia em Sistemas para Internet


Algoritmos e L�gica de Programa��o
S�tima Lista de Exerc�cios - Matrizes
Prof. Jorge Luiz Chiara

Aluno: Danillo Marcos Alves Viana
Curso: Sistemas para Internet
"""

#Construa os programas utilizando a linguagem Pyton, para os problemas abaixo.
#1. Exercicio01
#a. Crie uma lista de números inteiros
#b. Faça a entrada de 10 valores, digitados via teclado.
#c. Mostre os valores digitados na lista.

numeros = []
for c in range(0,10):
    numeros.append(int(input("Número: ")))
    print(numeros)

#2. Exercicio02
#a. Crie uma lista constituída de “String” de caracteres.
#b. Faça a entrada de dados através do teclado.
#c. Ordene a lista
#d. Mostre os valores digitados nessa lista.

letra = []
for c in range(0,5):
    letra.append(str(input("Digite um caractere: ")))
    letra.sort()
    print("lista em ordem alfabética: ", letra)

#3. Exercicio03
#a. Crie uma lista de números inteiros
#b. Preencha a lista com 50 números aleatórios compreendidos entre 1 e 100;
#c. Mostre os valores da lista
#d. Mostre o maior valor entre eles (utilize a instrução for....)
#e. Mostre o menor valor entre eles. (utilize a instrução for....)

import random
def MaiorNum(lista):
max = lista[0]
for x in lista:
    if x > max :
    max = x
return max
def MenorNum(lista):
min = lista[0]
for x in lista:
    if x < min :
    min = x
return min
lista=[]
lista = random.sample(range(1,100),20)
print(lista)
print("Maior valor: ", MaiorNum(lista))
print("Menor valor: ", MenorNum(lista))


#4. Exercicio04
#a. Crie 3 listas, lista1, lista2 e lista3 de números inteiros.
#b. Preencha a lista1 com 20 números aleatórios compreendidos entre 30 e 50.
#c. Preencha a lista2 com 30 números aleatórios compreendidos entre 50 e 70.
#d. Preencha a lista 3 com os elementos das listas lista1 e lista2, respectivamente
#e. Mostre as listas
#f. Qual o maior número contido na lista3? Qual o menor? (utilize a instrução for...)
#g. Mostre a média aritmética dos valores contidos na lista3. (utilize a instrução for...)

import random
def MaiorNum(lista3):
max = lista3[0]
for x in lista3:
    if x > max :
    max = x
    return max
def MenorNum(lista3):
min = lista3[0]
for x in lista3:
    if x < min :
    min = x
    return min
print("Lista1")
lista1=[]
for c in range(20):
    lista1.append(random.randint(30,50))
    print(lista1)
    print("Lista2")
    lista2=[]
for c in range(30):
    lista2.append(random.randint(50,70))
    print(lista2)
    lista3=[]
    lista3 = lista1+lista2
    print("Lista3")
    print(lista3)
print("Maior valor: ", MaiorNum(lista3))
print("Menor valor: ", MenorNum(lista3))