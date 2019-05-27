nome = input('Insira o seu nome (maior que 3 caractéres):\n')
while len(nome) < 4:
    nome = input('Insira um nome válido!\n')

age = int(input('Insira sua idade:\n'))
while age > 150 or age < 0:
    age = int(input('Insira uma idade válida!\n'))

salario = float(input('Insira seu salário:\n'))
while salario < 0.0:
    salario = float(input('Insira um salário válido!\n'))

sexo = input('Insira seu sexo. F ou M:\n')
while sexo != 'F' and sexo != 'M':
    sexo = input('Insira um sexo válido!\n')

ec = input('Insira seu estado civil. S/C/V/D:\n')
while ec != 'S' and ec != 'C' and ec != 'V' and ec != 'D':
    ec = input('Insira um estado civil válido!\n')