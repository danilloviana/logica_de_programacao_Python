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



