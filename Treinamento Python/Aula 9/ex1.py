print('Diga qual é o seu sexo.\nM- Masculino\nF- Feminino')
choice = input()
while choice != 'F' and choice != 'M':
    choice = input('Por favor faça uma seleção correta, tente novamente: ')
print('Você selecionou',choice)