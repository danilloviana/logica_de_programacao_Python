"""
Faculdade de Tecnologia prof. Rubens Lara
Curso de Tecnologia em Sistemas para Internet


Algoritmos e L�gica de Programa��o
S�tima Lista de Exerc�cios - Matrizes
Prof. Jorge Luiz Chiara

Aluno: Danillo Marcos Alves Viana
Curso: Sistemas para Internet
"""

#utilizando a linguagem de programação Python para solução dos problemas abaixo:
#1. Considerando uma frase digitada pelo usuário, pede-se para imprimir:
#a. A quantidade de caracteres
"""frase = input('')
print (len(frase))
b. Separar (split) a frase nos espaços em branco.
frase = input('')
print (frase.split(' '))
c. A frase invertida
frase = input('')
print (frase[::-1])
d. Toda a frase em caixa alta
frase = input('')
print (frase.upper())
e. Toda a frase em caixa baixa
frase = input('')
print (frase.lower())"""


#2. Considerando uma frase digitada pelo usuário, pede-se para verificar se é uma frase palíndromo, não levando em consideração espaços e caracteres especiais ou acentuados.

frase = input('')
fraseSemEspacos = frase.replace(' ', '')
fraseMinúscula = fraseSemEspacos.lower()
fraseInvertida = fraseMinúscula[::-1]
if fraseInvertida==fraseMinúscula:
    print ("Frase palíndromo")
else:
    print ("Não é frase palíndromo")

#3. Leia uma frase e exiba quantas vogais aparecem na frase.

frase="dia lindo"
contador = 0
for letra in frase:
    if letra in "aeiouAEIOU":
    contador += 1
print ("A frase {} tem {} vogais".format(frase, contador))

#4. Faça um programa que leia uma string e um caractere e diga quantas vezes o caractere aparece na string

frase="A casa da vovó"
contador=0
for letra in frase:
    if letra in "aA":
    contador +=1
print ("A frase {} tem {} caracteres".format(frase, contador))

#5. Faça um programa que leia uma string e crie uma outra string repetindo os caracteres. Ex: carro => ccaarrrroo

frase = str(input("Digite sua frase: "))
resultado = ''
for letras in frase:
    resultado += letras*2
    print(resultado)

#6. Faça um programa que leia uma string e crie uma outra string repetindo apenas as vogais Ex: carro => caarroo

S = input("Digite uma palavra: ")
def vogal(ch):
ch = ch.upper()
if (ch == 'A' or ch == 'E' or
    ch == 'I' or ch == 'O' or
    ch == 'U'):
    return True
else:
    return False
    def duplicaVogal(S):
    t = len(S)
    res = ""
for i in range(t):
    if (vogal(S[i])):
    res += S[i]
    res += S[i]
    return res
    res = duplicaVogal(S)
    print(res)

#7. Faça um programa que leia duas strings e imprima a interseção entre elas. Ex: cabelo e pelo => e, l, o

#8. Uma entidade beneficente fez um sorteio cujos bilhetes continham números de 6 dígitos. O sorteio foi baseado nos dois primeiros prêmios da loteria federal, sendo o número sorteado formado pelos três últimos dígitos do primeiro e do segundo prêmio. Por exemplo, se o primeiro prêmio fosse 34.582 e o segundo 54.098, o número da LBV seria 582.098. Escreva um programa que lê os dois prêmios e retorna o número sorteado.

premio1 = input("Premio 1: ")
premio2 = input("Premio 2: ")
print(premio2[-3:])
print("Numero sorteado é: {}.{}".format(premio1[-3:],premio2[-3:]))

#9. Um pangrama é uma frase que contém pelo menos uma vez cada uma das 26 letras do novo alfabeto Português. Um exemplo de pangrama é: “um pequeno jabuti xereta chamado kya viu dez cegonhas felizes e gritou iwup, iwup!”
#Construa um programa Python para ler uma frase e verificar se é ou não um pangrama.
#Outras frases a serem verificadas:
#jackdawf loves my big quartz sphinx
#abcdefghijklmnopqrstuvwxyz
#ola mundo

import string

def pangrama(frase):
    alfabeto = "abcdefghijklmnopqrstuvwxyz"
    for char in alfabeto:
        if char not in frase.lower():
            return False
    return True

frase1 = "jackdawf loves my big quartz sphinx"
frase2 = "abcdefghijklmnopqrstuvwxyz"
frase3 = "ola mundo"

print("jackdawf loves my big quartz sphinx:")
if pangrama(frase1):
    print("É um pangrama")
else:
    print("Não é um pangrama")

print("\nabcdefghijklmnopqrstuvwxyz")
if pangrama(frase2):
    print("É um pangrama")
else:
    print("Não é um pangrama")

print("\nola mundo")
if pangrama(frase3):
    print("É um pangrama")
else:
    print("Não é um pangrama")
