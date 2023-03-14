from random import randrange
cont = 0
while True:
    esc = str(input('Escolha par[p] ou impar[i]: ')).lower()
    print('-='*20)
    if esc == 'p' or esc == 'i':
        pc = randrange(1,6)
        num = int(input('Digite um número de 1 a 5: '))
        if esc == 'p':
            esc = 'PAR'
            if ((pc + num) % 2 == 0):
                print(f'''                  Você escolheu: {esc}
                    Você jogou: {num}
                    PC jogou: {pc}
                    \033[1;30;42mVOCÊ GANHOU!!!\033[m''')
                cont += 1
            else:
                print(f'''                  Você escolheu: {esc}
                    Você jogou: {num}
                    PC jogou: {pc}
                    \033[1;30;41mVOCÊ PERDEU!!!\033[m''')
                break
        elif esc == 'i':
            esc = 'IMPAR'
            if ((pc + num)%2 == 0):
                print(f'''                  Você escolheu: {esc}
                    Você jogou: {num}
                    PC jogou: {pc}
                    \033[1;30;41mVOCÊ PERDEU!!!\033[m''')
                break
            else:
                print(f'''                  Você escolheu: {esc}
                    Você jogou: {num}
                    PC jogou: {pc}
                    \033[1;30;42mVOCÊ GANHOU!!!\033[m''')
                cont += 1
print(f'''\033[1;30;43mVocê venceu {cont} vezes!\033[m''')