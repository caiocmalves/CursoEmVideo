metros = float(input("Digite o valor em metros: "))

cm = metros * 100
mm = metros * 1000


print("{:.2f} metros, equivalem a {:.2f} centimentos e {:.2f} milimetros".format(metros, cm, mm))