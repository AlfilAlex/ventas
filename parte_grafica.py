#Agregar un producto
#Agregar el inicio de un nuevo día
#Agregar una venta para un dia determinado
#Agregar una cantidad incial para un día determiando

from tkinter import Tk, Button, Frame
from coordinador import iniciadora

clase_preparadora = 'clase_en_proceso'

root = Tk()
root.geometry('500x300')
root.title('Venta')

frame = Frame(root, width=500, height=300)
frame.grid(row=0, column=0)


def venta():
    print('Se hizo una venta')
    pass

def iniciador():
  root = Tk()
  root.geometry('500x400')
  root.title('Venta_de_hoy')
  while True:
    iniciador = iniciadora(root).grid(row=0, column=0)
    root.mainloop()
    


boton_archivo = Button(frame, text='Se hizo una venta', command=venta)
boton_archivo.grid(row=1, column=0, padx=20, pady=30)

boton_archivo = Button(frame, text='Preparar_Programa', command=iniciador)
boton_archivo.grid(row=0, column=0, padx=20, pady=30)

root.mainloop()
















