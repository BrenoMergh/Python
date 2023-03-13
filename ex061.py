num = int(input('Digite o primeiro termo da P.A: '))
razao = int(input('Digite a razão da P.A: '))
cont = 1
#Fórmula P.A: An = A1 + (n - 1) * r
while cont <= 10:
    print(num)
    num += razao
    cont+=1