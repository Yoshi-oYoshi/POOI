enter = (input('INsira o que deseja fazer: '), int(input('Insira o primeiro número: ')), int(input('Insira o segundo número: ')))
aws = 0
if enter[0] == 'SOMA':
    aws = enter[1] + enter[2]
    print(aws)
elif enter[0] == 'SUB':
    aws = enter[1] - enter[2]
    print(aws)
elif enter[0] == 'DIV':
    aws = enter[1] // enter[2]
    print(aws)
elif enter[0] == 'MULT':
    aws = enter[1] * enter[2]
    print(aws)
else:
    print('NONE')
