num = soma = cont = 0
while num != 999: 
    soma += num
    cont += 1
    num = int(input('Digite um número [999 para parar]: '))
print('A soma dos números foi {} e foram digitados {} números'.format(soma, cont-1))