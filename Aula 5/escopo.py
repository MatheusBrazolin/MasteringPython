escopo_global = 10 

def minha_funcao():
    escopo_local = 5.4
    print(f'minha_fucao> {escopo_global}')
    print(f'minha_fucao> {escopo_local}')
    return escopo_local

def minha_funcao2():
    escopo_local = 34.5
    escopo_global = 20
    print(f'minha_fucao> {escopo_global}')
    print(f'minha_fucao> {escopo_local}')
    return escopo_local

print(minha_funcao())
print(minha_funcao2())

print (f'principal>{escopo_global}')


    