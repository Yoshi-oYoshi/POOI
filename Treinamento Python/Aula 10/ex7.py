salario = float(input('Dgite o seu sálario: '))
if salario < 400.01:
    novo_s = salario*1.15
elif salario < 800.01:
    novo_s = salario*1.12
elif salario < 1200.01:
    novo_s = salario*1.1
elif salario <= 2000.00:
    novo_s = salario*1.07
else:
    novo_s = salario*1.04
print('Seu novo salário é R${:.2f}'.format(novo_s))