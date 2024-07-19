def gestion_inventario():
    # Inicializar el inventario como un diccionario vacío
    inventario = {}

    while True:
        # Menú de opciones
        print("\n1. Agregar producto")
        print("2. Mostrar stock")
        print("3. Buscar producto")
        print("4. Disminuir producto")
        print("5. Sustituir producto")
        print("6. Eliminar producto")
        print("7. Realizar venta")
        print("8. Salir")

        opcion = input("Selecciona una opción (1/2/3/4/5/6/7/8): ")

        if opcion == "1":
            # Agregar producto
            nombre_producto = input("Ingrese el nombre del producto: ")
            cantidad_producto = int(input("Ingrese la cantidad de unidades: "))
            precio_producto = float(input("Ingrese el precio unitario del producto: "))

            # Convertir el nombre a minúsculas
            nombre_producto = nombre_producto.lower()

            # Actualizar el inventario
            if nombre_producto in inventario:
                inventario[nombre_producto]['cantidad'] += cantidad_producto
            else:
                inventario[nombre_producto] = {'cantidad': cantidad_producto, 'precio': precio_producto}

        elif opcion == "2":
            # Mostrar stock
            print("Stock actual:")
            total_valor = 0
            for producto, info in inventario.items():
                cantidad = info['cantidad']
                precio = info['precio']
                valor_producto = cantidad * precio
                total_valor += valor_producto

                if cantidad < 12:
                    print(f"{producto}: {cantidad} unidades - Precio unitario: S/ {precio:.2f} - Valor total: S/ {valor_producto:.2f} - ¡Alerta! Stock bajo (menos de 12 unidades).")
                else:
                    print(f"{producto}: {cantidad} unidades - Precio unitario: S/ {precio:.2f} - Valor total: S/ {valor_producto:.2f}")

            print(f"Valor total del inventario: S/ {total_valor:.2f}")

        elif opcion == "3":
            # Buscar producto
            nombre_buscar = input("Ingrese el nombre del producto a buscar: ")
            nombre_buscar = nombre_buscar.lower()

            if nombre_buscar in inventario:
                info = inventario[nombre_buscar]
                print(f"{nombre_buscar} está en stock: {info['cantidad']} unidades - Precio unitario: S/ {info['precio']:.2f}")
                if info['cantidad'] < 12:
                    print(f"¡Alerta! {nombre_buscar} tiene un stock bajo (menos de 12 unidades).")
            else:
                print(f"{nombre_buscar} no se encuentra en el inventario")

        elif opcion == "4":
            # Disminuir producto
            nombre_disminuir = input("Ingrese el nombre del producto a disminuir: ")
            cantidad_disminuir = int(input("Ingrese la cantidad de unidades a restar: "))
            nombre_disminuir = nombre_disminuir.lower()

            if nombre_disminuir in inventario:
                if cantidad_disminuir <= inventario[nombre_disminuir]['cantidad']:
                    inventario[nombre_disminuir]['cantidad'] -= cantidad_disminuir
                    print(f"Se han restado {cantidad_disminuir} unidades de {nombre_disminuir}")
                    if inventario[nombre_disminuir]['cantidad'] == 0:
                        print(f"¡Alerta! {nombre_disminuir} está fuera de stock.")
                    elif inventario[nombre_disminuir]['cantidad'] < 12:
                        print(f"¡Alerta! {nombre_disminuir} tiene un stock bajo (menos de 12 unidades).")
                else:
                    print("No hay suficientes unidades disponibles.")
            else:
                print(f"{nombre_disminuir} no se encuentra en el inventario")

        elif opcion == "5":
            # Sustituir producto
            nombre_actual = input("Ingrese el nombre del producto a sustituir: ")
            nombre_nuevo = input("Ingrese el nuevo nombre del producto: ")
            cantidad_nueva = int(input("Ingrese la cantidad de unidades del nuevo producto: "))
            precio_nuevo = float(input("Ingrese el precio unitario del nuevo producto: "))
            nombre_actual = nombre_actual.lower()
            nombre_nuevo = nombre_nuevo.lower()

            if nombre_actual in inventario:
                info = inventario.pop(nombre_actual)
                inventario[nombre_nuevo] = {'cantidad': cantidad_nueva, 'precio': precio_nuevo}
                print(f"{nombre_actual} ha sido sustituido por {nombre_nuevo} con {cantidad_nueva} unidades y precio S/ {precio_nuevo:.2f}")
                if cantidad_nueva < 12:
                    print(f"¡Alerta! {nombre_nuevo} tiene un stock bajo (menos de 12 unidades).")
            else:
                print(f"{nombre_actual} no se encuentra en el inventario")

        elif opcion == "6":
            # Eliminar producto
            nombre_eliminar = input("Ingrese el nombre del producto a eliminar: ")
            nombre_eliminar = nombre_eliminar.lower()

            if nombre_eliminar in inventario:
                del inventario[nombre_eliminar]
                print(f"{nombre_eliminar} ha sido eliminado del inventario")
            else:
                print(f"{nombre_eliminar} no se encuentra en el inventario")

        elif opcion == "7":
            # Realizar venta
            nombre_venta = input("Ingrese el nombre del producto a vender: ")
            cantidad_venta = int(input("Ingrese la cantidad de unidades a vender: "))
            nombre_venta = nombre_venta.lower()

            if nombre_venta in inventario:
                if cantidad_venta <= inventario[nombre_venta]['cantidad']:
                    precio_unitario = inventario[nombre_venta]['precio']
                    total_venta = cantidad_venta * precio_unitario
                    inventario[nombre_venta]['cantidad'] -= cantidad_venta
                    print(f"Venta realizada: {cantidad_venta} unidades de {nombre_venta} por un total de S/ {total_venta:.2f}")
                    if inventario[nombre_venta]['cantidad'] == 0:
                        print(f"¡Alerta! {nombre_venta} está fuera de stock.")
                    elif inventario[nombre_venta]['cantidad'] < 12:
                        print(f"¡Alerta! {nombre_venta} tiene un stock bajo (menos de 12 unidades).")
                else:
                    print("No hay suficientes unidades disponibles para la venta.")
            else:
                print(f"{nombre_venta} no se encuentra en el inventario")

        elif opcion == "8":
            # Salir del programa
            print("¡Hasta luego!")
            break

        else:
            print("Opción no válida. Por favor, selecciona una opción válida.")

# Llamada a la función para iniciar el programa
gestion_inventario()
