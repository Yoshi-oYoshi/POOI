la = []
lb = [] 
lista = []

for i in range(3):
    la.append(int(input('Primeira tupla:')))
for i in range(3):
    lb.append(int(input('Segunda tupla: ')))

for i in range(3):
    lista.append(tuple(la)[i])
    lista.append(tuple(lb)[i])

print(tuple(lista))
