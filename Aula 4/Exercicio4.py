# Desenvolver um programa que armazene pessoas.
# As pessoas devem informar nome, e-mail e idade.
# O programa deve ser o seguinte:

# 1 - Inclusão 
# 2 - Exclusão
# 3 - Exibição de todos os requisetos 
# 4 - Alteração dos dados de um pessoa
# 5 - Sair

inicio = True

while inicio:
    escolha = int(input("""
    1 - Inclusão 
    2 - Exclusão 
    3 - Exibição 
    4 - Alterar                    
    5 - Sair  
                        """))
while True:
    nome = input('digite o nome:')
    idade = int(input('Digite a idade:'))
    email = input('digite seu e-mail:')

