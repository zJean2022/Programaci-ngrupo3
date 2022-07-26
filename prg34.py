

import random
def validar(nombre,edad,email,cedula):
    n=""
    m=1
    codigos=[".","?","¡","%","=","(","&","!","/",")","+","-","*","/"]
    if len(cedula)< 10:
        n=n+"Su cedula tiene menos de 10 digitos"
        m=0
    if len(cedula)>= 11:
        n=n+"Su cedula tiene mas de 10 digitos"
        m=0
    if edad < 10:
        n=n+"Su edad es menor a 10"
        m=0
    if edad > 50:
        n=n+"Su edad es mayor a 50"
        m=0
    if not email.endswith("@edu.ec"):
        n=n+"Error su correo no termina en @edu.ec"
        m=0
    if "@" in email[0]:
        n=n+"Su correo inicia con arroba"
        m=0
    if email.count("@") > 1:
        n=n+"Su correo tiene mas de un arroba"
        m=0
    if " " in email:
        n=n+"Su correo no debe tener espacios"
        m=0
    if "." in email[0]:
        n=n+"Su correo inicia con punto"
        m=0
    if len(nombre) < 3:
        n=n+"Su nombre tiene 3 digitos"
        m=0
    if " " not in nombre:
        n=n+"Debe ingresar sus dos nombres"
        m=0
    for i in nombre:
        for j in codigos:
            if i == j:
                n=n+"Su nombre tiene no debe tener caracteres especiales"
                m=0
    if m == 0:
        return(False)
    else:
        return(True)
cedula=random.randint(0, 100000000000)
cedulatext=str(cedula)
print(validar("Josue Churo",18,"josuechuro@edu.ec","1725907826"))
print(validar("Josue Churo",32,"josuechuro@edu.ec","17259078268"))
print(validar("Josue Churo",55,"josuechuro@edu.ec","1725907826"))
print(validar("Josue Churo",25,"josuechuro@edu.ec","1725907826"))
print(validar("Josue",36,"josue//ch@edu.ec","1725907826"))
print(validar("Josue Churo",10,"josuechuro@edu.ec","1725907826"))
print(validar("Josue Churo",5,"josuechuro@edu.ec","1725907826"))