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
print(cadastro)