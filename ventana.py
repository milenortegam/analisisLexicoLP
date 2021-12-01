import tkinter
from tkinter import *
from analizadorLexico import *
from analizadorSintactico import *


window = Tk()
window.title("Analizador de Ruby")
window.geometry('600x700')

lbl1 = Label(window, text="Ingrese el texto a analizar", font=("Helvetica"))
lbl1.grid(row=5, column=2)
txt = Text(window, width=40, height=10, background="white", foreground="black", font=("Helvetica",15))
txt.grid(column=2, row=6)

lbl10 = Label(window, text="", font=("Helvetica"))
lbl10.grid(row=6, column=2)


lbl3 = Label(window, text="Resultado del análisis", font=("Helvetica"))
lbl3.grid(row=8, column=2)
txt2 = Text(window, width=40, height=10, background="white", foreground="black", font=("Helvetica",15))
txt2.grid(column=2, row=9)


lblc = Label(window, text="")
lblc.grid(column=2, row=12)

def clear():
    txt.delete("1.0","end")


def clear2():
    txt2.delete("1.0","end")


def clickedlex():
    lblc.configure(text="Análisis léxico realizado")
    cadena = txt.get("1.0", "end")
    resultadoLex = inputLex(cadena)
    txt2.insert(INSERT, resultadoLex)


def clickedsint():
    lblc.configure(text="Análisis sintáctico realizado")
    cadena = txt.get("1.0", "end")
    resultadoSint = inputSint(cadena)
    txt2.insert(INSERT, resultadoSint)

btncl = Button(window, text="Borrar contenido", command=clear)
btnlex = Button(window, text="Léxico", command=clickedlex)
btnsint = Button(window, text="Sintáctico", command=clickedsint)

btncl2 = Button(window, text="Borrar resultados", command=clear2)

lb = Label(window, text="")
lb.grid(column=1, row=3)
lb = Label(window, text="")
lb.grid(column=1, row=4)
lbl = Label(window, text="Tipo de análisis")
lbl.grid(column=2, row=1)

btncl.grid(column=3, row=6)
btnlex.grid(column=1, row=2)
btnsint.grid(column=2, row=2)
btncl2.grid(column=3, row=9)

window.mainloop()
