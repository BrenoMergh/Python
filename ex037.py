num = int(input('Digite um numero inteiro para ser convertido: '))
print('-='*20)
print('Escolha a base da conversão: ')
print('- \033[1;30;42m1 para binário\033[m')
print('- \033[1;30;44m2 para octal\033[m')
print('- \033[1;30;45m3 para hexadecimal\033[m')
print('-='*20)
escolha = int(input('Digite a base da conversão: '))
print('-='*20)
num2 = num

if escolha == 1:
    conversor = ""
    if num == 0:
       conv = 0
    else:
        while num > 0:
            resto = num % 2
            conversor = str(resto) + conversor
            num = num // 2
    conv = conversor
    print('\033[1;30;42mA base escolhida para a conversão foi binário!\033[m')
    print('\033[1;30;42mO número {} em binário é {}\033[m'.format(num2, conv))
    
elif escolha == 2:
    conversor = ""
    if num == 0:
       conv = 0
    else:
        while num > 0:
            resto = num % 8
            conversor = str(resto) + conversor
            num = num // 8
    conv = conversor
    print('\033[1;30;44mA base escolhida para a conversão foi octal!\033[m')
    print('\033[1;30;44mO número {} em octal é {}\033[m'.format(num2, conv))
    
elif escolha == 3:
    conversor = ""
    if num == 0:
       conv = 0
    else:
    print('A base escolhida para a conversão foi hexadecimal!')
    print('O número {} em hexadecimal é {}'.format(num2, conv))
    
else:
    print('Escolha um número de 1 a 3')
