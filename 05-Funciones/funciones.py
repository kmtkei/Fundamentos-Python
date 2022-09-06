##podemos reutilizar instrucciones o procesos mediante funciones o metodos, estos permiten reducir la cantidad de lineas y mejorar la 
#legibilidad de nuestro codigo ya que mediante el contexto o tarea que cumpla nuestra funcion nos permitira encontrar mas rapido errores de procedimientos 
#o ubicacion de codigo para mejoras. 


#funcion que recibe 2 parametros (a, b) y retorna un valor el cual en este caso sera el resultado de la operacion a+b
def suma(a, b):
    return a+b


#imprimimos por pantalla el valor retornado por la funcion suma, a la cual se le envio como parametro los valores 2 y 2 (a y b respectivamente)
print (suma(2,2))

def resta(a,b):
    return a-b
def multiplicacion(a,b):
    return a*b
def division(a,b):
    return a/b

#podemos utilizar estas llamadas a la funcion para guardar el valor retornado en variables ademas de imprimir el valor retornado como vimos lineas anteriores

resultado = multiplicacion(2,2)

