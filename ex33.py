n1 = int(input("Primeiro valor:"))
n2 = int(input("Segundo valor:"))
n3 = int(input("Terceiro valor:"))

lista = [n1, n2, n3]
menor = n1
maior = n1

for i in range(1, len(lista)):
    if menor > lista[i]:
        menor = lista[i]

for i in range(1,len(lista)):
    if maior < lista[i]:
        maior = lista[i]

print('O menor valor digitado foi:', menor)
print('O maior valor digitado foi:', maior)

