from random import randint
maior = 0
indexo = [[]]
matriz =[[i for i in range(4)]for j in range(4)]
for linha in range(4):
    for coluna in range(4):
        matriz[linha][coluna] = int(input(f'Digite o número da posição {linha},{coluna}: '))
        if matriz[linha][coluna] > maior:
            maior = matriz[linha][coluna]
            linha_index = linha
            coluna_index = coluna
print(f'{linha_index}, {coluna_index}')