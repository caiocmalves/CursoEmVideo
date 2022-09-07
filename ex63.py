print('-' * 20)
print('Sequêbcia de Fibonacci')
print('-' * 20)
termos = int(input('Quantos termos você quer mostrar? '))
fibo = [0, 1, 1]
for i in range(3,termos):
    fibo.append(fibo[i - 1] + fibo[i - 2]) 

for i in fibo:
    print(i, end=' -> ')
print('FIM')