n50 = n20 = n10 = n1 = 0
saque = int(input('Digite o valor a ser sacado: '))
while saque > 0:
    if saque >= 50:
        n50 = saque // 50
        saque = saque - (n50*50)
    elif saque >= 20:
        n20 = saque // 20
        saque = saque - (n20*20)
    elif saque >= 10:
        n10 = saque // 10
        saque = saque - (n10*10)
    elif saque >= 1:
        n1 = saque // 1
        saque = saque - (n1*1)
print(f'O valor a ser sacado foi {saque}')
if n50 > 0:
    print(f'{n50} Cédulas de R$ 50')
if n20 > 0:
    print(f'{n20} Cédulas de R$ 20')
if n10 > 0:
    print(f'{n10} Cédulas de R$ 10')
if n1 > 0:
    print(f'{n1} Cédulas de R$ 1')