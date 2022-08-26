nome = input("Qual é seu nome completo? ").strip().lower()

nomeCompleto = nome.split(" ")
silva = False

for i in range(0, len(nomeCompleto)):
    if(nomeCompleto[i] == "silva"):
        silva = True
        
print("Seu nome tem Silva?", silva)

#outra forma é usar o in
#print("Seu nome tem Silva? {}".format('silva' in nome)