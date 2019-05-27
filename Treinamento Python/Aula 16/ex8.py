y = int(input('Insira um valor: '))
x = int(input('Insira outro valor: '))
aws = []
if x > y:
    for i in range(y,x+1):
        aws.append(i)
elif y > x:
    for i in range(x, y+1):
        aws.append(i)
    aws.reverse()
else:
    aws.append(x)
print(aws)