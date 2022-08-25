dias = int(input("Quantos dias o carro foi alugado? "))
km = int(input("Quantos Km rodados? "))

diaria = 60
kmRodado = 0.15

total = (diaria * dias) + (kmRodado * km)


print("O total a pagar é de R$ {:.2f}".format(total))