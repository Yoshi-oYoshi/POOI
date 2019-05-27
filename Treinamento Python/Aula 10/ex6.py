x = float(input('Insira a média do aluno: '))
if x >= 8:
    conceito = 'A'
elif x >= 7:
    conceito = 'B'
elif x >= 6:
    conceito = 'C'
elif x >= 5:
    conceito = 'D'
else:
    conceito = 'E'
print('O conceito do aluno é',conceito)