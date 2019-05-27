total = []
while True:
    aux = 0
    lista = []
    cadastro = {}
    cadastro["Nome"] = str(input('Insira seu nome: '))
    cadastro["Jogos"] = int(input('Insira quantos jogos você jogou: '))
    for i in range(cadastro["Jogos"]):
        lista.append(int(input(f'Quantos gols você fez na {i+1} partida: ')))
    cadastro["Gols"] = lista
    for i in range(len(lista)):
        aux += lista[i]
    cadastro["Soma de gols"] = aux
    total.append(cadastro.copy())
    controle = int(input("Deseja cadastrar mais alguém? 1-sim 2-não\n"))
    while controle != 1 or controle != 2:
        controle = int(input("COloque uma seleção válida!!!\n"))
    if controle == 2:
        break
while True:
    print('Deseja ver o resultado de algum cadastrado?')
    for i in range(len(total)):
        print(f'{i+1} - {total[i]["Nome"]}')
    escolha = int(input('Digite 0 para fechar o programa.\n'))
    while escolha > len(total):
        escolha = int(input('Coloque um número válido!!!\n'))
    if escolha == 0:
        break
    elif escolha <= len(total):
        print(total[escolha-1])
     