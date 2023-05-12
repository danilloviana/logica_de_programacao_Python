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
    print("Perímetro: " + str(per) + chr(13) + "  Área: " + str(area))
