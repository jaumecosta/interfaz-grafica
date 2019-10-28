from tkinter import * 

raiz = Tk()
raiz.title('Calculadora 1.0')
raiz.resizable(0,0)


miFrame = Frame(raiz, width=1000, height=500, padx=30, pady=30)
miFrame.pack()

# ******** funcion *************
numeroVisor = StringVar()
def codigoBoton(num):
    numeroVisor.set(numeroVisor.get() + num)
#****************************************


# Visor 
visor = Entry(miFrame,font=('Arial',30), textvariable=numeroVisor)
visor.grid(row=0, column=0, columnspan=4)
visor.config(bg='#2B2A33', fg='white', justify='right')

# Boton

#fila uno
botoncalcular = Button(miFrame, text='AC', command=lambda:codigoBoton('AC'))
botoncalcular.grid(row=2, column=0)
botoncalcular.config(bg='#3C3B45', fg='white', width=6, height=3, font=('Arial',25), relief='solid', activeforeground='red')

botonmasmenos = Button(miFrame, text='+/-', width=4, command=lambda:codigoBoton('+/'))
botonmasmenos.grid(row=2, column=1)
botonmasmenos.config(bg='#3C3B45', fg='white',  width=6, height=3, font=('Arial',25), relief='solid')


botonresto = Button(miFrame, text='%', width=4, command=lambda:codigoBoton('%'))
botonresto.grid(row=2, column=2)
botonresto.config(bg='#3C3B45', fg='white',  width=6, height=3, font=('Arial',25), relief='solid')


botondividir = Button(miFrame, text='/', command=lambda:codigoBoton('/'))
botondividir.grid(row=2, column=3)
botondividir.config(bg='#FF8A08', fg='white', width=6, height=3, font=('Arial',25), relief='solid')

#fila dos

botonsiete = Button(miFrame, text='7', command=lambda:codigoBoton('7'))
botonsiete.grid(row=3, column=0)
botonsiete.config(bg='#56585E', fg='white',  width=6, height=3, font=('Arial',25), relief='solid')

botonocho = Button(miFrame, text='8', command=lambda:codigoBoton('8'))
botonocho.grid(row=3, column=1)
botonocho.config(bg='#56585E', fg='white',  width=6, height=3, font=('Arial',25), relief='solid')

botonnueve = Button(miFrame, text='9', command=lambda:codigoBoton('9'))
botonnueve.grid(row=3, column=2)
botonnueve.config(bg='#56585E', fg='white',  width=6, height=3, font=('Arial',25), relief='solid')

botonmultiplicar = Button(miFrame, text='x', command=lambda:codigoBoton('x'))
botonmultiplicar.grid(row=3, column=3)
botonmultiplicar.config(bg='#FF8A08', fg='white',  width=6, height=3, font=('Arial',25), relief='solid')

#fila tres
botoncuatro = Button(miFrame, text='4', command=lambda:codigoBoton('4'))
botoncuatro.grid(row=4, column=0)
botoncuatro.config(bg='#56585E', fg='white',  width=6, height=3, font=('Arial',25),relief='solid')

botocinco = Button(miFrame, text='5', command=lambda:codigoBoton('5'))
botocinco.grid(row=4, column=1)
botocinco.config(bg='#56585E', fg='white',  width=6, height=3, font=('Arial',25), relief='solid')

botonseis = Button(miFrame, text='6', command=lambda:codigoBoton('6'))
botonseis.grid(row=4, column=2)
botonseis.config(bg='#56585E', fg='white',  width=6, height=3, font=('Arial',25),relief='solid')

botonmenos = Button(miFrame, text='-', command=lambda:codigoBoton('-'))
botonmenos.grid(row=4, column=3)
botonmenos.config(bg='#FF8A08', fg='white', width=6, height=3, font=('Arial',25), relief='solid')


#fila cinco

botonuno = Button(miFrame, text='1', command=lambda:codigoBoton('1'))
botonuno.grid(row=5, column=0)
botonuno.config(bg='#56585E', fg='white',  width=6, height=3, font=('Arial',25), relief='solid')

botodos = Button(miFrame, text='2', command=lambda:codigoBoton('2'))
botodos.grid(row=5, column=1)
botodos.config(bg='#56585E', fg='white',  width=6, height=3, font=('Arial',25), relief='solid')

botontres = Button(miFrame, text='3', command=lambda:codigoBoton('3'))
botontres.grid(row=5, column=2)
botontres.config(bg='#56585E', fg='white',  width=6, height=3, font=('Arial',25), relief='solid')

botonmas = Button(miFrame, text='+', command=lambda:codigoBoton('AC'))
botonmas.grid(row=5, column=3)
botonmas.config(bg='#FF8A08', fg='white', width=6, height=3, font=('Arial',25), relief='solid')



#fila seis

botonCero = Button(miFrame, text='0', command=codigoBoton)
botonCero.grid(row=6, columnspan=2)
botonCero.config(bg='#56585E', fg='white',  width=12, height=3, font=('Arial',25), relief='solid')

botonComa = Button(miFrame, text=',', command=codigoBoton)
botonComa.grid(row=6, column=2)
botonComa.config(bg='#56585E', fg='white',  width=6, height=3, font=('Arial',25), relief='solid')

botonIgual = Button(miFrame, text='=', command=codigoBoton)
botonIgual.grid(row=6, column=3)
botonIgual.config(bg='#FF8A08', fg='white',  width=6, height=3, font=('Arial',25), relief='solid')


raiz.mainloop()