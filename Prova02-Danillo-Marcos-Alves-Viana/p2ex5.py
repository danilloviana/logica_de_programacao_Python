frase= "Em 1543, o ano em que foi construída a Santa Casa de Misericórdia de Todos os Santos marcou oficialmente a fundação do povoado, conhecido apenas como Porto. A 26 de janeiro de 1839, Santos passou à categoria de cidade."
novafrase=frase.split()
maiores=[]
for palavra in novafrase:
    if len (palavra)>=3:
        maiores.append(palavra)
print(maiores)
    
