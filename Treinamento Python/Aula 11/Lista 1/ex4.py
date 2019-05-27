#lista = [int(x) for x in input('Insira 10 valores.').split()]
lista = []
for i in range(0,10):
    x = int(input('Insira um número: '))
    lista.append(x)

final = sorted(lista)
print(final)