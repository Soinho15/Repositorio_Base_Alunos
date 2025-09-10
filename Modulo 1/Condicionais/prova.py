nome = input('digite seu nome')

#input é usado para receber algum dado.

peso = int(input('digite o seu peso'))

# int é usado para receber valores inteiros.

altura = float(input('digite a sua altura'))

#float é usado para receber numeros com casas decimais.

imc = peso/(altura*altura)

#print é usado para fornecer algum dado no terminal.


if imc>30:
    print('obeso tipo 1')


elif imc>25:
    print('a cima do peso')


elif imc>16:
    print('abaixo do peso')


else:
    print('peso ideal')


#if, elif e else, é a criação de uma condição.