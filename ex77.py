vogais = ('A', 'E', 'I', 'O', 'U')

palavras = ['APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON', 'CURSO', 'GRATIS', 'ESTUDAR', 'PRATICAR', 'TRABALHAR', 'MERCADO', 'PROGRAMADOR', 'FUTURO']

letras = ''
for i in range(0, len(palavras)):
    letras = ''
    for j in palavras[i]:
        if j in vogais:
            letras += j + ' '
    print('Na palavra {} temos {}'.format(palavras[i], letras.lower()))        
