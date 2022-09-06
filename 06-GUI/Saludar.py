from tkinter import *

ventana = Tk()
ventana.title("Saludar")
ventana.geometry("450x500")
ventana.resizable(0,0)

## Captura de Datos
def obtenerDato():
    saludo.set("Hola "+nombre.get())

nombre = StringVar()
saludo = StringVar()

## Agregar Encabezado
encabezado = Label(ventana, text="Saludar")
encabezado.config(
    font=("Open Sans", 18),
    padx=40,
    pady=10
)
encabezado.grid(row=0, column=1, columnspan=2)

## Agregar Label Nombre
texto = Label(ventana, text="Nombre")
texto.grid(row=1, column=1)

## Agregar Input Nombre
input = Entry(ventana, textvariable=nombre)
input.grid(row=1, column=2)

## Agregar Label Nombre
texto = Label(ventana, text="Saludo: ")
texto.grid(row=2, column=1)

## Agregar Label Nombre
texto = Label(ventana, textvariable=saludo)
texto.grid(row=2, column=2)

## Agregar Boton Saludar
boton = Button(ventana, text="Saludar", command=obtenerDato)
boton.grid(row=3, column=2)

ventana.mainloop()
