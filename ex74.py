import random

n = []
x = ()

for i in range(0, 5):
    n.append(random.randint(0,10))

x = tuple(n)

print('Os valores sorteados são: {}'.format(x))
print('O maior valor sorteado foi {}'.format(sorted(x, reverse=True)[0]))
print('O menor valor sorteado foi {}'.format(sorted(x)[0]))