from time import sleep


nome = input("Digite seu nome completo: ")
print("Analisando seu nome...")

sleep(1)

print("Seu nome em maiúsculas é {}".format(nome.upper()))
print("Seu nome em minúsculas é {}".format(nome.lower()))
print("Seu nome tem ao todo {} letras".format(len(nome)))
print("Seu primeiro nome é {} e ele tem {} letras".format(nome.split(" ")[0], len(nome.split(" ")[0])))