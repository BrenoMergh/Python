num = int(input('Quantos termos quer mostrar? '))
c = 3
t1 = 0
t2 = 1
print('{} => {}'.format(t1, t2), end='')
while c <= num:
    t3 = t1 + t2
    print(' => {}'.format(t3), end='')
    t1 = t2
    t2 = t3
    c += 1