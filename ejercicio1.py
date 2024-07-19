'''
1. Crea un programa que crea una función que toma dos argumentos (nombre y edad) e
imprime sus valores.
'''

def datos(nombre,edad):
    print(f"Nombre: {nombre}")
    print(f"Edad: {edad}")

nombre_usuario: input("Ingrese su nombre: ")
edad_usuario: input("Ingrese su edad: ")


datos(nombre_usuario, edad_usuario)