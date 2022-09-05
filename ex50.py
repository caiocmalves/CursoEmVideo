x = []
soma = 0
for i in range(0, 6):
    x.append(int(input('Digite um valor inteiro: ')))
    if x[i] % 2 == 0:
        soma += x[i]
print (soma)
