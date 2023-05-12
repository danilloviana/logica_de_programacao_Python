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
