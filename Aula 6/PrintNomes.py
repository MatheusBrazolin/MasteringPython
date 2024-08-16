class Pessoa: 
    def __init__(self, n, sn , fone='') -> None:
        self.nome = n
        self.sobrenome = sn
        self.telefone = fone

p1 = Pessoa('Matheus', "Brazolin", 11989656078)
p2 = Pessoa('Adriano', "Carpinelli")

print(type(p1))
print(id(p1))    
        
print(p1.nome)
print(p1.sobrenome)
print(p1.telefone)

print(p2.nome)
print(p2.sobrenome)
print(p2.telefone)
        