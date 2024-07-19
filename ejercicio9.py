'''
9. Encuentra el elemento más grande de una lista dada
x = [4, 6, 8, 24, 12, 2]
Expected Output:
24
'''

x = [4, 6, 8, 24, 12, 2]

def elemento_mas_grande(lista):
    return max(lista)

elemento_max = elemento_mas_grande(x)

print("El elemento más grande es:",elemento_max)