from tkinter import Tk, Button, Frame, Text, ttk, Label, END, messagebox
from productos import prodcutos
from funciones_db import *
from excel_gen import excel_Gen


class p_Screen(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initilize()
        self.resumen()
    
    def initilize(self):
        self.frame = Frame(self.parent, width=500, height=300)
        self.frame.grid(row=0, column=0)

        self.frame2 = Frame(self.frame)#, bg = 'white')
        self.frame2.grid(row=2, column=0, padx=20, pady=5, columnspan = 2)

        self.venta_Prod = ttk.Combobox(self.frame, state="readonly")
        tabla = prod_Select()
        self.venta_Prod["values"] = [x[1] for x in tabla]
        self.venta_Prod.grid(row=0, column=0, padx=20, pady=15) #, padx=20, pady=30

        self.venta_Num = ttk.Combobox(self.frame)
        self.venta_Num["values"] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.venta_Num.grid(row=0, column=1)

        self.boton_sumVenta = Button(self.frame2, text='Sumar venta', command=self.venta)
        self.boton_sumVenta.grid(row=0, column=0, padx=20, pady=5)

        self.boton_sellDelete = Button(self.frame2, text='Restar venta', command=self.sell_Delete) #Aun no resta venta
        self.boton_sellDelete.grid(row=0, column=1, padx=20, pady=5)

        self.label = Label(self.frame, text="Resumen")
        self.label.grid(row=3, column=0, padx=20, pady=30)

        self.outputtxt = Text(self.frame, height = 10, width = 25, bg = "light yellow")
        self.outputtxt.grid(row=3, column=1, padx=20, pady=30)

        self.boton_archivo = Button(self.frame, text='Añadir productos', command = self.add_Products)
        self.boton_archivo.grid(row=4, column=0, padx=20, pady=30)

        self.boton_ganancias = Button(self.frame, text='Ganancias', command = self.ganancias_text)
        self.boton_ganancias.grid(row=4, column=1, padx=20, pady=30)

        self.boton_genExcel = Button(self.frame, text='Generar_excel', command = self.Generar_excel)
        self.boton_genExcel.grid(row=5, column=0, padx=20, pady=30, columnspan = 3)

  
    def venta(self):
        prod_id = self.venta_Prod.get()
        sell_Num = self.venta_Num.get()
        if prod_id == None or prod_id == '' or sell_Num == None or sell_Num == '':
            print('No has llenado todos los campos')
        else:
            ventas(prod_id, sell_Num)
        self.resumen()

    def resumen(self):
        resumen = prod_Resum()
        self.outputtxt.delete('1.0', END)
        for producto in resumen:
            self.outputtxt.insert(END, producto[3] + ' ' + '(' + str(producto[4]) + ')' + '\n')    

    def sell_Delete(self):
        prod_id = self.venta_Prod.get()
        sell_Num = self.venta_Num.get()
        del_Product(prod_id, 't_venta')
        self.resumen()  

    def add_Products(self):
        def on_closing():
            if messagebox.askokcancel("Quit", "Do you want to quit?"):
                root.destroy()
                print('listo')
                tabla = prod_Select()
                self.venta_Prod["values"] = [x[1] for x in tabla]


        root = Tk()
        app = prodcutos(root)
        root.protocol("WM_DELETE_WINDOW", on_closing)              
        root.mainloop()
        
    def ganancias_text(self):
        tabla = ganancias()
        self.outputtxt.insert(END, 'Ganancias: ' + str(sum([x[0]*x[1] for x in tabla])) + '\n')    

    def Generar_excel(self):
        root = Tk()
        excel_Gen(root)
        root.mainloop()        



if __name__ == '__main__':
    root = Tk()
    root.title('Venta')
    p_Screen = p_Screen(root)
    root.mainloop()
















