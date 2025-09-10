valor = int(input("Digite o valor da compra: R$"))


if valor > 100:
    valorcompra =valor- ( valor * 0.10)
    print(valorcompra) 
    
else:
    print("Valor da compra: R$ {valor:.2f}")
