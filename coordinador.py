import sqlite3



class iniciadora():
  def __init__(self):
    self.conexion = None
    self.list_Producto = []

  def lista_de_productos(self):    
    cursor = conecta_base()
    cursor.execute("""SELECT PRODUCTOS FROM productos""")
    self.list_Producto = cursor.fetchall()   
    return lista_productos
  
  def agregar_producto():
    producto_Nuevo = input('Introduce el nombre del nuevo producto')
    precio_producto_Nuevo = intput('Introduce el nombre del nuevo producto')

    producto_to_dab = (producto_Nuevo, precio_producto_Nuevo)
    cursor = conecta_base()
    cursor.execute("INSERT INTO productos VALUES (?, ?)", producto_to_dab)

    cursor.execute("""SELECT PRODUCTOS FROM productos""")
    self.list_Producto = cursor.fetchall()   

    return lista_productos

  def conecta_base():
    self.conexion = sqlite3.connect('productos.db')
    cursor = self.conexion.cursor()
    cursor.execute("""CREATE TABLE productos IF NOT EXIST 
                    (ID_PROD INT PRIMARY KEY  AUTO_INCREMENT, 
                    PRODUCTOS VARCHAR(15),
                    PRECIO INT)""")
    return cursor
  def desconectar_base():
    self.conexion.close()
    #return conexion























