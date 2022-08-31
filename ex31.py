dist = float(input("Qual é a distância da sua viagem em Km? "))
print("Você está prestes a começar uma viagem de {:.1f} Km.".format(dist))

preco = 0
if dist < 200:
    preco = dist * 0.5
else:
    preco = dist * 0.45
    
print("E o preço da sua passagem será de R$ {:.2f}".format(preco))