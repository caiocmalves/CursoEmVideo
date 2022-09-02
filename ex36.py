valorCasa = int(input('Valor da casa: R$ '))
salario = int(input('Salário do comprador: R$ '))
anos = int(input('Quantos anos de financiamento? '))

prestacao = valorCasa / (anos * 12)

if prestacao > salario * 0.3:
    print('Seu empréstimo foi negado')
else:
    print('Parabéns, você vai pagar R$ {:.2f} por {} anos em prestações mensais de R$ {:.2f}'.format(valorCasa, anos, prestacao))