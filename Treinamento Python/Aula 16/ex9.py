la = []
lb = [] 
lista = []
for i in range(3):
    la.append(int(input('Primeira lista: ')))
for i in range(3):
    lb.append(int(input('Segunda lista: ')))

for i in range(3):
    lista.append(la[i]+lb[i])
    

print(lista)
