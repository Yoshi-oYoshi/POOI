media_alta = 0
sum = 0.0
z = int(input('Insira a quantidade de notas: '))
for x in range(0,5):
    nome = input('Insira o nome do aluno: ')
    for y in range(0,z):
        nota = float(input('Insira sua nota: '))
        sum = nota+sum
    media = sum/z
    if media > media_alta:
        nome_alto = nome
        media_alta = media
if media_alta < 2.75:
    print(f'{nome} você está reprovado.')
elif media_alta < 5.75:
    print(f'{nome} você tem direito a uma prova de recuperação.')
else:
    print(f'{nome} você está aprovado.')
    