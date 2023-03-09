from datetime import date
nasc = int(input('Digite seu ano de nascimento: '))

idade = date.today().year - nasc

if idade <= 9:
    print('\033[1;30;42mCATEGORIA MIRIM!\033[m')
elif idade <= 14:
    print('\033[1;30;43mCATEGORIA INFANTIL!\033[m')
elif idade <= 19:
    print('\033[1;30;44mCATEGORIA JUNIOR!\033[m')
elif idade <= 20:
    print('\033[1;30;45mCATEGORIA SÊNIOR!\033[m')
else:
    print('\033[1;30;46mCATEGORIA MASTER!\033[m')