import random

try:
    n=int(input('Ingrese cantidad de numeros entre 0 y 1 con 6 digitos:  '))
except:
    print('No se reconocio la cantidad, se generaran 5 numeros entre 0 y 1 con 6 digitos')
    n=5

numeros=[]

for i in range(n):
    numeros.append(round(random.random(),6))
print(numeros)