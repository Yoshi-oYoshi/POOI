
geral = {}
cadastro,idades,mulheres = [],[],[]
c,media_idade,aux=0,0,0
while True:
    c+=1 
    geral["nome"] = str(input('Insira seu nome:\n'))
    geral["sexo"] = str(input('Insira seu sexo:(masculino ou feminino) \n'))
    
    while geral["sexo"] != "masculino" and geral["sexo"] != "feminino":
        geral["sexo"] = str(input('Insira um sexo válido?\n'))
    
    geral["idade"] = int(input('Insira sua idade:\n'))
    idades.append(geral["idade"])
    cadastro.append(geral.copy())
    controle = int(input("Deseja parar? 1- sim 2- não\n"))
    if controle == 1:
        break

print(f'{c} pessoas foram cadastradas.')

for i in range(len(idades)):
    aux += idades[i]
media_idade = aux/(len(idades))
print(f'A média do grupo é de {media_idade} anos.')

for i in range(len(cadastro)):
    if cadastro[i]["sexo"] == "feminino":
        mulheres.append(cadastro[i])
print(f'As mulheres do grupo são:\n{mulheres}')

print('As pessoas acima da faixa etária são:')
for i in range(len(cadastro)):
    if cadastro[i]["idade"] > media_idade:
        print(cadastro[i])