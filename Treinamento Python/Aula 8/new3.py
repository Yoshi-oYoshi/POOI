peso = float(input('Insira seu peso em Kg: '))
altura = float(input('Insira sua altura em Metros: '))

IMC = peso/(altura**2)

if IMC < 18.5:
	print('De acordo com seu IMC você está abaixo do peso')
elif IMC <= 25:
	print('De acordo com seu IMC você está no peso ideal')
elif IMC <= 30:
	print('De acordo com seu IMC você está no sobrepeso')
elif IMC <= 40:
	print('De acordo com seu IMC você está na obesidade')
else:
	print('De acordo com seu IMC você está em obesidade mórbida')