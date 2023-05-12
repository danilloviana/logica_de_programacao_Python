"""4.	Divisão: Ler três números e efetuar uma divisão, mas somente se o divisor for diferente de zero; quando isto ocorrer, é mostrada uma mensagem de erro apropriada"""


"""
if n1 > n2 and n1 > n3:
    print("O maior é " + str(n1))
else:
    if n2 > n1 and n2 > n3:
        print("O maior é: " + str(n2))
    else:
        print("O maior é: " + str(n3))"""


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
        
