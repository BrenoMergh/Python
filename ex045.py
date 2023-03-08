import random
while True:
    pc = random.randrange(1,4)
    print('-='*20)
    print('Escolha pedra, papel ou tesoura: ')
    print('\033[1;30;42m- 1 para pedra\033[m')
    print('\033[1;30;44m- 2 para papel\033[m')
    print('\033[1;30;45m- 3 para tesoura\033[m')
    print('-='*20)
    escolha = int(input('Digite a sua escolha: '))
    print('-='*20)
    if pc == escolha:
        print('\033[1;30;43mEMPATE!!!\033[m')
    elif (pc == 1 and escolha == 3) or (pc == 2 and escolha == 1) or (pc == 3 and escolha == 2):
        print('\033[1;30;41mPERDEU!!!\033[m')
    elif (pc == 3 and escolha == 1) or (pc == 1 and escolha == 2) or (pc == 2 and escolha == 3):
        print('\033[1;30;42mGANHOU!!!\033[m')
    else:
        print('\033[1;30;46mVALOR INVÁLIDO!!!\033[m')