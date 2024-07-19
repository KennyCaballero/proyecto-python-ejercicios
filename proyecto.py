print("Bienvenido al programa de gestion de inventario".center(60,'-'))
cantidad = []
producto = []
precio = []


while True:
    print("""
    1. Añadir Producto
    2. Buscar Prodducto
    3. Modificar Producto
    4. Ver Producto
    5. Salir
    """)

    respuesta = int(input("Ingrese su opcion: "))
    if respuesta == 1:
        ac = int(input("Ingrese la Cantidad de su Producto: "))
        apro = input("Ingrese el Nombre de su Producto: ")
        apre = int(input("Ingrese el Precio de su Producto: "))

        cantidad.append(ac)
        producto.append(apro)
        precio.append(apre)
    elif respuesta == 2:
        buscador = input("Ingrese el Nombre del Producto: ")
        posicion = producto.index(buscador)
        print(f"La Cantidad del Producto es: {cantidad[posicion]}")
        print(f"EL Nombre del Producto es: {producto[posicion]}")
        print(f"El precio del producto es: {precio[posicion]}$")

    elif respuesta == 3:
        buscador = input("Ingrese el Nombre del Producto: ")
        posicion = producto.index(buscador)
        ac = int(input("Ingrese la Cantidad de su Producto: "))
        apro = input("Ingrese el Nombre de su Producto: ")
        apre = int(input("Ingrese el Precio de su Producto: "))
        cantidad[posicion] = ac
        producto[posicion] = apro
        precio[posicion] = apre
        
    elif respuesta == 4:
        print(f"La Cantidad es: {cantidad}")
        print(f"EL Nombre es: {producto}")
        print(f"EL Precio es: {precio}$")
    else:
        break
