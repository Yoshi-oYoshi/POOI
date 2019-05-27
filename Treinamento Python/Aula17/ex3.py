n = int(input())
matriz = [[x for x in range(n)]for j in range(n)]
x,y = map(int, input().split())
matriz[x-1][y-1] = -1
a,s = map(int, input().split())
matriz[a-1][s-1] = -2
if matriz[x-1].index(-1) >= matriz[n//2][n-1] and matriz[a-1].index(-2) >= matriz[n//2][n-1]:
    print('S')
elif matriz[x-1].index(-1) < matriz[n//2][n-1] and matriz[a-1].index(-2) < matriz[n//2][n-1]:
    print('S')
elif matriz[x-1].index(-1) < matriz[n-1][n//2] and matriz[a-1].index(-2) < matriz[n-1][n//2]:
    print('S')
elif matriz[x-1].index(-1) >= matriz[n-1][n//2] and matriz[a-1].index(-2) > matriz[n-1][n//2]:
    print('S')
else:
    print('N')