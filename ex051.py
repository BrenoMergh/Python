num = int(input('Digite o primeiro termo da P.A: '))
razao = int(input('Digite a razão da P.A: '))
#Fórmula P.A: An = A1 + (n - 1) * r
#No nosso caso seria: DécimoTermo = num (10 - 1) * razao
#Mas como o python não considera o último digito podemos tirar esse -1 => (10 - 1)
for i in range(num, (num + 10 * razao), razao):
    print(i)