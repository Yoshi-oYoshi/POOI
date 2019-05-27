n = int(input())
k = 0
x = 1
for i in range(0, n-1):
    if i == 0:
        print(k)
    if i == 1:
        print(x)
    else:
        sum = k + x
        k = x
        x = sum
        print(sum)