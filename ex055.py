peso = []
maior = 0
menor = 0
for i in range(0,5):
    peso.insert(i, float(input('Digite o peso da {}ª pessoa em kg: '.format(i+1))))
    if i == 0:
        maior = peso[0]
        menor = peso[0]
    else:
        if peso[i] > maior:
            maior = peso[i]
        elif peso[i] < menor:
            menor = peso[i]
print('\033[1;30;46mO maior peso foi de {}kg\033[m'.format(maior))
print('\033[1;30;47mO menor peso foi de {}kg\033[m'.format(menor))