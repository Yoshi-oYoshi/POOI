#x = [[i for i in range(1,5)] for j in range(5)]
#print(x[1][3])
matriz = [[i for i in range(0, 3)]for j in range(3)]
print(matriz)
for linha in range(0,3):
    for coluna in range(0,3):
        matriz[linha][coluna] = int(input(f'Digite o valor para [{linha}, {coluna}] :'))
for linha in range(0,3):
    for coluna in range(0,3):
        print(f'[{matriz[linha][coluna]}]', end='')
    print()