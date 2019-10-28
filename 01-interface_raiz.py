"""
    INTERFACE GRAFICAS, PYTHON
"""

#Inicializar libreria Tkinter
from tkinter import * #No hace falta descargar nada

#instanciar la clase TK
raiz=Tk()

# titulo de la ventana 
raiz.title('Primera Interface')

# controlar el ancho y alto de la ventana, con booleanos
raiz.resizable(0,0)

#cambiar tamaño de la raiz
raiz.geometry('800x600')

#cambiar el icono de la ventana
raiz.iconbitmap('icono.ico')

# diferentes configuraciones
raiz.config(bg='red')

# crear un bucle infinito para que la vantana este ecuchando las acciones del usuario permanentemente
raiz.mainloop()