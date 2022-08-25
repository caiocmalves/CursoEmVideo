import math

catOp = float(input("Comprimento do cateto oposto: "))
catAdj = float(input("COmprimento do cateto adjacente: "))

hip = math.hypot(catOp, catAdj)

print("A hipotenusa vai medir {:.2f}".format(hip))