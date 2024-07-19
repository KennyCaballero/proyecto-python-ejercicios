'''
Escribir un programa que permita gestionar la base de datos de clientes de una empresa. Los clientes se guardarán en un diccionario en el que la clave de cada cliente será su DNI, y el valor será otro diccionario con los datos del cliente (nombre, dirección, teléfono, correo, preferente), donde preferente tendrá el valor True si se trata de un cliente preferente. El programa debe preguntar al usuario por una opción del siguiente menú: (1) Añadir cliente, (2) Eliminar cliente, (3) Mostrar cliente, (4) Listar todos los clientes, (5) Listar clientes preferentes, (6) Terminar. En función de la opción elegida el programa tendrá que hacer lo siguiente: 1. Preguntar los datos del cliente, crear un diccionario con los datos y añadirlo a la base de datos. 2. Preguntar por el DNI del cliente y eliminar sus datos de la base de datos. 3. Preguntar por el DNI del cliente y mostrar sus datos. 4. Mostrar lista de todos los clientes de la base datos con su DNI y nombre. 5. Mostrar la lista de clientes preferentes de la base de datos con su DNI y nombre. 6. Terminar el programa.
'''

clientes = {}

while True:
    opcion = input("""
Menú de opciones
1. Añadir cliente
2. Eliminar cliente
3. Mostrar cliente
4. Listar todos los cliente
5. Listar clientes preferentes
6. terminar
""")
    
    if opcion == "1":
        dni = input("Introduzca el DNI del cliente: ")
        nombre = input("Introduzca el nombre del cliente: ")
        direccion = input("Introduzca la dirección del cliente: ")
        telefono = input("Introduzca el telefono del cliente: ")
        correo = input("Introduzca el correo del cliente: ")
        preferente = input("Es un cliente preferente (S/N)? ").lower() == "s"

        clientes[dni] = {'nombre': nombre, 'direccion': direccion, 'telefono': telefono, 'correo': correo, 'preferente': preferente}

        print("Cliente agregado con éxito.")

    elif opcion == '2':
        dni = input("Introduzca el DNI del cliente: ")
        if dni in clientes:
            del clientes[dni]
            print("Cliente eliminado con éxito.")
        else:
            print("No se encontró el cliente con el DNI proporcionado.")

    elif opcion == '3':
        dni = input("Introduzca el DNI del cliente: ")
        if dni in clientes:
            cliente = clientes[dni]
            print(f"Nombre: {cliente['nombre']}\nDirección: {cliente['direccion']}\nTelefono: {cliente['telefono']}\nCorreo: {cliente['correo']}\nPreferente: {cliente['preferente']}")
        else:
            print("No se encontró el cliente con el DNI proporcionado")
    
    elif opcion == '4':
        for dni, cliente in clientes.items():
            print(f"DNI: {dni}, Nombre: {cliente['nombre']}")

    elif opcion == '5':
        clientes_preferente = [cliente for dni, cliente in clientes.items() if cliente['preferente']]
        for cliente in clientes_preferente:
            print(f"DNI: {dni}, Nombre: {cliente['nombre']}")
    
    if opcion == '6':
        break