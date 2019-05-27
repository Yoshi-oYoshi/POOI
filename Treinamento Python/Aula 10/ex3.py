tempo = int(input('Digite quantos segundos os pães devem ficar no forno:'))
horas = tempo//3600
minutos = tempo%3600//60
segundos = tempo%3600%60
print(f'{horas}:{minutos}:{segundos}')