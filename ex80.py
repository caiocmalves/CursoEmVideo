valores = []

for i in range(5):
    valor = int(input('Digite um valor: '))
    valores.append(valor)
    valores.sort()
    if valor == valores[-1]:
        print('Adicionado ao final da lista...')
    else:
        print('Adicionado na posição {} da lista...'.format(valores.index(valor)))

print(valores)