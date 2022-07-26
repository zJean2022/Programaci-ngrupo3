

import math
 
def numero_primo(num):
   
    if (num<=1):
        return False
 
    for i in range(3, math.ceil(math.sqrt(num))+1):
        if(num%i==0 and i!=num):
            return False
    return True
 
while True:
        num2= int(input("Ingrese un numero : "))
        if numero_primo(num2):
            print ("El numero si es primo" , num2)  
        break
    
  

