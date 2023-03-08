dia = int(input('Digite quantos dias você ficou com o carro: '))
km = float(input('Digite quantos KM você rodou com o carro: '))
total = (dia * 60) + (km * 0.15)
print('O total a ser pago será de R${:.2f} \nReferente a: \n{} dias com o carro e de {:.2f}km rodado.'.format(total, dia, km))

