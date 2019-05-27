lista = [int(x) for x in input().split()]
aux = 0
index = 0
for i in range(0, len(lista)):
    if lista[i] > aux:
        r = lista[i]
        index = lista.index(r) + 1
    aux = lista[i]
print(f'O maior número está na posição {index}')