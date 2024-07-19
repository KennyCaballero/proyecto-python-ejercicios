'''
3. Escriba un programa para crear una función que pueda aceptar dos variables y calcular su
suma y resta. Además, debe devolver tanto la suma como la resta en una sola llamada de
retorno.
'''

def suma_y_resta(numero1,numero2):
    suma = numero1 + numero2
    resta = numero1 - numero2

    return suma, resta

num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))

resultado_suma, resultado_resta = suma_y_resta(num1,num2)


print(f"La suma es: {resultado_suma}")
print(f"La resta es: {resultado_resta}")