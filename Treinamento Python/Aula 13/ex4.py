from random import randint
print('='*50)
print('JOGO NA MEGA SENA'.center(50))
print('='*50)


n = int(input('Quantos jogos você quer que eu sorteie?'.center(50)))
lista = [[] for i in range(n)]
for i in range(0,n):
    for x in range(0,6):
        lista[i].append(randint(1,60))
print(f'-=-=-=-=-=-=-= SORTEANDO {n} JOGOS -=-=-=-=-=-=-='.center(50))
for i in range(1,n+1):
    print(f'|Jogo {i}: {lista[i-1]}|'.center(50))
print('-=-=-=-=-=-=-= < BOA SORTE! > -=-=-=-=-=-=-=-='.center(50))