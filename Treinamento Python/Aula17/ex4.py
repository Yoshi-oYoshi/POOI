def Id_verification(ide):
    while True:
        if len(ids) >= 1:
            for i in range(0,len(ids)):
                while ide == ids[i]:
                    ide = int(input('iD já cadastrada!!!\nInsira outra iD: '))
            break
        else:
            break
    return ide

def Idade_menor(age):
    x = 0
    if len(menor_idade) < 2:
        menor = age
        menor_idade.append(nome)
        menor_idade.append(ide)
        menor_idade.append(profissao)
        menor_idade.append(menor)
    else:
        if age < menor:
            menor = age
            while x < 4:
                aux.pop()
                x+=1
            menor_idade.append(nome)
            menor_idade.append(ide)
            menor_idade.append(profissao)
            menor_idade.append(menor)

cadastro = list()
ids = list()
aux = list()
menor_idade = list() 
while True:
    nome = input('Insira seu nome: ')
    ide = int(input('Insira sua iD: '))
    ide = Id_verification(ide)
    profissao = input('Insira sua profissão: ')
    idade = int(input('Insira sua idade: '))
    Idade_menor
    while idade > 1000:
        idade = int(input('Insira uma idade válida!!!\n'))
    while True:
        print(f'Nome      = {nome}\niD        = {ide}\nProfissão = {profissao}\nIdade     = {idade}')
        n=int(input('Deseja alterar algum dado cadastrado?\n1-Nome\n2-id\n3-Profissão\n4-Idade\n5-Novo Cadastro\n6-Finalizar cadastro\n    '))
        while n > 7 or n < 1:
            n = int(input('Por favor faça uma seleção válida!\n'))
        
        if n == 1:
            nome = input('Insira seu nome: ')
        
        elif n == 2:
            ide = int(input('Insira sua iD: ')) 
            ide = Id_verification(ide)
        
        elif n == 3:
            profissao = input('Insira sua profissão: ')
        
        elif n == 4:
            idade = int(input('Insira sua idade: '))
            Idade_menor
        elif n == 5 or n == 6:
            break
    aux.append(nome)
    aux.append(ide)
    aux.append(profissao)
    aux.append(idade)
    ids.append(ide)
    cadastro.append(aux)
    for i in range(4):
        aux.pop()
    if n == 6:
        break
while True:
    print('Num.   Nome    iD      Profissão      Idade')
    for i in range(len(cadastro)+1):
        print(f' {i}.','   {cadastro[i][0]}'.ljust(3,' '),'{cadastro[i][1]}'.ljust(5,' '),'{cadastro[i][2]}'.ljust(5,' '),'{cadastro[i][3]}'.ljust(5,' '))
    while True:
        x = input('Deseja saber quem é o funcionário mais novo?\nY/n\n')
        if x.lower() == 'y':
            for i in range(4):
                print(f'{menor_idade[i]}')
                break
        elif x.lower() == 'n':
            break
        else:
            x = input('Por favor insira algo válido!!!\n')
    shutdown = input('digte sim para fechar o programa\n')
    if shutdown.lower() == 'sim':
        exit