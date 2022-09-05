print('=' * 10, 'LOJAS GUANABARA', '=' * 10)

compras = float(input('Preço das compras: R$ '))

print('FORMAS DE PAGAMENTO')
print('[1] à vista dinheiro/cheque')
print('[2] à vista cartao')
print('[3] 2x no cartao')
print('[4] 3x ou mais no cartao')

pagamento = 0
while pagamento < 1 or pagamento > 4:
    pagamento = int(input('Digite sua opcao: ')) 

if pagamento == 4:
    x = int(input('Quantas parcelas?'))
    print('Sua compra sera parcelada em {}x de R$ {:.2f} COM juros.'.format(x, compras * 1.2 / x))
    print('Sua compra de R$ {:.2f} vai custar R$ {:.2f} no final.'.format(compras, compras * 1.2))
elif pagamento ==3:
    print('Sua compra sera parcelada em 2x de R$ {:.2f} sem juros.'.format(compras / 2))
elif pagamento == 2:
    print('Sua compra sera paga a vista, no valor de R$ {} com desconto de 5%'.format(compras * 0.95))
elif pagamento == 1:
    print('Sua compra sera paga a vista, no valor de R$ {} com desconto de 10%'.format(compras * 0.9))