print('=' * 20)
print('BANCO CEV')
print('=' * 20)
    
saque = int(input('Que valor você quer sacar? R$ '))
if saque // 50 > 0:
    print('Total de {} cédulas de R$ 50,00'.format(saque // 50))
    saque = saque % 50
if saque // 20 > 0:
    print('Total de {} cédulas de R$ 20,00'.format(saque // 20))
    saque = saque % 20
if saque // 10 > 0:
    print('Total de {} cédulas de R$ 10,00'.format(saque // 10))
    saque = saque % 10
if saque // 1 > 0:
    print('Total de {} cédulas de R$ 1,00'.format(saque // 1))
    saque = saque % 1
print('=' * 20)
print('Volte sempre ao BANCO CEV! Tenha um bom dia')