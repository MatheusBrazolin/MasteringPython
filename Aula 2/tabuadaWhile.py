print ('tabuada com WHILE')

num = int(input('digite um numero para obter a tabuada: '))

while num <= 0: 
    print ('não pode numero negativo! ')
    num = int(input('digite um numero para obter a tabuada: '))

i = 1 
while i<11 :
    resultado = num * i
    print (f'{num} x {i} = {resultado}')  
    i += 1  # o mesmo que i = i + 1 


# While: Uma forma de iteração em Python é a instrução while, que permite repetir a execução de um bloco de código, sempre que a condição do loop seja verdadeira. O código no corpo do loop deve alterar uma ou mais variáveis até que a condição resulte falsa e o loop termine.