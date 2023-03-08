import random
aluno = []
for i in range(4):
    aluno.insert(i, input('Digite o nome do {}° aluno: '.format(i+1)))
a = random.randrange(0,4)
print(aluno[a])