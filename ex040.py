nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

media = (nota1 + nota2)/2

if media < 5:
    print('\033[1;30;31mREPROVADO!!!\033[m')
elif media >= 5 and media <= 6.9:
    print('\033[1;30;43mRECUPERAÇÃO!!!\033[m')
else:
    print('\033[1;30;42mAPROVADO!!!\033[m')