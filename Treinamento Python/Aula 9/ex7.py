num = int(input('Mande um número: '))
cont = 1
maior = num
menor = num
sum = 0
while True:
    word = input('Deseja continuar? y/n\n')
    if word == 'n':
        break
    else:
        num = int(input('Mande um número: '))
        if num > maior:
            maior = num
            sum += num
            cont += 1
        elif num < menor:
            menor = num
            sum += num
            cont += 1
        else:
            sum += num
            cont += 1
print(f'Você colocou {cont} números onde:\nMaior = {maior}\nMenor = {menor}\nSoma = {sum}\nMédia = {sum/cont}')            
