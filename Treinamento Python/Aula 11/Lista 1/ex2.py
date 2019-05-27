lista = list(map(int,input('Insira uma lista de números inteiros:\n').split()))
x = int(input('Insira o número que você deseja procurar: '))
awnser = lista.count(x)
print(f'O número {x} aparece {awnser} vezes.')