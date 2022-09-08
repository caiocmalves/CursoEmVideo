from time import sleep
while True:
    n = int(input('Quer ver a tabuada de qual valor? '))
    if n < 0:
        break
    sleep(1)
    print('-' * 20)
    for i in range(1, 11):
        print('{} * {} = {}'.format(n, i, n * i))
    print('-' * 20)
print('-' * 20)
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')