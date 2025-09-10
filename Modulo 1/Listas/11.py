numeros = [10,20,30,40,50]
 #1. Adicione 60 no final 
numeros.append(60)

 #2. insira 15 na posiçao 1
numeros.insert(1, 15)

 #3. remova o elemento 30
numeros.remove(30)

 #4. remova o ultimo elemento e guarde-o em uma variavel
ultimo = numeros.pop()

print("lista final:", numeros)
print("Ultimo elemento removido:", ultimo)