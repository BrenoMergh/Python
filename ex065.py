proseg = 's'
cont = soma = maior = menor = 0
while proseg == 's':
    num = int(input('Digite um número: '))
    if cont == 0:
        maior = num
        menor = num
    else:
        if num > maior:
            maior = num
        elif num < menor:
            menor = num
    proseg = str(input('Gostaria de continuar a digitar os número: ')).lower()
    cont += 1
    soma += num
media = soma/cont
print(f'A média foi de {media}')
print(f'A soma de {soma}')
print(f'O maior foi {maior}')
print(f'O menor foi {menor}')
    