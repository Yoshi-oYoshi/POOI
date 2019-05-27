def func(x):
    aux = 0
    index = 0  
    for i in range(0, len(x)):
        if lista[i] > aux:
            r = lista[i]
            index = lista.index(r) + 1
        aux = lista[i]
    return index

lista = [int(x) for x in input().split()]    

print(f'O maior número está na posição {func(lista)}')