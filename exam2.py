mes = input("Ingrese el mes: ").lower()
dia = int(input("Ingrese el dia: "))

if (mes == "marzo" and 20 <= dia <= 31) or (mes == "abril") or (mes == "mayo") or (mes == "junio" and dia <= 20):
    estacion = "Primavera"

elif (mes == "junio" and dia > 20) or (mes == "julio") or (mes == "agosto") or (mes == "septiembre" and dia <= 21):
    estacion = "Verano"

elif (mes == "septiembre" and dia > 21) or (mes == "octubre") or (mes == "noviembre") or (mes == "diciembre" and dia <= 20):
    estacion = "Otoño"

elif (mes == "diciembre" and dia > 20) or (mes == "enero") or (mes == "febrero") or (mes == "marzo" and dia <= 19):
    estacion = "Invierno"

else:
    estacion = "Fecha invalida"

print(f"La estacion correspondiente a {mes} {dia} es: {estacion}")