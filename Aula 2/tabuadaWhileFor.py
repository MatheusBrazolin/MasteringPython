print ('tabuada com WHILE/FOR')

num = int(input('digite um numero para obter a tabuada: '))

while num <= 0: 
    print ('não pode numero negativo! ')
    num = int(input('digite um numero para obter a tabuada: '))

for i in range (1, 11, 1):
    resultado = num * i 
    print (f'{num} x {i} = {resultado}')  