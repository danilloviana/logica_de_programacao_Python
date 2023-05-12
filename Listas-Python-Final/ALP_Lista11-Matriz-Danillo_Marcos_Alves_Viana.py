"""
Faculdade de Tecnologia prof. Rubens Lara
Curso de Tecnologia em Sistemas para Internet


Algoritmos e Lógica de Programação
Sétima Lista de Exercícios - Matrizes
Prof. Jorge Luiz Chiara

Aluno: Danillo Marcos Alves Viana
Curso: Sistemas para Internet
"""

#Construa os programas Python para os seguintes problemas:


#1.	Construir e exibir uma matriz 2x4 de números inteiros quaisquer.

def exibematriz(matriz):
 for lin in range(len(matriz)):
  for col in range (len(matriz[0])):
    print(matriz[lin][col],end="  ")
  print()

import random
matriz=[]
for i in range (2):
    linha=[]
    for j in range (4):
        n=random.randint(1,9)
        linha.append(n)
    matriz.append(linha)
exibematriz(matriz)

#2.	Considere  uma matriz 4x4 de valores inteiros:

#a)	Preencher a matriz com números aleatórios na faixa de 1 a 15.

import random

matriz=[]
for i in range(4):
 linha=[]
 for j in range(4):
     n=random.randint(1,15)
     linha.append(n)
 m.append(linha)
exibematriz(m)

#b)	Calcular e exibir a média aritmética dos valores da matriz.
soma=0
for linha in m:
     for n in linha:
          soma=soma+n
media=soma/16
print(f"Media aritmetica: {media}")

#c)	Criar e exibir uma lista com os valores que são menores que a média dos valores da matriz.

soma=0
for linha in m:
     for n in linha:
         soma=soma+n
media=soma/16
print(f"Media aritmetica: {media}")
media=soma/16
menores=[]
for linha in m:
     for n in linha:
         if n < media:
             menores.append(n)
print(menores)

#d)	Calcular e exibir  a soma dos elementos da diagonal secundária.  

ds=0
for lin in range(len(m)):
     for col in range(len(m[0])):
         if lin+col==len(m)-1:
             ds=ds+m[lin][col]
         print(m[lin][col],end="  ")
print()         
print(f"Soma da Diagonal secundaria: {ds}")

#e)	Calcular e exibir a soma dos elementos da diagonal principal.

print("Elementos da diagonal principal")
dp=0
for lin in range(len(m)):
     for col in range(len(m[0])):
         if lin==col:
             dp=dp+m[lin][col]
         print(m[lin][col],end="  ")
print()         
print(f"Soma da Diagonal principal: {dp}")

#3.	Considerando duas matrizes A e B de ordem  3 (3x3),
#a.	Preenche-las  com números aleatórios entre 1 e 9.

def exibematriz(matriz):			
 for lin in range(len(matriz)):
  for col in range (len(matriz[0])):
    print(matriz[lin][col],end="  ")
  print()

import random
matriz=[]
for i in range (3):
    linha=[]
    for j in range (3):
        n=random.randint(1,9)
        linha.append(n)
    matriz.append(linha)
exibematriz(matriz)


"""b.	Exibir as matrizes A e B.
A=9  3  5  
     9  1  3  
     5  7  6  

B=1  6  4       
     1  9  1  
     6  3  7
c.	Construir a Matriz C, resultado da soma das matrizes A e B."""

#A
def exibematriz(matriz):
 for lin in range(len(matriz)):
  for col in range (len(matriz[0])):
    print(matriz[lin][col],end="  ")
  print()

import random
matriz=[]
for i in range (3):
    linha=[]
    for j in range (3):
        n=random.randint(1,9)
        linha.append(n)
    matriz.append(linha)
exibematriz(matriz)


#B
def exibematriz(matriz):
 for lin in range(len(matriz)):
  for col in range (len(matriz[0])):
    print(matriz[lin][col],end="  ")
  print()

import random
matriz=[]
for i in range (3):
    linha=[]
    for j in range (3):
        n=random.randint(1,9)
        linha.append(n)
    matriz.append(linha)
exibematriz(matriz)

def somaMatrizes(A,B):

C=[]
 for i in range(len(A)):
    linha=[]
    for j in range(len(A[0])):
        list.append(linha.A[i][j]+B[i][j])
    list.append(C,linha)
    return C

#d.	Exibir a matriz C

C=4  5  4
     3  5  7
     3  9  4
     9  4  9
     9  5  8
     1  1  5

#4.	Considerando a matriz M , 5x5 faça,
#a)	Preencha a matriz com números aleatórios na faixa de 1 a 25
def exibematriz(matriz):
 for lin in range(len(matriz)):
  for col in range (len(matriz[0])):
    print(matriz[lin][col],end="  ")
  print()

import random
matriz=[]
for i in range (5):
    linha=[]
    for j in range (5):
        n=random.randint(1,25)
        linha.append(n)
    matriz.append(linha)
exibematriz(matriz)

#b)	Calcule e exiba a soma dos elementos da primeira coluna;
#c)	Calcule e exiba o produto dos elementos da primeira linha;
#d)	Calcule e exiba a soma de todos os elementos da matriz;
#e)	Calcule e exiba a soma do diagonal principal;

def exibematriz(matriz):
 for lin in range(len(matriz)):
  for col in range (len(matriz[0])):
    print(matriz[lin][col],end="  ")
  print()
  
m=[[10,17,15,12,22],  
   [20,13,2,2,16],
   [24,1,21,12,12],  
   [21,14,14,11,5],  
   [18,5,21,24,6],
   ]

import random
matriz=[]
for i in range (5):
    linha=[]
    for j in range (5):
        n=random.randint(1,25)
        linha.append(n)
    matriz.append(linha)
exibematriz(matriz)

print("Elementos da diagonal principal")
dp=0
for lin in range(len(m)):
     for col in range(len(m[0])):
         if lin==col:
             dp=dp+m[lin][col]
         print(m[lin][col],end="  ")
print()         
print(f"Soma da Diagonal principal: {dp}")

