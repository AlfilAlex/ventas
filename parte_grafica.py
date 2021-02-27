#Agregar un producto
#Agregar el inicio de un nuevo día
#Agregar una venta para un dia determinado
#Agregar una cantidad incial para un día determiando

from tkinter import Tk, Button, Frame, Text
from coordinador import iniciadora
from inicio import mainthing
from tkinter import ttk

from funciones_db import ventas


clase_preparadora = 'clase_en_proceso'

root = Tk()
root.geometry('600x300')
root.title('Venta')

frame = Frame(root, width=500, height=300)
frame.grid(row=0, column=0)

frame2 = Frame(frame, bg = 'red')
frame2.grid(row=0, column=2, padx=20, pady=30)

def venta():
    prod_id = venta_Prod.get()
    sell_Num = venta_Num.get()
    ventas(prod_id, sell_Num)
    print('Se hizo una venta')
    pass

def iniciador():
    root = Tk()
    app = mainthing(root)
    root.mainloop()
    
#Seccion de venta
venta_Prod = ttk.Combobox(frame, state="readonly")
venta_Prod["values"] = ["Dulce", "Mole", "Rajas_queso", "Rojos"]
venta_Prod.grid(row=0, column=0, padx=20, pady=30) #, padx=20, pady=30

venta_Num = ttk.Combobox(frame)
venta_Num["values"] = [1, 2, 3, 4, 5, 6, 7, 8, 9]
venta_Num.grid(row=0, column=1)

boton_sumVenta = Button(frame2, text='Sumar venta', command=venta)
boton_sumVenta.grid(row=0, column=0)

boton_resVenta = Button(frame2, text='Restar venta', command=venta)
boton_resVenta.grid(row=0, column=1)



boton_archivo = Button(frame, text='Preparar_Programa', command=iniciador)
boton_archivo.grid(row=3, column=0, padx=20, pady=30)

#
# combox3 = ttk.Combobox(frame, state="readonly")
# combox3["values"] = ["Python", "C", "C++", "Java"]
# combox3.grid(row=2, column=0, padx=20, pady=30)

# outputtxt = Text(frame, height = 10, width = 25, bg = "light yellow")
# outputtxt.grid(row=2, column=1, padx=20, pady=30)

root.mainloop()
















