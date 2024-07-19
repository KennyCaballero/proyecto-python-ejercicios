lista_prueba=[8, 2, 3, 0, 7 ]

def suma_lista(lista):
    suma_total = 0
    for elemento in lista:
        suma_total += elemento

    return suma_total

suma_resultado = suma_lista(lista_prueba)

print(f"La suma de la lista es: {suma_resultado}")