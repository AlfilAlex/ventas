from tkinter import Tk, Button, Frame, Text, ttk, Label
import tkinter as tk
from funciones_db import *

class prodcutos(tk.Frame):
    """Esta clase abre una pestaña que permite posteriormente
       agregar nuevos articulos a la base de datos en la tabal productos"""
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.initialize()

    def initialize(self):
        self.parent.title("Productos")
        #En bg y fg pueden ir códigos de colores
        self.prod_Name = tk.Entry(self.parent, bg = "white", fg = "black") 
        self.prod_Name.grid(row=0, column=1,  sticky="ew", padx=20, pady=30)

        self.prod_Price = tk.Entry(self.parent, bg = "white", fg = "black") 
        self.prod_Price.grid(row=0, column=2, sticky="ew", padx=20, pady=30)

        self.add_Prod = tk.Button(self.parent, text="Agregar_producto", command = self.add_Producto)
        self.add_Prod.grid(row=0, column=3, padx=20, pady=30)


        self.prod_Name_list = ttk.Combobox(self.parent)
        tabla = self.lista_productos()
        self.prod_Name_list["values"] = [x[1] for x in tabla]
        self.prod_Name_list.grid(row=1, column=1,  sticky="ew", padx=20, pady=30)

        self.del_Prod = tk.Button(self.parent, text="Borrar_producto", command = self.del_Product_class)
        self.del_Prod.grid(row=1, column=2, padx=20, pady=30)

    def add_Producto(self):
        name, price = self.prod_Name.get(), self.prod_Price.get()
        table_Insert((name, price), funcion = 'productos')
        new_text = ""
        self.prod_Name.delete(0, tk.END)
        self.prod_Name.insert(0, new_text)
        self.prod_Price.delete(0, tk.END)
        self.prod_Price.insert(0, new_text)
        self.actualizar_lista()
    
    def lista_productos(self):
        """Permite obtener la lista de los productos de la BD en la tabla productos"""
        tabla = prod_Select()
        return tabla
    
    def actualizar_lista(self):
        tabla = self.lista_productos()
        self.prod_Name_list["values"] = [x[1] for x in tabla]

    def del_Product_class(self):
        prod_to_del = self.prod_Name_list.get()
        del_Product(prod_to_del)
        self.prod_Name_list.set('')
        self.actualizar_lista()





if __name__ == '__main__':
    root = tk.Tk()
    prod = prodcutos(root)
    root.mainloop()





















