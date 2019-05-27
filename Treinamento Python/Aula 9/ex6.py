num = int(input())
sum = 0
cont = 1
while True:
    if num == 123:
        break
    else:
        sum += num
        cont += 1
        num = int(input())
print(f'You inserted {cont-1} numbers and their sum is {sum}')
