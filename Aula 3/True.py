niveis= {'junior', 'pleno' , 'senior'} 

print('Cadastro niveis')

while True:
    n = input('Digite seu nivel proficional: ')
    niveis.add(n)

    print (niveis)

    continuar = input ('Deseja continuar?')
    if not continuar:
        break 

    print('end')
    print (niveis)