lista = [[],[]]


for i in range (1,8):
    x = int(input(f'Digite o {i}o. valor: '))
    if x%2 == 1:
        lista[1].append(x)
    else:
        lista[0].append(x)
print(f'Números pares: {lista[0]}\nNúmeros ímpares: {lista[1]}')
for i in range(2):
    if i == 1:
        print(' ')
    for x in range(len(lista[i])):
        print(lista[i][x], end=' ')
print('')