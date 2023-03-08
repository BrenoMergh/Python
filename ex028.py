import random
think = random.randrange(0,5)
number = int(input('Qual número que o pc pensou?'))
if number == think:
    print('Você acertou!! Parabéns')
else:
    i = 1
    while number != think:
        number = int(input('Tente outra vez: '))
        i = i+1
    print('Até que fim você acertou, precisou apenas de {} tentativas'. format(i))

