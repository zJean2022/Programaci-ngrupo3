

import random
n=int(input('Ingrese el numero de filas: '))
m=int(input('Ingrese el numero de columnas: ')) 
if n<4 or m<4:
	print("error debe ser mayor a 4")
elif n>30 or m >30:
	print("error debe ser menor a 30")
elif n!=m:
	print("error las matrices deben ser cuadradas")
else:
	matriz=[[int()for i in range(n)] for j in range(m)]
	matriz2=[[int()for i in range(n)] for j in range(m)]
	matriz3=[[int()for i in range(n)] for j in range(m)]
	diagonal = []
	secundaria = []
	for i in range(n):
	    for j in range (m):
	        matriz[i][j]=random.randint(50,1000)


	for i in range(n):
	    for j in range (m):
	        print ("/",matriz[i][j],"/",end="")
	        matriz2[i][j]=matriz[i][j]
	        matriz3[i][j]=matriz[i][j]
	    diagonal.append(matriz[i][i])
	    secundaria.append(matriz[i][(n-1)-i])
	    print(" ")

	for i in range(n):
	    for j in range (m):
	        matriz3[i][j]="-"

	for i in range(n):
	    matriz3[i][(n-1)-i]=secundaria[i]

	for i in range(n):
	    for j in range (m):
	        matriz2[i][j]="-"

	for i in range(n):
	    matriz2[i][i]=diagonal[i]


	print("Diagonal principal")
	for i in range(n):
	    for j in range (m):
	        print ("/",matriz2[i][j],"/",end="")
	    print(" ")

	print("Diagonal secundaria")
	for i in range(n):
	    for j in range (m):
	        print ("/",matriz3[i][j],"/",end="")
	    print(" ")

