i=1
s=0
for c in range(1,72):
    s=s+(1/(i**3))
    i=i+2
pi=(s*32)**(1/3)
print(f"Valor de pi, aproximado é:{pi}")
