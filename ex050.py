soma = 0
for i in range(0,6):
    num = int(input('Digite o {}° número: '.format(i+1)))
    if num % 2 == 0:
        soma += num
print('\033[1;30;42mA soma dos números pares é {}\033[m'.format(soma))