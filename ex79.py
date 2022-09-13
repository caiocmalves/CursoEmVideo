ns = []
ns.append(int(input('Digite um valor: ')))
continuar = input('Quer continuar? [S/N] ').lower().strip()

while continuar != 'n':
    n = int(input('Digite um valor: '))
    for i in range(0, len(ns)):
        if n == ns[i]:
            print('Valor duplicado! Não vou adicionar...')     
    for i in range(0, len(ns)):
        if n not in ns:
            ns.append(n)
            print('Valor adicionado com sucesso...')    
    continuar = input('Quer continuar? [S/N] ').lower().strip()
    
print(ns)