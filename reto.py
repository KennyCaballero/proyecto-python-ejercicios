data = []

respuesta = int(input("Ingrese un entero (ingrese 0 para detenerse): "))

while respuesta != 0:

    data.append(respuesta)

    respuesta = int(input("Ingrese un entero (ingrese 0 para detenerse): "))

largo_data = len(data)

for i in range(largo_data -1):
    for j in range(0, largo_data -i -1):
        if data[j] > data[j + 1]:
            data[j], data[j + 1] = data[j + 1], data[j]

print("Valores introducidos en orden ascendente:")
for elemento in data:
    print(elemento)