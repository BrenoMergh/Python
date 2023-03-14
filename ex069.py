contidade = contmasc = contfem = 0
while True:
    print('-='*20)
    idade = int(input('Digite a idade: '))
    sexo = str(input('Digite o sexo [M/F]: ')).lower()
    while sexo != 'm' and sexo != 'f':
        sexo = str(input('Digite o sexo [M/F]: ')).lower()
    print('-='*20)
    if sexo == 'f' and idade < 20:
        contfem += 1
    if idade > 18:
        contidade += 1
    if sexo =='m':
        contmasc += 1
    cont = str(input('Deseja continuar [S/N]? ')).lower()
    while cont != 's' and cont != 'n':
        cont = str(input('Deseja continuar [S/N]? ')).lower()
    if cont == 'n':
        break
print(f'Foram cadastradas {contidade} pessoas com mais de 18 anos.')
print(f'Foram cadastradas {contmasc} homens')
print(f'Foram cadastradas {contfem} mulheres com menos de 20 anos')