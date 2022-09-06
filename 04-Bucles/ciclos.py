# la sentencia for nos permite repetir codigo o bloques de codigo en un determinado rango, o bien , nos permite recorrer 
#estructuras como listas o diccionarios

#contar los primeros 9 numeros (repetira la accion de 1 a 10 veces)
for numero in range(1,10):
    print(numero)

#recorremos los elementos de una lista
autos = ["Renault", "Citroen", "Peugeot"]
for auto in autos:
    print(auto)

#recorremos los elementos de un Diccionario

d_autos = {
    'Chevrolet':'Captiva',
    'Subaru':'Legacy',
    'Hyundai':'Tucson',
    'Citroen':'C4'}

for nombre in d_autos:
    print ("marca: ",nombre, "| modelo: ", d_autos[nombre])


#sentencia while, al igual que con for repetimos x cantidad de veces una instruccion o bloque de instrucciones para ello 
# debemos especificar una condicion, permitiendo repetir las instrucciones siempre que se cumpla la condicion terminando las iteraciones
#cuando esta ya no se cumpla

tope = 0

while tope <=10:
    print("iteracion Nº ", tope)
    tope=tope+1

## podemos realizar un ciclo infinito igualando la condicion a true, y dentro de las instrucciones utilizando un condicional
#podemos especificar cuando terminara de iterar.
nuevotope=0
while True:
    nuevotope=nuevotope+1
    if(nuevotope==10):
        break
    else:
        print("Repitiendo")

    
