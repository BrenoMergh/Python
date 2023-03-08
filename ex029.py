velo = int(input('Digite a velocidade do carro em KM: '))
if velo > 80:
    print('Você foi MULTADO!\nO valor da multa foi de R${}'.format((velo-80)*7))
else:
    print('Continue sendo um bom motorista!!!')