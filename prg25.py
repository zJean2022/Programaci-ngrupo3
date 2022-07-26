

def l100kmtompg(litros):
    n1=(100*1000)/1609.344
    n2= litros/3.785411784
    return n1/n2

def mpgtol100km(millas):
    litros=3.785411784
    kilometros=(millas*1609.344)/1000
    km=kilometros/100 
    return litros/km
print(l100kmtompg(3.9))
print(l100kmtompg(7.5))
print(l100kmtompg(10.))
print(mpgtol100km(60.3))
print(mpgtol100km(31.4))
print(mpgtol100km(23.5))