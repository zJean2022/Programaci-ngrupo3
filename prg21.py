
def bisiesto(año):
    if año<1582:
        return False
    elif año%4 !=0:
        return False
    elif año%100 !=0:
        return True
    elif año%400 !=0:
        return False
    return True
Data=[1900, 2000, 2016, 1987]
Resultado=[False,True,True,False]
for i in range(len(Data)):
    y=Data[i]
    print(y,'->',end=' ')
    resultado=bisiesto(y)
    if resultado==Resultado[i]:
        print('OK')
    else:
        print('Failed')