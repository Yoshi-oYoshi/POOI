matriz = [[i for i in range(3)]for j in range(3)]
for linha in range(0,3):
    for coluna in range(0,3):
        matriz[linha][coluna] = int(input(f'Insira o valor para a posição {linha},{coluna}:\n'))
for linha in range(0,3):
    print('_' * 20)
    for coluna in range(0,3):
        print(f'|{matriz[linha][coluna]:^5}|',end = '')
    print()