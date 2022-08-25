import math

a = int(input("Digite o ângulo que você deseja: "))
r = math.radians(a)

print("O ângulo de {:.1f} tem o SENO de {:.2f}".format(a, math.sin(r)))
print("O ângulo de {:.1f} tem o COSSSENO de {:.2f}".format(a, math.cos(r)))
print("O ângulo de {:.1f} tem a TANGENTE de {:.2f}".format(a, math.tan(r)))