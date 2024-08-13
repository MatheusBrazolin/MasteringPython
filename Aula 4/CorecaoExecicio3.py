# Desenvolver um programa que armazene pessoas. 
# As pessoas devem informar nome, e-mail e idade. 
# O programa deve ser o seguinte menu: 

# 1 - Inclusão 
# 2 - Exclusão 
# 3 - Exibição 
# 4 - Sair

nomes = ["joao", "matheus"]
inicio = True

while inicio:
    escolha = int(input("""
    1 - Inclusão 
    2 - Exclusão 
    3 - Exibição 
    4 - Sair  
                        """))
    match escolha:
        case 1: 
            n= input("digite o nome para adicionar:")
            nomes.append(n)
            print(f'{n} inserido!')

        case 2: 
            n= input("digite oque deseja excluir:")
            nomes.remove(n)
            print(f'{n} Excluido!')

        case 3: 
            for n in nomes:
                print(n)

        case 4:
            break

        case _:
            print("Escolha outra opção:")