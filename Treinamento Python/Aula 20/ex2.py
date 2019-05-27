import random
final = []
jogadores = {}
lista = []
end = {}
end_lista = []
for i in range(4):
    jogadores["nome"] = str(input('Insira seu nome:\n'))
    jogadores["ponto"] = random.randint(1,6)
    final.append(jogadores.copy())
print(final)
for i in range(4):
    lista.append(final[i]["ponto"])

lista.sort(reverse=True)
print(lista)
for x in range(4):
    for i in range(4):
        if final[i]["ponto"] == lista[x]:
            end["nome"] = final[i]["nome"]
            end["ponto"] = final[i]["ponto"]
            final[i]["ponto"] = 7
            end_lista.append(end.copy())
            break
print(end_lista)