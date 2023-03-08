num = []
i = 0
for i in range(3):
    num.insert(i, int(input('Digite um numero: ')))
if num[0] > num[1] and num[0] > num[2]:
    maior = num[0]
    if num[1] > num[2]:
        menor = num[2]
    else:
        menor = num[1]
elif num[1] > num[0] and num[1] > num[2]:
    maior = num[1]
    if num[0] > num[2]:
        menor = num[2]
    else:
        menor = num[0]
else:
    maior = num[2]
    if num[0] > num[1]:
        menor = num[1]
    else:
        menor = num[0]
print('O maior número é:', maior, '\nO menor número é:', menor)
