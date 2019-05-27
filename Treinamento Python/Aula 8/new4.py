n1 = int(input('Insira sua primeira nota: '))
n2 = int(input('Insira sua segunda nota: '))
n3 = int(input('Insira sua terceira nota: '))

media = (n1+n2+n3)/3
if media < 5:
	print('Você está reprovado')
elif media < 7:
	print('Você está de recuperação')
else:
	print('Você está aprovado')