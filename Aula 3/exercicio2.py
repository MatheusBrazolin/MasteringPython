# Entrar com dois valores via teclado onde o segundo devera ser maior que o primeiro
# Caso contrario solicitar novamemente apenas o segundo valor 

a = int(input('digite o primeiro valor: '))
b = int(input('digite o segundo valor: '))

while (b <= a):
    int(input('o segundo valor deve ser maior que o primeiro '))
    b = int(input('Digite o segndo valor: '))
    int(input(f'o primeiro valor foi {a} e o segundo valor foi {b}'))
