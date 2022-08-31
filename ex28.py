import random
from time import sleep

print("-=-" * 20)
print("Vou pensar em um número entre 0 e 5. Tente adivinhar...")
print("-=-" * 20)

secreto = random.randint(0,5)

adivinha = int(input("Em que número eu pensei? "))

print("Processando...")
sleep(1)

while secreto != adivinha:
    adivinha = int(input("Não foi dessa vez! Tente mais uma vez: "))
    secreto = random.randint(0,5)
    print("Processando...")
    sleep(1)
else:
    print("PARABÉNS! Você me ganhou.")




