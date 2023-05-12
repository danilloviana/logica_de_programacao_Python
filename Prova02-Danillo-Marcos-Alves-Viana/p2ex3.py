m= [[9,6,2,5,1],[3,1,1,4,1],[1,5,7,6,9],[9,3,3,9,7]]
nimpar=[]
for linha in range(len(m)):
    for coluna in range(len(m[0])):
        if m[linha][coluna]%2>0:
            nimpar.append(m[linha][coluna])
print(nimpar)
