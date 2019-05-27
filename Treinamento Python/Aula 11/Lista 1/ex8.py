def func(x):
    final = []
    for i in range (0, len(x)):
        if lista[i]%2 == 1:
            final.append('False')
        else:
            final.append('True')
    return final

lista = [int(x) for x in input().split()]    

print(func(lista))