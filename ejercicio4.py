'''
4. Escriba un programa para crear una función usando las siguientes condiciones.
• Debe aceptar el nombre y el salario del empleado y mostrar ambos.
• Si falta el salario en la llamada de función, asigne el valor predeterminado 9000 al
salario
'''

def mostrar_empleado(nombre, salario=9000):
    print(f"Nombre del empleado: {nombre}")
    print(f"Salario del empleado: {salario}")


nombre_empleado = input("Ingrese el nombre del empleado: ")
salario_empleado = input("Ingrese el salario del empleado (o presione Enter para usar el valor predeterminado): ")


if salario_empleado:
    mostrar_empleado(nombre_empleado, float(salario_empleado))
else:
    mostrar_empleado(nombre_empleado)



