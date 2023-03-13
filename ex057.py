sexo = str(input('Digite o sexo[M/F]:')).upper()
while (sexo != 'M' and sexo != 'F'):
    print('Digite um sexo válido')
    sexo = str(input('Digite o sexo[M/F]:')).upper()
print('Sexo {} registrado com sucesso'.format(sexo))