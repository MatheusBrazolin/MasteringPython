
print('lista de nomes para formatura:')

alunos=list()
for i in range (0, 5, 1):
    nome = input('Digite o nome do formando: ')
    alunos.append(nome)

print ('Os nomes dos formandos são:')

for aluno in alunos:
    print(aluno)

