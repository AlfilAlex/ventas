from tkinter import Tk, Button, Frame, Text, ttk, Label, Entry, END
from funciones_db import *

class excel_Gen(Frame):
    """Esta clase abre una pestaña que permite posteriormente
       generar un excel de los productos vendidos determiando dia"""
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initialize()

    def initialize(self):
        self.parent.title("Generar_Excel")
        self.prod_Name_list = ttk.Combobox(self.parent)
        days_tb = self.get_Days()
        self.prod_Name_list["values"] = [x for x in days_tb]
        self.prod_Name_list.grid(row=0, column=0,  sticky="ew", padx=20, pady=30)

        self.gen_Excel = Button(self.parent, text="Generar_Excel", command = self.generar_Excel)
        self.gen_Excel.grid(row=1, column=0, padx=20, pady=30, columnspan = 2)

    def get_Days(self):
        days = excel_Dias()
        list_Days = list(set([day[0] for day in days]))
        return list_Days

    def generar_Excel(self):
        day = self.prod_Name_list.get()
        data = excel_Data(day)
        lista_Venta = [''.join(str(x)).replace('(', '').replace(')', '').replace('"', '').replace(' ', '') for x in data]
        lista_Venta.insert(0, 'Indice,Dia,Hora,Producto,Cantidad')
        with open('venta.csv', 'a') as documento:
            for venta in lista_Venta:
                documento.write(venta + '\n')


if __name__ == '__main__':
    root = Tk()
    prod = excel_Gen(root)
    root.mainloop()





















