cadastro = {}
cadastro["Nome"] = str(input('Insira seu nome: '))
cadastro["iD carteira"] = int(input('Insira o número da sua carteira de trabalho: '))
cadastro["Idade"] = int(input('Insira sua idade: '))
if cadastro["iD carteira"] > 0:
    cadastro["Contratação"] = int(input('Colquer o ano que você foi contratado: '))
    cadastro["Sálario"] = float(input('Insira seu salário: R$'))
    cadastro["Aposentadoria"] = cadastro["Contratação"]+35
    cadastro["idade na aposentadoria"] = (cadastro["Idade"] +(cadastro["Aposentadoria"] - 2019))
else:
    print(cadastro)
    exit
print(cadastro)