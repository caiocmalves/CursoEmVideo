matriz = [[], [], []]

for i in range(0, 3):
    for j in range(0, 3):
        matriz[i].append(int(input(f'Digite um valor para [{i}, {j}]: ')))
        
for i in range(0, 3):
    print(matriz[i])