
from random import randint
matriz=[]
menor=0
mayor=0
columna=0
fila=0

n=int(input('Ingrese el numero de filas: '))
m=int(input('Ingrese el numero de columnas: '))   
for i in range(n):
    matriz.append([0])
    for j in range(m-1):
        matriz[i].append(randint(0,100))
print(matriz)

for numero in matriz:
    for evalue in numero:
        if evalue > mayor:
            mayor = evalue
            columna=j
            fila=i
print("\n"*2)
print(f"El numero mayor es {mayor}")
print("La posicion de la fila es:  ",fila)
print("La posicion de la columa es: ",columna)