lista = list(map(int,input('Insira uma lista de números inteiros.\n').split()))
final = []

for i in range (0, len(lista)):
    if lista[i]%2 == 1:
        final.append('False')
    else:
        final.append('True')
if len(final) == 0:
    print('Sua lista não possui nenhum elemento!')
else:    
    print(f'De acordo com a ordem da sua lista os elementos correspondentes ao mesmo index com true são pares:\n{final}')