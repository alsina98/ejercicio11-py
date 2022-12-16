from io import open

class Vehiculo:
    marca = ""
    precio = ""
    velocidad = ""

v1 = Vehiculo()
v2 = Vehiculo()

marcaO = v1.marca = str("Open")
precioO = v1.precio = str("10500")
velocidadO = v1.velocidad = str("120")

marcaV = v2.marca = str("volkswagen")
precioV = v2.precio = str("11560")
velocidadV = v2.velocidad = str("122")

obj1 = ("El coche de la marca {}, tiene un precio de {} con una velocidad de {}\n".format(marcaO, precioO, velocidadO))
obj2 = ("El coche de la marca {}, tiene un precio de {} con una velocidad de {}\n".format(marcaV, precioV, velocidadV))

archivo_texto = open('object.txt', 'w')
archivo_texto.write(obj1) # El coche de la marca Open, tiene un precio de 10500 con una velocidad de 120
archivo_texto.write(obj2) 
archivo_texto.close()

archivo_texto = open('object.txt', 'r')
texto = archivo_texto.read()
archivo_texto.close()

print(texto)