
import random
def vald(numero):
	if numero>=4 and numero<=30:
		print("cantidad correcta")
		return True
	else:
		print("cantidad incorrecta")
		return False
		
def rell(vector,n,primos):
	i=0
	j=0
	for i in range (n-1):
		vector.append(random.randint(1,40))
	print("El vector es: ")
	for j in range (n):
		print(vector[j])
		if prim(vector[j])==True:
			primos.append(vector[j])

def prim(numero2):
	for n in range(2,numero2):
		if numero2%n == 0:
			return False
	return True
	
	
n=int(input("Ingrese la cantidad: "))
if vald(n)==True:
	primos=[]
	vector=[n]
	rell(vector,n,primos)
	if len(primos)==0:
		print("No hay numeros primos")
	else:
		i=0
		print("Los numeros primos son los siguinetes: ")
		for i in range(len(primos)):
			print(primos[i])
		
	