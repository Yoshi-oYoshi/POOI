A = 80000
B = 200000
anos = 0
while A < B:
    Aa = A
    A = Aa * 1.03
    Bb = B
    B = Bb * 1.015
    anos += 1
print(anos)