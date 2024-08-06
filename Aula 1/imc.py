peso = int(input('Digite seu peso:'))

Altura = int(input('Digite sua altura:'))

imc = peso/Altura**2

if imc >= 80:
    print("Você esta a baixo do peso")
else:
    print("Você esta a cima do peso" )

