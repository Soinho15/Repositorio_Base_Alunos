valor_compra = float(input("Digite o valor da compra "))

if valor_compra >= 1000:
    print('desconto = 15',valor_compra*0.15)
elif valor_compra >= 500:
    print('desconto = 0.10')
elif valor_compra >= 100:
    print('desconto = 0.05')
else: 
    print('desconto = 0.0')