

from random import randrange
from time import sleep

dimencion=int(input("Ingrese la dimension del vector: "))
vector= []
for i in range(dimencion):
	vector.append(randrange(50,100))

for i in range(dimencion):
	print(f"el valor en la posicion {i+1} es {vector[i]}")
	sleep(1)

for j in range(len(vector)-1,0,-1):
        for i in range(j):
            if vector[i]>vector[i+1]:
                val= vector[i]
                vector[i] = vector[i+1]
                vector[i+1]=val

for i in range(dimencion):
	print(f"el vector ordenado en la posicion {i+1} es {vector[i]}")
	sleep(1)