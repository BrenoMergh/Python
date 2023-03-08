sal = float(input('Qual seu salário: '))
if sal > 1250:
    print('Seu salário atual de R${:.2f} sofreu um reajuste de 10% e foi para R${:.2f}.'.format(sal, sal+(sal*0.1)))
else:
    print('Seu salário atual de R${:.2f} sofreu um reajuste de 15% e foi para R${:.2f}.'.format(sal, sal+(sal*0.15)))