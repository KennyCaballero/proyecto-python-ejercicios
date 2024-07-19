'''
2. Escriba un programa que cree una función que acepte una cantidad variable de argumentos
e imprima sus valores.
'''

lista = []
flag = True

while flag:
    valor = input("Ingrese cualquier valor: ")
    lista.append(valor)
    flag = input("Desea agregar mas valores? S/N: ").lower() == 's'

def impresion(argumentos):
    for elemento in argumentos:
        print(elemento)

impresion(lista)