import sqlite3

def cursor():
    """Devuelve un cursor conectado a productos.db para realizar las operacion"""
    db_Con = sqlite3.connect('productos.db')
    return db_Con.cursor(), db_Con

def prod_Select():
    cursor_Insert, coneccion_Insert = cursor()
    cursor_Insert.execute("CREATE TABLE IF NOT EXISTS productos (pord_ID INT PRIMARY KEY AUTOINCREMENT, nombre VARCHAR(20), precio INT)")
    cursor_Insert.execute("SELECT * FROM productos")
    tabla = cursor_Insert.fetchall()
    return tabla

def add_Prod(name, price):
    cursor_Insert, coneccion_Insert = cursor()
    cursor_Insert.execute("CREATE TABLE IF NOT EXISTS productos (pord_ID INT PRIMARY KEY AUTOINCREMENT, nombre VARCHAR(20), precio INT)")
    cursor_Insert.execute("INSERT INTO productos VALUES (?, ?)", (name, price))
    print('Se agrego el producto %s con precio %s'%(name, price))

def ventas(prod_id, sell_Num):
    """Esta función debe agregar la venta a la base de datos en la tabla ventas"""
    cursor_Insert, coneccion_Insert = cursor()
    cursor_Insert.execute("CREATE TABLE IF NOT EXISTS ventas (dia VARCHAR(30), hora VARCHAR(30), prod_id INT, sell_Num INT)")
    table_Insert((prod_id, sell_Num), funcion = 'ventas')
    print('Se agregó la venta de %s de %s ´s '%(sell_Num, prod_id))

def inicio():
    """Esta funcion crea la base de datos de 'productos' """
    cursor_Insert, coneccion_Insert = cursor()
    cursor_Insert.execute("CREATE TABLE IF NOT EXISTS productos (pord_ID INT PRIMARY KEY AUTOINCREMENT, nombre VARCHAR(20), precio INT)")


def table_Insert(lista, funcion = 'ventas'):
    """Agrega a una tabla 'funcion' la lista de valores 'lista'"""
    cursor_Insert, coneccion_Insert = cursor()
    if funcion == 'ventas':
        cursor_Insert.execute('INSERT INTO ventas VALUES (DATE(), TIME(), ?, ?)', lista)
    elif funcion == 'nose':
        pass
    #Otros elif

    coneccion_Insert.commit()
        




























