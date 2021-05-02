def pedirNumeroEntero():
    correcto = False
    num = 0    

    while (not correcto):
        try:
            num = int(input("Introduce un numero entero: "))
            correcto = True
        except ValueError:
            print('Error, introduce un numero entero')

    return num

folio = 0
salir = False
opcion = 0
count = 0
import datetime
import time
Separador = ("*" * 20) + "\n"
fechaactual = datetime.date.today()


print(fechaactual)

while not salir:

    print("1. Registrar una venta")
    print("2. consultar una venta")
    print("3. Reporte por fecha")
    print("4 Salir")

    print("Elige una opcion")

    opcion = pedirNumeroEntero()
    import sqlite3

    con = sqlite3.connect('mydatabase.db')
    cursorObj = con.cursor()
    cursorObj.execute(
        "CREATE TABLE IF NOT EXISTS registros(folio INT PRIMARY KEY , fecha, descripcion, cantidad, precio)")
    
    cursorObj = con.cursor()
    cursorObj.execute('SELECT folio FROM registros')
    rows = cursorObj.fetchall()
    cont = 0

    
    for row in rows:        
        cont = row[0] + 1
    if opcion == 1:
        
        desc=input("Descripción de el artículo: ""\n")
        piezas=int(input("Cantidad de piezas vendidas: ""\n"))
        precio=float(input("Precio de venta: ""\n"))       
        total=piezas*precio
        folio = cont
        "import sqlite3"
        "con = sqlite3.connect('mydatabase.db')"
        "def sql_insert(con, entities):"
        cursorObj = con.cursor()
        cursorObj.execute("INSERT INTO registros VALUES('"+str(folio)+"', '"+str(fechaactual)+"', '"+desc+"', '"+str(piezas)+"', '"+str(precio)+"')")
        con.commit()

        print("Total a Pagar: "+str(total))
    elif opcion == 2:
        opt=int(input("ID de venta a buscar: ""\n"))
        cursorObj = con.cursor()
        cursorObj.execute("SELECT * FROM registros WHERE folio = '"+str(opt)+"'")
        rows = cursorObj.fetchall()
  
        for row in rows:        
            print(row)

    if opcion == 3:
        opt=input("Reporte por fechas de venta a buscar: ""\n")
        cursorObj = con.cursor()
        cursorObj.execute("SELECT * FROM registros WHERE fecha = '"+str(opt)+"'")
        rows = cursorObj.fetchall()

        for row in rows:        
            print(row)


    elif opcion == 4:
        salir = True
    else:
        print("Introduce un numero entre 1 y 4")

print("Fin")