palavra = input("Digite uma palavra")

vogais = ("a,e,i,o,u")
for item in palavra:
    if item in vogais:
        print("quantidade de vogais")