from datetime import datetime
nasc = int(input('Digite o ano que nasceu: '))

if (datetime.now().year - nasc) < 18:
    print('\033[1;30;42mVocê ainda terá que se alistar\033[m')
elif (datetime.now().year - nasc) == 18:
    print('\033[1;30;43mVocê terá que se alistar esse ano\033[m')
else:
    print('\033[1;30;41mVocê está atrasado com seu alistamento\033[m')