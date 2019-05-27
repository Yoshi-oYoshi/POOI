odd = 0
even = 0
for x in range(0,10):
    a = int(input('Insira um número:'))    
    if a%2 == 1:
        odd += 1
    else:
        even += 1       
print(f'Você insiriu {even} números pares e {odd} números ímpares')
