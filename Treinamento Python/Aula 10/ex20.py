n = int(input('Insira quantas pessoas existem no grupo: '))
sum = 0
for x in range(0,n):
    age = int(input('Insira a idade de uma pessoa do grupo: '))
    while age < 0:
        age = int(input('Insira uma idade válida!\n'))
    sum += age
if sum/n < 26:
    print('Essa turma está jovem, com uma média de', sum/n, 'anos')
elif sum/n < 61:
    print('Essa turma está adulta, com uma média de', sum/n,'anos')
else:
    print('Essa turma está idosa, com uma média de', sum/n, 'anos')