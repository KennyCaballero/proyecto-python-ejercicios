banco_preguntas = ['b', 'b', 'c','a','c']
respuesta_usuario = []
puntuacion = 0

print(
    "Ingrese las respuestas a las siguientes preguntas opciones: 'a', 'b', 'c'" 
)

for i in range(5):
    respuesta = input(f"Pregunta {i + 1}: ")
    respuesta_usuario.append(respuesta)

    if respuesta == banco_preguntas[i]:
        puntuacion += 1
    else:
        print("Respuesta Incorrecta")
        
print(f"Puntuacion obtenida: {puntuacion} / 5")