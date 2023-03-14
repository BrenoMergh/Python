total = cont = cont1000 = 0
nomebarato = ''
while True:
    nome = str(input('Digite o nome do produto: ')).lower()
    preco = float(input("Digite o preço do produto: "))
    if cont == 0:
        barato = preco
        nomebarato = nome
    elif preco < barato:
        barato = preco
        nomebarato = nome
    if preco > 1000:
        cont1000 += 1
    total += preco
    continuar = str(input('Deseja continuar com a compra[S/N]? ')).lower()
    while continuar != 's' and continuar != 'n':
        continuar = str(input('Deseja continuar com a compra[S/N]? ')).lower()
    if continuar == 'n':
        break
    cont += 1
print(f'O total gasto foi de R${total:.2f}')
print(f'Temos {cont1000} produtos custam mais de R$ 1000,00')
print(f'O produto mais barato foi {nomebarato} que custa R${barato:.2f}')