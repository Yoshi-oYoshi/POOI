classe = {}
aluno = []
while True:
    classe["nome"] = str(input('Insira o nome do aluno:\n'))
    classe["media"] = int(input('Insira a média do aluno:\n'))
    aluno.append(classe.copy())
    controle = int(input("Deseja parar? 1- sim 2- não\n"))
    if controle == 1:
        break

print(aluno)