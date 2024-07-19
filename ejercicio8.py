'''
Genere una lista de Python de todos los números pares entre 4 y 30.
Salida esperada:
[4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28]
'''

def n_par(n):
    return n % 2 == 0

lista_pares = []
for elemento in range(1,31):
    if n_par(elemento):
        lista_pares.append(elemento)

print(lista_pares)