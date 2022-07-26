

from random import randrange

def matrix_completa(matrix):
	for i in range(10):
		for j in range(7):
			matrix[i][j] = randrange(0,100)

	return matrix

def materias1(matrix):
	materias = []
	for i in range(10):
		suma = 0
		for j in range(7):
			suma += matrix[i][j]
		materias.append(suma)

	return materias

def notas1(matrix):
	notas = []
	for j in range(7):
		suma = 0
		for i in range(10):
			suma += matrix[i][j]
		notas.append(suma)

	return notas

def menu1(materias,notas):
	suma = 0
	for i in range(len(materias)):
		suma += materias[i]

	promedio = suma/len(materias)

	men = materias[0]
	pos = 0
	for i in range(len(materias)):
		if materias[i]<men:
			men = materias[i]
			pos = i + 1

	print("promedio: ",promedio)
	print(f"Materia con perores promedios es: M{pos} {materias[pos]}")

matrix = []
materias = []
notas = []

for i in range(10):
	a = [0]*7
	matrix.append(a)


matrix =matrix_completa(matrix)

print("\t\tMatriz")

for i in range(10):
	for j in range(7):
		print(matrix[i][j],end="\t")
	print("")

print("materias totales ")
print(materias1(matrix))
materias =materias1(matrix)

print("notas totales")
print(notas1(matrix))
notas =notas1(matrix)


menu1(materias,notas)