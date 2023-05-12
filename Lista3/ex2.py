        """  1. Construa um aplicativo que verifique e mostre ao usuário qual combustível compensa utilizar em um automóvel “flex”. Sabe-se que a relação entre o preço do álcool e o preço da gasolina é 0,7."""
        palcool=float (input ("Digite o preço do alcool: "))
        pgasolina= float (input ("Digite o preço da gasolina: "))
        razao= palcool/pgasolina
        if razao >= 0.7:
        print("Abasteça Gasolina")
        else:
        print("Abasteça Álcool")
       