A, B = map(int, input('Insira a população das duas cidades:\n').split())
Ac, Bc = map(float, input('Insira as taxas de crescimento das cidades respectivamente:\n').split())
anos = 0
while A < B:
    Aa = A
    A = Aa*(Ac/100+1)
    Bb = B
    B = Bb*(Bc/100+1)
    anos += 1
print(anos)