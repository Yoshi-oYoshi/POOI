#nome = input('Insira seu nome:\n')
nome = 'Leonardo Kazuyoshi Takahashi da Silva'
print(nome.upper())
print(nome.lower())
print('Seu nome possui:', len(nome) - nome.count(' '), 'letras')
print('Seu primeiro nome possui:', len(nome.split()[0]), 'letras')