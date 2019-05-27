z = True
a = int(input("Insira um número: "))
for x in range(2,a):
    if a%x == 0:
        z = False
        break
if z == True:
    print(f'{a} é primo')
else:
    print(f'{a} não é primo')