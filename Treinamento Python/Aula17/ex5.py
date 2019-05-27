def Fatorial(x):
    if x > 1:
        sum = x*Fatorial(x-1)
        return sum
    elif x == 1:
        return x



lista = [int(x) for x in input('\nInsira sua lista.\n').split()]
soma = 0
for i in range(len(lista)):
    soma += lista[i]
media = soma/len(lista)
sum = 0
while True:
    choice = int(input("\nO que deseja fazer?\n1-Calcular fatorial.\n2-Calcular a soma dos números maiores que a média.\n3-Ver o array em ordem descrescente.\n4-Desligar o programa.\n5-Inserir uma nova lista.\n"))
    if choice == 1:
        lista.sort()
        for i in range(len(lista)):
            print(f'\nNúmero: {lista[i]}\nValor fatorial: {Fatorial(lista[i])}\n', '=' * 20)
    elif choice == 2:
        lista.sort()
        for i in range(len(lista)):
            if lista[i] > media:
                sum += lista[i]
        print('\n',sum,'\n')
    elif choice == 3:
        lista.sort()
        lista.sort(reverse=True)
        print(f'{lista}')
    elif choice == 4:
        print('\nGood bye\n')
        exit
    elif choice == 5:
        for i in range(len(lista)):
            lista.pop()
        lista = [int(x) for x in input('\nInsira a sua lista.\n').split()]
        soma = 0
        for i in range(len(lista)):
            soma += lista[i]
        media = soma/len(lista)
        sum = 0