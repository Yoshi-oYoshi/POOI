letras = [['q', 'z'],['j','x'],['k'],['f','h','v','w','y'],['b','c','m','p'],['d','g'],['a', 'e', 'f', 'i', 'l', 'n', 'o', 'r', 's', 't', 'u']]
word = input().lower()
aux=0
aws=0
for i in range(len(letras)):
    for x in range(len(letras[i])):
        aux = word.count(letras[i][x])
        if i == 0 and aux>0:
            aws +=  aux*10
        elif i == 1 and aux>0:
            aws += aux*8
        elif i == 2 and aux>0:
            aws += aux*5
        elif i == 3 and aux>0:
            aws += aux*4
        elif i == 4 and aux>0:
            aws += aux*3
        elif i == 5 and aux>0:
            aws += aux*2
        elif i == 6 and aux>0:
            aws += aux
        aux = 0
print(aws)