n = input('Insira algo ')
if type(n) is str:
	print('Isso é um char')
else:
	if type(n) is int:
		print('Isso é um inteiro')
	else:
		if type(n) is float:
			print('Isso é um float')
		else:
			if type(n) is bool:
				print('Isso é um bool')
							