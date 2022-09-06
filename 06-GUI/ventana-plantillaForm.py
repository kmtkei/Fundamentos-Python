from textwrap import fill
from tkinter import *

class Programa :
    def __init__(self):
        self.title = "Ejercicio Básico GUI - Python"
        self.resizable = False
        self.size= "450x450"
    
    def cargar(self):
        ventana = Tk()
        self.ventana = ventana
        ventana.title(self.title)
        ventana.geometry(self.size)
        if (self.size==False) :
            ventana.resizable(0,0)
        else:
            ventana.resizable(1,1)

    def addTexto(self, textop, fila):
        texto = Label(self.ventana, text=textop)
        #texto.pack()
        texto.grid(row=fila, column=1, padx=10, pady=10)
    
    def addinput(self, fila):
        input = Entry(self.ventana)
        input.grid(row=fila, column=2, padx=10, pady=10, sticky=W)
        input.config(justify="right", state="normal")
    
    def addEncabezado(self, textop, fila):
        encabezado = Label(self.ventana, text=textop)
        encabezado.config(
            fg="darkgray",
            bg="white",
            font=("Open Sans", 18),
            padx=20,
            pady=10
        )
        encabezado.grid(row=fila, column = 0, columnspan=4, sticky=NW)
        #encabezado.pack(side=LEFT, anchor=NW, fill=X, expand=YES)

    def addtextArea(self, fila):
        txtArea = Text(self.ventana)
        txtArea.grid(row=fila, column=2, padx=10, pady=10, sticky=W)
        txtArea.config(state="normal",width=30, height=5)

    def addBoton(self, fila, tboton):
        boton = Button(self.ventana, text=tboton)
        boton.grid(row=fila, column=2, padx=10, pady=10, sticky=W)

    def lanzarVentana(self):
        self.ventana.mainloop()
    
##iniciar Ventana 
programa = Programa()
programa.cargar()
programa.addEncabezado("Encabezado", 1)
programa.addTexto("Nombre", 2)
programa.addinput(2)
programa.addTexto("Apellidos", 3)
programa.addinput(3)
programa.addTexto("Descripcion", 4)
programa.addtextArea(4)
programa.addBoton(5, "Enviar")
programa.lanzarVentana()


