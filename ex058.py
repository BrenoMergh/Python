#Mesmo exercício do 28, só com o while, na epoca eu já tinha feito ele assim, caso vc não tenha feito uma oportunidade de refazer, a diferença que agora é de 0 a 10
import random
think = random.randrange(0,11)
number = int(input('Qual número que o pc pensou?'))
if number == think:
    print('Você acertou!! Parabéns')
else:
    i = 1
    while number != think:
        number = int(input('Tente outra vez: '))
        i = i+1
    print('Até que fim você acertou, precisou apenas de {} tentativas'. format(i))
