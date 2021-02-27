from tkinter import Tk, Button, Frame, Text, ttk, Label
import tkinter as tk

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
        prod_Name = tk.Entry(self.parent, bg = "white", fg = "black") 
        prod_Name.grid(row=0, column=1,  sticky="ew", padx=20, pady=30)

        prod_Price = tk.Entry(self.parent, bg = "white", fg = "black") 
        prod_Price.grid(row=0, column=2, sticky="ew", padx=20, pady=30)

        add_Prod = tk.Button(self.parent, text="Agregar_producto")
        add_Prod.grid(row=0, column=3, padx=20, pady=30)


        prod_Name = ttk.Combobox(self.parent)
        prod_Name.grid(row=1, column=1,  sticky="ew", padx=20, pady=30)

        del_Prod = tk.Button(self.parent, text="Borrar_producto")
        del_Prod.grid(row=1, column=2, padx=20, pady=30)

    def add_Producto():
        pass

    pass



if __name__ == '__main__':
    root = tk.Tk()
    prod = prodcutos(root)
    root.mainloop()





















