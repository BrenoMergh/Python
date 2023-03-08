dist = float(input('Digite a distância em KM: '))
if dist <= 200:
    print('O valor da passagem para uma viagem de {}KM é R${:.2f}'.format(dist, dist*0.5))
else:
    print('O valor da passagem para uma viagem de {}KM é R${:.2f}'.format(dist, dist*0.45))
    