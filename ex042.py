reta = []
for i in range(3):
    reta.insert(i, int(input('Digite o tamanho da reta {}: '.format(i+1))))
if reta[0]>=reta[1]+reta[2] or reta[1]>=reta[2]+reta[0] or reta[2]>=reta[0]+reta[1]:
    print('\033[1;30;41mNão é Triangulo\033[m')
else:
    if reta[0] != reta[1] != reta[2] != reta[0]:
        print('\033[1;30;42mTRIÂNGULO ESCALENO\033[m')
    elif reta[0] == reta[1] == reta[2]:
        print('\033[1;30;43mTRIÂNGULO EQUILÁTERO\033[m')
    else:
        print('\033[1;30;44mTRIÂNGULO ISÓSCELES\033[m')