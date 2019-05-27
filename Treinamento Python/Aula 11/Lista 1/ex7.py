def func(i, y):
    return i.count(y)

lista = [int(x) for x in input().split()]    
numero = int(input())

print(func(lista,numero))