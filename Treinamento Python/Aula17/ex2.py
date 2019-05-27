n = int(input())
tiro = [[int(x) for x in input().split()]]
penalidades = 0
for i in range(n-1):
    tiro.append([int(x) for x in input().split()])
    if ((tiro[i][0]**2 + tiro[i][1]**2)**0.5) < ((tiro[i+1][0]**2 + tiro[i+1][1]**2)**0.5):
        penalidades += 1
print(penalidades)