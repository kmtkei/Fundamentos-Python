import random

print("Ejercicio Sorteo")

numeros = []
numeros_maximos = 5

while(len(numeros) != numeros_maximos):
    nuevonumero = int(input("Ingrese su numero (telefono/rut) para el sorteo: "))
    numeros.append(nuevonumero)

print("Inicia Sorteo: ")
sorteo = random.randint(1, len(numeros))
print("el ganador es : " , numeros[sorteo])
