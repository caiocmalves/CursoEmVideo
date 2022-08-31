ano = int(input("Digite o ano que deseja verificar se é bissexto (0 para o atual): "))

if ano == 0:
    ano = 2022
    if ano % 4 == 0 and ano % 100 != 0:
        print("{} é bissexto.".format(ano))    
    elif ano % 400 == 0:
        print("{} é bissexto.".format(ano))
    else:
        print("{} NÃO é bissexto.".format(ano))
elif ano % 4 == 0 and ano % 100 != 0:
    print("{} é bissexto.".format(ano))
elif ano % 400 == 0:
    print("{} é bissexto.".format(ano))
else:
    print("{} NÃO é bissexto.".format(ano))
    

    