
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
