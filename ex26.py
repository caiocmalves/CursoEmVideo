nome = input("Digite uma frase: ").strip().lower()

print("A letra A aparece {} vezes na frase.".format(nome.count("a")))
print("A primeira letra A apareceu na posição {}".format(nome.find("a") + 1))
print("A última letra A apareceu na posição {}".format(nome.rfind("a") + 1))