X, Y = map(int, input('Digite dois números: ').split())

while True:
    selecao = int(input('Bem vindo!\nSelecione o que deseja fazer:\n[1] - somar\n[2] - multiplicar\n[3] - mostrar o maior\n[4] - digitar novos números\n[5] - sair\n'))
    if selecao == 1:
        print(X + Y)
    elif selecao == 2:
        print(X*Y)
    elif selecao == 3:
        if X > Y:
            print(X)
        elif Y > X:
            print(Y)
        else:
            print('Eles são iguais u.u')
    elif selecao == 5:
        break
    elif selecao == 4:
        X, Y = map(int, input('Digite dois números: ').split())
