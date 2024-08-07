#correção ex aula 1
peso = int(input('Digite seu peso:'))

Altura = int(input('Digite sua altura:'))

imc = peso/(Altura * Altura)

if imc >= 20:
    print("Você esta a baixo do peso")
elif imc < 25:
    print("Peso ideal" )
else:
    print ("Acima do peso")
