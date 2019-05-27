n = int(input('Insira um número: '))
lista = [int(x) for x in range(n+1) if x%2 == 0]
print(lista)