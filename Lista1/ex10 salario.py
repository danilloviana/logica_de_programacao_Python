
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
    print("Isento")
