num = int(input('Digite o número que gostaria saber a tabuada: '))
for i in range(11):
    print('{} x {} = {}'.format(num, i, i*num))