
numero=0 #asignar una condicion para el numero en cero
resultado= 1 #asignar una condicion para el resultado en uno
contador3=0 #asignar una condicion para el contador3 en cero
suma=0 #asignar una condicion para la suma en cero
contador5=0 #asignar una condicion para el contador5 en cero
contadorpar=0 #asignar una condicion para el contadorpar en cero
contadorimpar=0 #asignar una condicion para el contadorimpar en cero
numero= input("Por favor ingrese un numero: ") #Ingresar numero por teclado 
numero= int(numero) + 1  #asignamos que numero es igual a numero+1
for i in range(1,numero): #Solicitamos una condicion con for i para dar un rango
        print("Tabla de multiplicar : " ,str(i), "\n") #Imprimir la tabla de multplicar 
        for j in range (1,16) : #Solicitamos una condicion con for j para dar un rango de 1 a 16
            resultado= i * j #Asiganamos que el resultado sea igual que i * j
            print ( i , "  *  " ,j , " = " , resultado) #Imprimir i * j
            if (resultado % 3)==0: #Solicitamos una condicion con if si el resultado modulo 3 es igual a cero
                contador3+=1 #Asiganamos que el contador3+ sea igual a uno
            if (resultado % 5)==0: #Solicitamos una condicion con if si el resultado modulo 5 es igual a cero
                contador5+=1 #Asiganamos que el contador5+ sea igual a uno
            if (resultado % 2)==0: #Solicitamos una condicion con if si el resultado modulo 2 es igual a cero
                contadorpar+=1 #Asiganamos que el contadorpar+ sea igual a uno
            else:
                contadorimpar+=1 #Asiganamos que el contadorimpar sea igual a uno
            suma+=resultado #Asiganamos que la suma+ sea igual al resultrado
print("la suma de los numeros es: ",suma) #Imprimir la suma de los numeros es,tomar el valaor suma
print("el promedio de los numeros es: ",suma/15) #Imprimir el promdeio de los numeros es , tomar el valor suma dividido para 15
print("los multiplos de 3 son:",contador3) #Imprimir los multimplos de 3 son, tomar el valor de contador3
print("los multiplos de 5 son:",contador5) #Imprimir los multimplos de 5 son, tomar el valor de contador5
print("los numeros pares son: ",contadorpar) #Imprimir los numeros pares son, tomar el valor de contadorpar
print("Los numeros impares son: ",contadorimpar) #Imprimir los numeros impares son, tomar el valor de contadorimpar
print("\n") #Imprimir un espacio

    