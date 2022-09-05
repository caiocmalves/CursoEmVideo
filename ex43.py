import math

peso = float(input('Qual é o seu peso ? (Kg) '))
altura = float(input('Qual é sua altura? (M) '))

imc = peso / math.pow(altura, 2)

if imc < 18.5:
    print('Seu IMC é {:.1f}, portanto, você está abaixo o seu peso ideal.'.format(imc))
elif imc >= 18.5 and imc < 25:
    print('Seu IMC é {:.1f}, portanto, você está no seu peso ideal.'.format(imc))
elif imc >= 25 and imc < 30:
    print('Seu IMC é {:.1f}, portanto, você está com sobrepeso.'.format(imc))
elif imc >= 30 and imc < 40:
    print('Seu IMC é {:.1f}, portanto, você está obeso.'.format(imc))
elif imc >= 40:
    print('Seu IMC é {:.1f}, portanto, você está com obesidade mórbida.'.format(imc))
