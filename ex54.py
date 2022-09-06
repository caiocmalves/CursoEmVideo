anos = []

for i in range(0,7):
    anos.append(int(input('Em que ano a {}ª pessoa nasceu? '.format(i + 1))))

maior = 0
menor = 0
for i in anos:
    if i < 2004:
        maior += 1
    else:
        menor += 1

print('Ao todo tivemos {} pessoas maiores de idade'.format(maior))
print('Ao todo tivemos {} pessoas menores de idade'.format(menor))