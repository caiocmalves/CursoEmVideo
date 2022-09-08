print('-' * 20)
print('LOJA SUPER BARATAO')
print('-' * 20)

produtoMaisBarato = ''
valorProdutoBarato = 0
totalCompra = 0
maisDeMil = 0
while True:
    produto = input('Nome do produto: ').strip()
    preco = float(input('Preço: R$ '))
    continuar = input('Quer continuar? [S/N] ').strip().upper()
    totalCompra += preco
    if preco > 1000:
        maisDeMil += 1
    if valorProdutoBarato == 0:
        valorProdutoBarato = preco
        produtoMaisBarato = produto
    elif valorProdutoBarato != 0 and preco < valorProdutoBarato:
        valorProdutoBarato = preco
        produtoMaisBarato = produto
    if continuar == 'N':
        break

print('-' * 7, 'FIM DO PROGRAMA', '-' * 7)
print()
print('O total da compra foi R$ {:.2f}'.format(totalCompra))
print('Temos {} produtos custando mais de R$ 1000,00'.format(maisDeMil))
print('O produto mais barato foi {} que custa R$ {:.2f}'.format(produtoMaisBarato, valorProdutoBarato))