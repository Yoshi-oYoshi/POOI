def func(i):
    if i < 0:
        return 1
    else:
        return 0    

lista = list(map(int,input('Insira uma lista de números inteiros:\n').split()))
sum = 0

for i in range(0, len(lista)):
    sum += func(lista[i])

print(f'Existem {sum} números negativos essa lista.')