from random import randrange
num = randrange(11)
test = int(input('Digite um número: '))
tentativas = 1
while test != num:
    test = int(input('Você errou tente novamente: '))
    tentativas += 1
print(f'GAME OVER\n Você acertou o número era {num}\n Isso em {tentativas} tentativas.')