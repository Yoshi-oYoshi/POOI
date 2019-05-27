ficha = list ()
sum = 0
while True:
    nome = (input('Nome: '))
    nota1 = int(input('Nota1: '))
    nota2 = int(input('Nota2: '))
    media = (nota1+nota2)/2
    ficha[sum].append([nome,[nota1,nota2],media])
    print('=========================')
    print('No. NOME            MÉDIA')
    print('=========================')
    for i in range(len(ficha)):
        print('{}   {}          {:.1f}'.format(i,nome,media))
    