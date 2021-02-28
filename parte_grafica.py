from tkinter import Tk, Button, Frame, Text, ttk, Label, END
from coordinador import iniciadora
from productos import prodcutos
from funciones_db import *


clase_preparadora = 'clase_en_proceso'
root = Tk()
root.title('Venta')

frame = Frame(root, width=500, height=300)
frame.grid(row=0, column=0)

frame2 = Frame(frame, bg = 'red')
frame2.grid(row=0, column=2, padx=20, pady=30)

def venta():
    prod_id = venta_Prod.get()
    sell_Num = venta_Num.get()
    ventas(prod_id, sell_Num)
    resumen = prod_Resum()
    outputtxt.delete('1.0', END)
    for producto in resumen:
        outputtxt.insert(END, producto[2] + ' ' + str(producto[3]) + '\n')


def add_Products():
    root = Tk()
    app = prodcutos(root)
    root.mainloop()
    
#Seccion de venta
venta_Prod = ttk.Combobox(frame, state="readonly")
tabla = prod_Select()
venta_Prod["values"] = [x[1] for x in tabla]
venta_Prod.grid(row=0, column=0, padx=20, pady=30) #, padx=20, pady=30

venta_Num = ttk.Combobox(frame)
venta_Num["values"] = [1, 2, 3, 4, 5, 6, 7, 8, 9]
venta_Num.grid(row=0, column=1)

boton_sumVenta = Button(frame2, text='Sumar venta', command=venta)
boton_sumVenta.grid(row=0, column=0)

boton_resVenta = Button(frame2, text='Restar venta', command=venta) #Aun no resta venta
boton_resVenta.grid(row=0, column=1)

label = Label(frame, text="Resumen")
label.grid(row=3, column=0, padx=20, pady=30)
#frame3 = Frame(frame)
outputtxt = Text(frame, height = 10, width = 25, bg = "light yellow")
outputtxt.grid(row=3, column=1, padx=20, pady=30)


boton_archivo = Button(frame, text='Productos A/B', command = add_Products)
boton_archivo.grid(row=4, column=0, padx=20, pady=30)

root.mainloop()
















