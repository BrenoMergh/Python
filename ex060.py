num = int(input('Digite um número: '))
i = num - 1
while i > 0:
    num *= i
    i -= 1
print(f'O fatorial é {num}')
