n=int(input("Digite o valor de N "))
cont=1
adc=0
while cont<=n:
    s=1/cont**5
    cont=cont+1
    adc=adc+s
    print(f"\nAdc:{adc}")
