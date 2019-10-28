"""
    INTERFACE GRAFICAS, PYTHON
"""

#Inicializar libreria Tkinter
from tkinter import * #No hace falta descargar nada

'''RAIZ '''
raiz=Tk()

# titulo de la ventana 
raiz.title('Primera Interface')

# controlar el ancho y alto de la ventana, con booleanos
raiz.resizable(0,0)

#cambiar tamaño de la raiz
raiz.geometry('800x600')

# diferentes configuraciones
raiz.config(bg='red')

""" FRAME """
# instanciar la clase frame 
primerFrame = Frame()
# Empaquetar el Frame dentro de la Raiz
primerFrame.pack()

primerFrame.config(bg='yellow')

# eliminar el tamaño de la raiz con nuestro nuevo tamaño del Frame
primerFrame.config(width='500', height='400')

# bordes
primerFrame.config(bd=20)
primerFrame.config(relief='groove')

#mover Frame alrededor del la Raiz
primerFrame.pack(side='right', anchor='s')

# crear un bucle infinito para que la vantana este ecuchando las acciones del usuario permanentemente
raiz.mainloop()