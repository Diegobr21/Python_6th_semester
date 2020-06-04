from tkinter import*
from proyecto_modelado import juego, resultados, tirar_dados

root = Tk()
txt = StringVar()
root.title("Proyecto Modelado equipo 1")
#root.iconbitmap('osofime.ico')
frame = Frame(root, width=620, height=420)
frame.pack()
frame.config(cursor = 'pencil', bg = 'blue', border = 15, relief = 'ridge')
root.resizable(0, 0)


def jugar():
    try:
        corridas = int(entry_var.get())
        results = resultados(corridas)
        dinero = results[0]
        n_meta = results[1]
        n_quiebra = results[2]

        meta_var.set(n_meta)
        quiebra_var.set(n_quiebra)
        money_var.set(dinero)
    except:
        print('No es un numero entero, intente de nuevo')

def reset():
    entry_var.set('')
    meta_var.set('')
    quiebra_var.set('')
    money_var.set('')

titulo=Label(frame, text='7 - 11 Equipo 1 Modelado')
titulo.config(bg='blue', fg='white', font=('verdana', 14))
titulo.place(x=200, y=10)


label1 = Label(frame, text='Numero de corridas/juegos:')
label1.config(bg = 'blue', fg = 'white', font = ('verdana', 10))
label1.place(x = 10, y = 70)

entry_var = StringVar() # Cantidad de juegos a realizar/corridas
meta_var = StringVar() #Veces llegadas a la meta
quiebra_var = StringVar() #Veces llegadas a la quiebra
money_var = StringVar() #Dinero restante

entry=Entry(frame, width=60, textvariable=entry_var) #Ingresar texto
#corridas=entry_var.get()
entry.place(x=210, y=70)

btn=Button(frame, text='Jugar', command=jugar)
btn.place(x=220, y=110)

labelmeta = Label(frame, text='# de Metas')
labelmeta.config(bg = 'blue', fg = 'white', font = ('verdana', 10))
labelmeta.place(x = 10, y = 150)

entrym=Entry(frame, width=10, textvariable=meta_var) #Ingresar texto
entrym.place(x=15, y=180)

labelquiebra = Label(frame, text='# de Quiebras')
labelquiebra.config(bg = 'blue', fg = 'white', font = ('verdana', 10))
labelquiebra.place(x = 190, y = 150)

entryq=Entry(frame, width=10, textvariable=quiebra_var) #Ingresar texto
entryq.place(x=195, y=180)

labelmoney = Label(frame, text='Dinero restante')
labelmoney.config(bg = 'blue', fg = 'white', font = ('verdana', 10))
labelmoney.place(x = 390, y = 150)

entryd=Entry(frame, width=10, textvariable=money_var) #Ingresar texto
entryd.place(x=395, y=180)

btnreset=Button(frame, text='Reset', command=reset)
btnreset.place(x=300, y=300)

#Abajo de todo
root.mainloop()