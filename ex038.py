valor1 = int(input('\033[1;30;41mDigite o 1° valor: \033[m'))
valor2 = int(input('\033[1;30;42mDigite o 2° valor: \033[m'))

if valor1 > valor2:
    print('O primeiro valor \033[1;30;41m{}\033[m é maior que o segundo valor \033[1;30;42m{}\033[m.'.format(valor1, valor2))
elif valor1 < valor2:
    print('O segundo valor \033[1;30;42m{}\033[m é maior que o primeiro valor \033[1;30;41m{}\033[m.'.format(valor2, valor1))
else:
    print('Os valores digitados \033[1;30;41m{}\033[m e \033[1;30;42m{}\033[m são idênticos.'.format(valor1, valor2))