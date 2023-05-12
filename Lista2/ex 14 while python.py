c=1
i=1
s=0
while c<=71:
    s=s+(1/(i**3))
    i=i+2
    c=c+1
pi=(s*32)**(1/3)
print(f"Valor de pi, aproximado é:{pi}")
    
