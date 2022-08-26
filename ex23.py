from time import sleep


n = int(input("Informe um número: "))

print("Analisando o numero {}".format(n))
sleep(1)

milhar = n // 1000
centena = (n % 1000) / 100
dezena = ((n % 1000) % 100) / 10
unidade = ((n % 1000) % 100) % 10

print("Unidade: {}".format(int(unidade)))
print("Dezena: {}".format(int(dezena)))
print("Centena: {}".format(int(centena)))
print("Milhar: {}".format(int(milhar)))

#Outra forma é transformando o numero em string e utilizar o parâmetro para diferenciar.
#num = str(n)
#.format(n[0]) para milhar
#.format(n[1]) para centena
#...