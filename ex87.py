matriz = [[], [], []]

pares = 0
terceira = 0
maiorSec = 0
for i in range(0,3):
    for j in range(0, 3):
        matriz[i].append(int(input(f'Digite um valor para [{i}, {j}]: ')))
        if matriz[i][j] % 2 == 0:
            pares += matriz[i][j]
        if j == 2:
            terceira += matriz[i][j]
        if i == 1 and matriz[i][j] > maiorSec:
            maiorSec = matriz[i][j]
    
print('=-' * 20)
for i in range(0, len(matriz)):
    for j in range(0, 3):
        print(f'[ {matriz[i][j]} ]', end= ' ')
    print()
print('=-' * 20)

print(f'A soma dos valores pares é {pares}')
print(f'A soma dos valores da terceira coluna é {terceira}')
print(f'O maior valor da segunda linha é {maiorSec}')