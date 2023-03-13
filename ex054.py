from datetime import date
ano = []
maior = 0
for i in range(0,7):
    ano.insert(i, int(input('Digite o ano de nascimento da {}ª pessoa: '.format(i+1))))
    if (date.today().year - ano[i]) >= 18:
        maior += 1
if maior == 0:
    print('Nenhuma pessoa é maior de idade')
else:
    if maior == 1:
        print('Das 7 pessoas apenas {} é maior de idade'.format(maior))
    elif maior < 7:
        print('Das 7 pessoas apenas {} são maiores de idade'.format(maior))
    else:
        print('Todas as 7 pessoas são maiores de idade')

    