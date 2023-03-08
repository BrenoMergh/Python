lar = float(input('Digite a largura em metros: '))
alt = float(input('Digite a altura em metros: '))
area = lar * alt
tinta = area / 2
print('A área da superfície é de {:.2f} e considerando que cada litro de tinta rende 2m², será necessario {:.2f} litros de tinta para toda superfície.'.format(area, tinta))

