num = int(input('Digite o primeiro termo da P.A: '))
razao = int(input('Digite a razão da P.A: '))
for i in range(num, (num+10*razao), razao):
    print(i)