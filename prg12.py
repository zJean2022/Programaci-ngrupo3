
filas=columnas=0	#inicializo las variables '''
while filas<=0:
    filas=int(input("Ingrese un numero para la primera fila: "))  
while columnas<=0:
    columnas=int(input("Ingrese un numero para las columnas  "))
	
print("  |",end=" ")	
for i in range(0,columnas+1):  
	print(f"\t{i}",end=" ")
print()	

for i in range(0,columnas*10):   
	print("-",end="")
print()	
for i in range(1,filas+1):
	print("\n",i,"|",end="")  
	for j in range (columnas+1):
		print(i*j,end="\t")
        


	  