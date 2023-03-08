num = float(input('Digite qual seu saldo: '))
print('Com R${:.2f} você consegue comprar U${:.2f} levando em consideração o valor do dólar de R$ 5,22'
      .format(num, num/5.22))