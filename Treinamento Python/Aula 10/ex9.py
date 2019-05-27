nota = int(input('Insira uma nota de 0 a 10: '))
while nota > 10 or nota < 0:
    nota = int(input('Valor inválido insira um novo: '))
print('Valor válido :D')