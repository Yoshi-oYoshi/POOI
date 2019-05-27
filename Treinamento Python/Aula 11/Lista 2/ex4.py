n = ('Arroz', 3.50,'Alface',2.50,'rúcula',3.00)
print('='*37)
print('          LISTAGEM DE PREÇOS')
print('='*37)
for i in range(0,len(n),2):
    print(n[i],'.'*(30-len(n[i])),'R${}'.format(n[i+1]))
print('='*37)