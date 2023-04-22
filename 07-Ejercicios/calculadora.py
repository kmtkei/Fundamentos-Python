print("Calculadora")

print("""
      1. Suma
      2. Resta
      3. Multiplicacion
      4. Division
      """)
   

while(True):
    opcion = int(input("Ingrese una opcion: "))
    a = int(input("Ingrese un numero: "))
    b = int(input("Ingrese otro numero: "))

    if opcion == 1:
        print (a + b)
    elif opcion == 2:
        print (a - b)
    elif opcion == 3:
        print (a * b)
    elif opcion == 4:
        print (a / b)
    else:
        print ("adios")
        break