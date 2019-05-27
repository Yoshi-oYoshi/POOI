a,b,c,d = map(int,input().split())
lista = (a,b,c,d)
pares =[]
if lista.count(9) > 0:
    print(f'Existe uma quantidade de 9 = {lista.count(9)}')
if lista.count(9) == 0:
    print('Não existem numeros nove')
if lista.count(3) > 0:
    print(f'O número 3 está na posição {lista.index(3)}')
for i in range(0, len(lista)):
    if lista[i]%2 == 0:
        pares.append(lista[i])
print(f'Os números pares são {pares}')