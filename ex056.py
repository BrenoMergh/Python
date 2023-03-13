nome = []
idade = []
sexo = []
soma = 0
velho = 0
contm = 0

for i in range(0,4):
    print('-='*4, '{}ª PESSOA'.format(i+1), '-='*4)
    nome.insert(i, str(input('Digite o nome:')))
    idade.insert(i, int(input('Digite a idade: ')))
    sexo.insert(i, str(input('Digite o sexo [M/F]: ')))
    soma += idade[i]
    if idade[i] > velho and sexo[i] == 'm':
        velho = idade[i]
        nomevelho = nome[i]
    if sexo[i] == 'f' and idade[i] < 20:
        contm += 1
media = soma / 4

print('A média de idade do grupo é de {}anos.'.format(media))
print('O nome do homem mais velho é {} e possui {} anos.'.format(nomevelho, velho))
print('O grupo possui {} mulheres com idade inferior a 20 anos.'.format(contm))