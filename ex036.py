casa = float(input('Digite o valor da casa: '))
salario = float(input('Digite o valor do seu salário: '))
anos = int(input('Digite em quantos anos pretende pagar a casa: '))

prest = casa / (anos*12)

if prest > (salario - (salario*0.7)):
    print('\033[1;30;41mEmpréstimo NEGADO!!!\033[m')
else:
    print('\033[1;30;42mEmpréstimo APROVADO!!!\033[m')