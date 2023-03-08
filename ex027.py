nome = input('Digite seu nome completo: ').strip()
s = nome.split()
p = s[0]
u = s[-1]
print('Seu nome é: {}\nPrimeiro nome é: {}\nÚltimo nome é: {}'.format(nome, p, u))
