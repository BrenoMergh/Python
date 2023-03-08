from random import shuffle
aluno = []
for i in range(4):
    aluno.insert(i, input('Digite o nome do {}° aluno: '.format(i+1)))
shuffle(aluno)
print(aluno)