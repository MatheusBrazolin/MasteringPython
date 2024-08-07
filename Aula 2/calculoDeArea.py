#Calcular e exibir a media aritimedica de quatro valores que serão digitado!2

a = float(input("Digite o primeiro valor:"))
b = float(input("Digite o segundo valor:"))
c = float(input("Digite o terceiro valor:"))
d = float(input("Digite o quarto valor:"))

ma = (a+b+c+d) / 4

#imprimir o resultado com 2 casa decimais 

print(f'A media aritimédica é: {ma: .2f}')  #.2f limita os 0 apos a , "(1.00)""