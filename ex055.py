peso = []
maior = 0
for i in range(0,5):
    peso.insert(i, int(input('Digite o peso da {}° pessoa em kg: '.format(i+1))))
    #p = peso[i]
    if peso[i] > maior:
        maior = peso[i]
print('\033[1;30;46mO maior peso foi de {}kg\033[m'.format(maior))