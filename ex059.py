num1 = float(input('Digite o 1º valor: '))
num2 = float(input('Digite o 2º valor: '))
print('-='*4,'Escolha uma opção','-='*4)
print('''      [ 1 ] Somar
      [ 2 ] Multiplicar
      [ 3 ] Maior valor
      [ 4 ] Inserir novamente os valores
      [ 5 ] Sair''')
opcao = int(input('Digite a opção desejada: '))
while opcao != 5:
    if opcao == 1:
        soma = num1 + num2
        print(f'\033[1;30;42mA soma entre {num1} e {num2} é {soma}\033[m')
    elif opcao == 2:
        mult = num1 * num2
        print(f'\033[1;30;42mA multiplicação entre {num1} e {num2} é {mult}\033[m')
    elif opcao == 3:
        if num1 > num2:
            print(f'\033[1;30;42mO maior numero é {num1}\033[m')
        elif num1 < num2:
            print(f'\033[1;30;42mO maior numero é {num2}\033[m')
        else:
            print('\033[1;30;42mOs valores são idênticos')
    elif opcao == 4:
        num1 = float(input('Digite o 1º valor: '))
        num2 = float(input('Digite o 2º valor: '))
    else:
        print('\033[1;30;41mDigite uma opção válida\033[m')
    print('-='*4,'Escolha uma opção','-='*4)
    print('''      [1] Somar
      [2] Multiplicar
      [3] Maior valor
      [4] Inserir novamente os valores
      [5] Sair''')  
    opcao = int(input('Digite a opção desejada: '))
    if opcao == 5:
        print('\033[1;30;41mSaindo do programa\033[m')