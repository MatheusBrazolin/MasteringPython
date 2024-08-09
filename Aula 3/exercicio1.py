# Armazenar des numeros em uma lista
# Depois exibir os valores na ordem inversa da digitação

numeros = []

for i in range (1,  11, 1):
    n = int(input(f'Digite o {i}: '))
    numeros.append(n)

numeros.reverse()

print(numeros)

numeros_slices = numeros[: : -1]
print(numeros_slices)