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


salir = False
opcion = 0
count = 0
registros=[]

while not salir:

    print("1. Registrar una venta")
    print("2. consultar una venta")
    print("3. Salir")

    print("Elige una opcion")

    opcion = pedirNumeroEntero()
    
    if opcion == 1:
        count += 1
        desc=input("Descripción de el artículo: ""\n")
        piezas=int(input("Cantidad de piezas vendidas: ""\n"))
        precio=float(input("Precio de venta: ""\n"))       
        total=piezas*precio 
        registros.append([count,desc,piezas,precio,total])
        

        print("Total a Pagar: "+str(total))
    elif opcion == 2:
        opt=int(input("ID de venta a buscar: ""\n"))
        for vc in registros:
            if vc[0] == opt:
                print(vc)

    elif opcion == 3:
        salir = True
    else:
        print("Introduce un numero entre 1 y 3")

print("Fin")