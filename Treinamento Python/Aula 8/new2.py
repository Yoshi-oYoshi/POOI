valor = float(input('Ponha o valor do produto R$'))
tipo = int(input('Selecione o meio de pagamento: 1  A vista, 2- 1x no cartão, 3- 2x no cartão ou 4- 3x mais no cartâo. '))

if tipo == 1:
	pagamento = valor * 0.9
	print('Você ira pagar R${:.2f}'.format(pagamento))
elif tipo == 2:
	pagamento = valor * 0.95
	print('Você ira pagar R${:.2f}'.format(pagamento))
elif tipo == 3:
	pagamento = valor
	print('Você ira pagar R${:.2f}'.format(pagamento))
else:
	pagamento = valor * 1.2
	print('Você ira pagar R${:.2f}'.format(pagamento))