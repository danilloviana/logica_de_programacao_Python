
import math
a= int(input ("Digite o lado A"))
b= int(input ("Digite o lado B"))
c= int(input ("Digite o lado C"))
if a < b + c and c < a + b and b < a + c:
    print("Representam um triângulo")
    perimetro = a + b + c
    sp = float(perimetro) / 2
    area = math.sqrt(sp * (sp - a) * (sp - b) * (sp - c))
    print("  Área= ",area, "  Perímetro= ",perimetro, "  Sp= ",sp)
    if a == b and a == c:
        print("Triangulo equilátero")
    else:
        if a == b or b == c or a == c:
            print("Triangulo isóseles")
        else:
            print("Triangulo escaleno")
else:
    print("Não representam um triângulo")




