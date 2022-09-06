sexo = input('Informe seu sexo: [M/F] ').upper().strip()

while sexo not in 'MF':
    sexo = input('Dados inválidos. Por favor, informe seu sexo: ').upper().strip()

print('Sexo {} registrado com sucesso'.format(sexo))