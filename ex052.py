import sys
num = int(input('Digite o número para saber se é primo: '))
for i in range(1, num+1):
    if num == 1:
        print('\033[1;30;41mNÃO É PRIMO\033[m')
        sys.exit()   
    elif i != 1 and i != num:
        if num % i == 0:
            print('\033[1;30;41mNÃO É PRIMO\033[m')
            #exit() ou quit() sai do programa quando executado mas não são recomendados
            sys.exit()
            #A melhor forma de sair de um programa é com o método sys.exit()
print('\033[1;30;42mÉ PRIMO\033[m')