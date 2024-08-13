pronomes = ['seu', 'sua']
perguntas = [ 'nome', 'missão', 'cor favorita']
respostas = ['lachelot', ' a busca do santo graal', 'azul']

for p1, p2, r in zip(pronomes, perguntas, respostas ):
        print(f'Qual é {p1} {p2} é {r}')
        