'''
Ejercicio 7:
Escribe un programa que lea enteros del usuario y los almacene en una lista. Tu programa debería continuar leyendo valores hasta que el usuario introduzca 0. A continuación, debe mostrar todos los valores introducidos por el usuario (excepto el 0) en orden ascendente, con un valor que aparece en cada línea. Utilice el método sort o la función sorted para ordenar la lista.
'''
""" data = []


respuesta = int(input("Ingrese un numero entero (Ingrese 0 para detener el programa):  "))

while respuesta != 0:

    #agrega numeros a la lista
    data.append(respuesta)


    respuesta = int(input("Ingrese un numero entero (Ingrese 0 para detener el programa):  "))

#ordena lista
data.sort()

for elemento in data:
    print(elemento) """

'''
Ejercicio 8:
En este ejercicio, crearás un programa que lea palabras del usuario hasta que éste introduzca una línea en blanco. Después de que el usuario ingrese una línea en blanco, su programa debe mostrar cada palabra ingresada por el usuario exactamente una vez. Las palabras deben mostrarse en en el mismo orden en que fueron introducidas. Por ejemplo, si el usuario introduce: primero segundo primero tercero segundo entonces su programa debe mostrar: primero segundo tercero
'''

""" lista = []
palabra = input("Ingrese una palabra (espacio en blanco pata terminar): ")

while palabra != " ":
    #Verifica que no exista la palabra en la lista
    if palabra not in lista:
        lista.append(palabra)

    palabra = input("Ingrese una palabra (espacio en blanco pata terminar): ")

for elemento in lista:

    print(elemento) """

'''
Ejercicio 9:
Cree un programa que lea números enteros del usuario hasta que se introduzca una línea en blanco. Una vez que todos los números enteros han sido leídos tu programa debe mostrar todos los números negativos, seguidos por todos los ceros, seguidos por todos los números positivos. Dentro de cada grupo, los números deben mostrarse en el mismo orden en que fueron introducidos por el usuario. Por ejemplo, si el usuario ingresa los valores 3, -4, 1, 0, -1, 0, y -2 entonces su programa debe mostrar los valores -4, -1, -2, 0, 0, 3, y 1. Su programa debe mostrar cada valor en su propia línea.
'''

""" positivos = []
ceros = []
negativos =  []

num = input("Ingrese un numero (Espacio para terminar): ")

while num != " ":
    respuesta = int(num)

    if respuesta < 0:
        negativos.append(respuesta)
    elif respuesta == 0:
        ceros.append(respuesta)
    else:
        positivos.append(respuesta)

    num = input("Ingrese un numero (Espacio para terminar): ")

for elemento in negativos:
    print(elemento)

for elemento in ceros:
    print(elemento)

for elemento in positivos:
    print(elemento) """

'''
Ejercicio 10:
Al escribir una lista de elementos en inglés, normalmente se separan los elementos con comas. Además, normalmente se incluye la palabra "and" antes del último elemento, a menos que la lista sólo contenga un elemento. Considere las cuatro listas siguientes: apples manzanas y naranjas manzanas, naranjas y plátanos manzanas, naranjas, plátanos y limones Escriba un programa que solicite elementos al usuario y los almacene en una lista, se termina de ingresar los elementos de la lista cuando se igrese un espaio en blanco (" ").
El rpograma debe mostrar la palabra o palabras por "," o "y" segun corresponda a la cantidad de elementos ingresados a la lista. 
'''

""" data = []

respuesta = input("Ingrese una palabra (Espacio en blanco para terminar): ")

while respuesta != " ":

    #agrega elementos a la lista
    data.append(respuesta)

    respuesta = input("Ingrese una palabra (Espacio en blanco para terminar): ")

#identifica la cantidad de elementos
largo_data = len(data)

if largo_data == 0:
    print("La lista esta vacia")
if largo_data == 1:
    print(data[0])

for index in range(0, largo_data -2):
        
     respuesta = respuesta + data[index] + ", "
    
respuesta = respuesta + data[largo_data -2] + " y "
respuesta = respuesta + data[largo_data -1]
print(respuesta) """

'''
Ejercicio 11:
La librería estándar de Python incluye un método llamado count que determina cuántas veces aparece un valor específico en una lista. En este ejercicio, crearás una programa llamada countRange. Determinará y devolverá el número de elementos de una lista que son mayores o iguales a un valor mínimo y menores que un valor máximo. Tu programa tomará tres parámetros: la lista, el valor mínimo y el valor máximo. Devolverá un resultado entero mayor o igual que 0. 
'''

""" data = []

respuesta = input("Ingrese un numero (Espacio en blanco para terminar)")

while respuesta != " ":
    numero = int(respuesta)

    data.append(numero)


    respuesta = input("Ingrese un numero (Espacio en blanco para terminar): ")

minimo = int(input("Ingrese el numero minimo del rango: "))
maximo = int(input("Ingrese el numero maxino del rango: "))

contador = 0
for elemento in data:
    if elemento >= minimo and elemento <= maximo:
        contador += 1

print(f"La cantidad de elementos en el rango es: {contador}") """






