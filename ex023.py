num = int(input('Digite um número: '))
'''a = '000' + num
print('unidade:', a[-1])
print('dezena:', a[-2])
print('centena:', a[-3])
print('milhar:', a[-4])'''

u = num // 1 % 10
c = num // 10 % 10
d = num // 100 % 10
m = num // 1000 % 10

print('unidade:', u)
print('dezena:', c)
print('centena:', d)
print('milhar:', m)
    
    