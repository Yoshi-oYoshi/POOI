
valor = float(input('Insira o valor da casa: '))
salario = float(input('Insira o seu sálario: '))
anos = float(input('Insira quantos anos você pretende pagar a casa: '))

if (valor/(anos * 12) > (salario * 0.3)):
	print('Empréstimo negado')
else:
	print('Empréstimo aprovado')