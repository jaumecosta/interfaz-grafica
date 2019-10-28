from tkinter import *

raiz = Tk()

miFrame=Frame(raiz, width=1000, height=500, padx=20, pady=20)
miFrame.pack()


# Entry
#Entry es un cuadro de texto no es un input
nombreLabel = Label(miFrame, text='Nombre:')
nombreLabel.grid(row=0,column=0,padx=5,pady=0, sticky='e')

cuadroTexto = Entry(miFrame)
cuadroTexto.grid(row=0,column=1,padx=0,pady=0)
cuadroTexto.config(fg='blue',justify='left')

# EMail
emailLabel = Label(miFrame, text='Email:')
emailLabel.grid(row=1,column=0,padx=5,pady=0, sticky='e')

cuadroEmail = Entry(miFrame)
cuadroEmail.grid(row=1,column=1,padx=0,pady=0)
cuadroEmail.config(fg='blue',justify='left')

#Password
passwordLabel = Label(miFrame, text='Password:')
passwordLabel.grid(row=2,column=0,padx=5,pady=0, sticky='e')


cuadroPassword = Entry(miFrame)
cuadroPassword.grid(row=2,column=1,padx=0,pady=0)
cuadroPassword.config(fg='blue',justify='center', show='*')

raiz.mainloop()