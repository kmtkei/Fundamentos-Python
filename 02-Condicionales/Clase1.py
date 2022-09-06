#podemos utilizar la instruccion if para ejecutar un bloque de codigo si es que se cumple con alguna condicion.
# en caso de no cumplirse la condicion es posible ejecutar un bloque de codigo alternativo utilizando la sentencia else 

opcion = 2

if(opcion == 2):
    print("El valor de la variable opcion es igual a 2")
else:
    print("El valor de la variable opcion es igual a : ", opcion)


#podemos utilizar la instruccion elif para definir condiciones intermedias para valores que no cumplan con la primera condicion.

edad = 18

if(edad < 18):
    print("Usted es menor de edad")
elif (edad == 18):
    print("Felicidades ha cumplido la mayoria de edad")
else:
    print("Usted es Mayor de edad")


# Recordatorio: Python a diferencia de otros lenguajes de programacion no utiliza llaves para abrir y cerrar bloques de codigo "{ }"
#para identificar estos bloques utilizamos ":" para abrir el bloque , para manejar las instrucciones que contiene dicho bloque se utiliza a identacion. 