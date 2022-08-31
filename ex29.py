velo = int(input("Qual é a velocidade atual do carro? "))

valor = 0
if velo > 80:
    valor = 7 * (velo - 80)
    print("MULTADO! Você excedeu o limite permitido que é de 80Km/h")
    print("Você deve pagar uma multa de R$ {:.2f}".format(valor))
print("Tenha um bom dia! Dirija com segurança!")
