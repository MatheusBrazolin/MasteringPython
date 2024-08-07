numeros = []

for i in range (0,  5, 1):
    x = int(input('Digite um numero: '))
    numeros.append(x)

print('Os numeros que vc digitou foram: ')

for i in range (0, 5, 1 ):
    print(numeros[i])

print('=' * 10)

# Exibir de forma decrescente 
for i in range (4, -1, -1):
    print (numeros[i])

print('=' * 10)

for item in numeros: 
    print(item)

print('=' * 10)