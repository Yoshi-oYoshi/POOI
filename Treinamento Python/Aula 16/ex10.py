lista = []
n = int(input('Insira um número aleatório: '))
if n < 0:
    exit
lista.append(n)
print(lista)
while n >= 0:
    n = int(input('Insira um número aleatório: '))
    if n > lista[0]:
        lista.insert(0,n)
    print(lista)