n = [int(x) for x in input().split()]
a = [int(x) for x in n if x%2 == 0]
b = [int(x) for x in n if x%2 == 1]
print(f'{n}\n{a}\n{b}')