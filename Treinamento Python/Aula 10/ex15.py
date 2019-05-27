a,b = map(int,input('Insira dois números: ').split())
sum = 0
for x in range(a+1,b):
    print(x)
    sum += x
print(sum)