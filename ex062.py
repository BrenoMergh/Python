num = int(input('Digite o 1º termo da P.A: '))
r = int(input('Digite a razão da P.A: '))
pa = num
a = 10
c = 0
print('\33[1;36mOs 10 primeiros termos dessa P.A são:\33[m')
while a != 0:
    for i in range(a):
        print(pa)
        pa += r
        c += 1
    a = int(input('- Deseja ver mais quanto termos: '))
print(f'P.A finalizada com {c} termos no total')
