'''
6. Escriba un programa para crear una función recursiva para calcular la suma de números del 0
al 10.
'''

def suma_recursiva(n):
    if n == 0:
        return 0
    else:
        return n + suma_recursiva(n -1)
    
resultado = suma_recursiva(10)

print(f"La suma de los numeros del 0 al 10 es {resultado}")