nome = input('Digite o nome da sua cidade: ').strip()
check = nome.upper().find('SANTO')
if check == 0:
    print('Sua cidade começa Santo no nome')
else:
    print('Sua cidade não começa Santo no nome')
