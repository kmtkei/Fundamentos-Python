
# Listas con marcas de automoviles 
autos = ["Ford", "Volvo", "BMW", "Hyundai", "Chevrolet", "Kia", "Citroen"]
#imprimimos el valor numero 3 del array , (considerando que el primer elemento es el indice 0 )
print(autos[3])

# Metodos básicos para manipulacion de listas
#len()    -> nos devuelve el largo (elementos) de nuestro array
#.append() -> permite agregar un elemento al final del array
#.pop(1)  -> nos permite eliminar un elemento de la posicion (1)
#.remove("Volvo") -> nos permite eliminar el elemento "Volvo" de la lista
#.sort() -> nos permite ordenar nuestro array
#.clear() -> elimina todos los elementos del array

print(len(autos))  
autos.append("Peugeot")
print(autos[len(autos)-1])
print(autos[3])
autos.pop(3)
print(autos[3])
print(autos[0])
autos.remove("Ford")
print(autos[0])
autos.clear()
print(len(autos))

# Diccionarios

diccionario1 =	{
  "Marca": "Citroen",
  "Modelo": "C4",
  "Año": 2007
}
print(diccionario1)

print(diccionario1["Marca"])

print(len(diccionario1))

diccionario2 =	{
  "Marca": "Chevrolet",
  "Automatico": False,
  "Año": 2015,
  "Colores": ["Blanco", "Gris", "Azul"]
} 

print(diccionario2["Colores"])

print(type(diccionario2)) 
