nome = input('Digite seu nome: ').strip()

'''check = nome.upper().find('SILVA')
if check >= 0:
    print('Você possui o nome Silva')
else:
    print('Você não possui o nome Silva')'''
    
    
print('Seu nome tem silva? {}'. format('SILVA' in nome.upper()))
