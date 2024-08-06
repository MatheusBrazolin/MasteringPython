#Calculo de Media
n1 = int(input ('digite a primeira nota:'))

n2 = int(input ('digite a segunda nota:'))

media = ( n1+n2)/2

if media >= 5:
    print(f"Parabens, você foi aprovado com a nota: {media}")
else:
    print(f"Você foi reprovado pela media: {media}")
    