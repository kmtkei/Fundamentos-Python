print("Ejercicio rango etario")

edad= int(input("Ingrese su edad: "))
if(edad >0)&(edad <= 5 ):
    print("usted es un bebé")
elif(edad<=13):
    print("Usted es un niño")
elif(edad <= 18):
    print("usted es un adolecente")
elif(edad <= 30):
    print("usted es un adulto Joven")
elif(edad <= 60):
    print("usted es un adulto")
elif(edad <= 124):
    print("usted es un adulto mayor")
else:
    print("no pertenece a la edad")