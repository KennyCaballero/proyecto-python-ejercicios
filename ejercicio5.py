'''
Cree una función externa que acepte dos parámetros, a y b
• Cree una función interna dentro de la función externa que calculará la suma de a y b
• Al final, la función externa agregará 5 a la variable que almacena la suma y lo devolverá
'''

def funcion_externa(a, b):
    def funcion_interna():
        return a + b
    suma = funcion_interna()
    return suma + 5
    

num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))

print(funcion_externa( num1, num2))