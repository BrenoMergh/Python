peso = float(input('Digite seu peso em kg: '))
altura = float(input('Digite sua altura em metros:'))

imc = peso / (altura * altura)

if imc < 18.5:
    print('\033[1;30;44mABAIXO DO PESO!\033[m')
elif 18.5 <= imc <= 25:
    print('\033[1;30;42mPESO IDEAL!\033[m')
elif 25 < imc <= 30:
    print('\033[1;30;43mSOBREPESO!\033[m')
elif 30 < imc <= 40:
    print('\033[1;30;45mOBESIDADE!\033[m')
else:
    print('\033[1;30;41mOBESIDADE MÓRBIDA!\033[m')
    