
numero = input("Ingrese un numero palidromo: ")

def palidromo_num (string):
    x=""
    for i in  string:
        x= i + x
    return x
if numero== palidromo_num (numero):
    print("El numero si es palidromo")
else:
    print("El numero no es palidromo")
