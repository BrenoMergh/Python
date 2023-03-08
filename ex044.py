preco = float(input('Digite o preço do produto: '))
print('-='*20)
print('Escolha a forma de pagamento: ')
print('\033[1;30;42m- 1 para dinheiro ou cheque(10% de desconto)\033[m')
print('\033[1;30;44m- 2 para cartão\033[m')
print('-='*20)
escolha = int(input('Digite a forma de pagamento escolhida: '))
print('-='*20)
if escolha == 1:
    print('Para pagamento a vista, o novo preço do produto é de R${}'.format(preco-(preco*0.1)))
elif escolha == 2:
    print('-='*20)
    print('Escolha em quantas vezes gostaria de parcelar o pagamento ')
    print('\033[1;30;44m- 1 para à vista\033[m')
    print('\033[1;30;45m- 2 para 2x no cartão\033[m')
    print('\033[1;30;46m- 3 para 3x ou mais no cartão\033[m')
    print('-='*20)
    escolha2 = int(input('Digite a forma de pagamento escolhida: '))
    print('-='*20)
    if escolha2 == 1:
        print('\033[1;30;44mPara pagamento a vista no cartão, o novo preço do produto é de R${}\033[m'.format(preco-(preco*0.05)))
    elif escolha2 == 2:
         print('\033[1;30;45mPara pagamento em 2x no cartão, o preço do produto é de R${}\033[m'.format(preco))
    elif escolha2 == 3:
         print('\033[1;30;46mPara pagamento em 3x ou mais no cartão, o novo preço do produto é de R${}\033[m'.format(preco+(preco*0.2)))
    else:
        print('\033[1;30;31mValor inválido\033[m')
else:
    print('\033[1;30;31mValor inválido\033[m')
    
    