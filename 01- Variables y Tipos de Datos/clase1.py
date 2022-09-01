# Esto es un comentario 

"""
esto es un comentario multi
linea

"""

# utilizamos print para imprimir mensajes por pantalla

from operator import truediv


print("Hola Mundo")

# podemos realizar saltos de lineas dentro de una instruccion mediante el comando \n

print("Hola \n Mundo")

# podemos utilizar funciones del sistema para realizar tareas como la de limpiar pantalla utilizando la funcion system para ello debemos 
# importar del paquete os y utilizaremos la funcion system seguida del comando como parametro, donde: 
# cls sera la instruccion para limpiar pantalla en windows y clear en linux / mac

"""
import os
os.system("clear")

"""

# Variables 
# Para definir una variable simplemente escribiremos el nombre de la misma inicializandola con su valor por defecto o inicial.

#variable - Cadena de texto 

cadena = "Esto es una cadena"

#variable - Numerica 

numero = 2

# Variable de tipo - Booleana
logica = True

print(cadena)
print(numero)
print(logica)

#en python una variable puede cambiar su tipo de dato desde que se define hasta su ultimo valor por lo que con el comando type() podemos
#saber que tipo de dato contiene cada variable 

tipovariable = "esto es un string"
print("La variable tipovariable es de tipo: ",type(tipovariable))
tipovariable = 2
print("La variable tipovariable es te tipo: ",type(tipovariable))

# para solicitar datos por teclado utilizaremos la funcion input y guardar el valor en una variable.

nombre = input('Ingrese su Nombre: ')
print("Hola "+ nombre) 

# podemos modificar la salida de print añadiendo formato alternado entre texto y variables:

print(f"Hola {nombre} , Bienvenido ")

#Para ingresar datos por teclado es necesario saber que siempre seran de tipo string (cadena de texto) por lo que es necesario
#realizar una conversion en caso de necesitar otro tipo de dato para realizar operaciones. 

variableUno = input("Ingrese Valor: ")
print(type(variableUno))

variableDos = int(input("Ingrese Valor: "))
print(type(variableDos))

variableTres = str(variableDos)
print(f"aqui se convierte nuevamente el valor a string de {variableTres}",type(variableTres))

variableCuatro = float(input("Ingrese Valor: "))
print(type(variableCuatro))

