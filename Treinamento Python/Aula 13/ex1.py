final = []
nomes = []
pesos = []
nomes_mais_pesado = []
nomes_mais_leves = []
sum = 0
p_maior = 0
p_menor = 100000
while True:
    
    nomes = [x for x in input('Insira o(s) nome(s): ').split()]
    for i in range(0, len(nomes)):
        sum += 1
    pesos = int(input('Insira o peso: '))
    
    if pesos >= p_maior:
        p_maior = pesos
        nomes_mais_pesado = nomes.copy()
    
    elif pesos <= p_menor:
        p_menor = pesos
        nomes_mais_leves = nomes.copy()
    
    nomes.append(pesos)
    final.append(nomes)

    controle = input('Deseja continuar?\nY/n\n')
    while controle != 'y' and controle != 'n' and controle != 'Y' and controle != 'N':
        controle = input('Por favor coloque um input aceitável!\n')
    if controle == 'n' or controle == 'N':
        break
print(f'A quantidade de pessoas cadastradas foram: {sum}\nAs que possuem o maior peso são: {nomes_mais_pesado}\nAs que são mais leves são: {nomes_mais_leves}\nThanks for Playing!!')
print(pesos)