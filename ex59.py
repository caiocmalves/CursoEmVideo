from time import sleep

n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
print("""      [1] somar
      [2] multiplicar
      [3] maior
      [4] novos números
      [5] sair do programa""")
opcao = int(input('Qual é a sua opção? '))
while opcao < 1 or opcao > 5:
    opcao = int(input('Opção inválida. Tente novamente:  '))

while opcao != 5:
    match opcao:
        case 1:
            print('A soma entre {} e {} é {}'.format(n1, n2, n1+n2))
        case 2:
            print('A multiplicação entre {} e {} é {}'.format(n1, n2, n1*n2))
        case 3:
            if n1 > n2:
                print('O maior valor entre {} e {} é {}'.format(n1, n2, n1))
            elif n2 > n1:
                print('O maior valor entre {} e {} é {}'.format(n1, n2, n2))
        case 4:
            n1 = int(input('Primeiro valor: '))
            n2 = int(input('Segundo valor: '))
    print('=-=' * 10)
    sleep(2)
    print("""        [1] somar
        [2] multiplicar
        [3] maior
        [4] novos números
        [5] sair do programa""")   
    opcao = int(input('Qual é a sua opção? '))
    while opcao < 1 or opcao > 5:
        print('Opção inválida. Tente novamente:  ')
        print('=-=' * 10)
        sleep(2)
        print("""        [1] somar
        [2] multiplicar
        [3] maior
        [4] novos números
        [5] sair do programa""")
        opcao = int(input('Qual é a sua opção? '))
print('finalizando...')
sleep(1)
print('=-=' * 10)        
print('Fim do programa! Volte sempre!')
