reta = []
for i in range(3):
    reta.insert(i, int(input('Digite o tamanho da reta {}: '.format(i+1))))
if reta[0]>=reta[1]+reta[2] or reta[1]>=reta[2]+reta[0] or reta[2]>=reta[0]+reta[1]:
    print('Não é Triangulo')
else:
    print('É triangulo')