#mesmo princípio do exercicio 64 mas agora usando o break
soma = cont = 0
while True:
    num = int(input('Digite um número: '))
    if num == 999:
        break
    soma += num
    cont += 1
print(f'Foram digitados {cont} números e a soma foi de {soma}')    
