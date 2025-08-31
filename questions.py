import random
import sys    #para usar exit a partir de linea 38

# Se crea variable para contabilizar puntaje
puntaje = 0.0

# Preguntas para el juego
questions = [
    "¿Qué función se usa para obtener la longitud de una cadena en Python?",
    "¿Cuál de las siguientes opciones es un número entero en Python?",
    "¿Cómo se solicita entrada del usuario en Python?",
    "¿Cuál de las siguientes expresiones es un comentario válido en Python?",
    "¿Cuál es el operador de comparación para verificar si dos valores son iguales?",
]
#Respuestas posibles para cada pregunta, en el mismo orden que las preguntas
answers = [
    ("size()", "len()", "length()", "count()"),
    ("3.14", "'42'", "10", "True"),
    ("input()", "scan()", "read()", "ask()"),
    (
        "// Esto es un comentario",
        "/* Esto es un comentario */",
        "-- Esto es un comentario",
        "# Esto es un comentario",
    ),
    ("=", "==", "!=", "==="),
]
#Índice de la respuesta correcta para cada pregunta, el el mismo orden que las preguntas
correct_answers_index = [1, 2, 0, 3, 1]

# Se combina las listas en una
all_questions = list(zip(questions, answers, correct_answers_index))


# Se elegien 3 prguntas al azar
questions_to_ask = random.sample(all_questions, k=3)

# El usuario deberá contestar 3 preguntas
for questions, answers, correct_answers_index in questions_to_ask:
    # Se muestra la pregunta y las respuestas posibles
    print ("\n"+ questions)
    
    for i, answer in enumerate(answers):
        print(f"{i + 1}. {answer}")

# El usuario tiene 2 intentos para responder correctamente
    for intento in range(2):
        try:
            user_answer = int(input("Respuesta: ")) - 1
        except ValueError:
            print ("Respuesta invalida")
            sys.exit(1)
        # Se verifica que el numero este dentro del rango
        if not 0 <= user_answer < len(answers):
            print("Respuesta no válida")
            sys.exit(1)
            # Se verifica si la respuesta es correcta
        if user_answer == correct_answers_index:
            print("¡Correcto!")
            puntaje += 1
            break
    else:
        #Si el usuario no responde correctamente después de 2 intentos,
        # se muestra la respuesta correcta
        print("Incorrecto. La respuesta correcta es:")
        print(answers[correct_answers_index])
        puntaje -= 0.5

print (f'El puntaje obtenido ha sido de : {puntaje} puntos')
# Se imprime un blanco al final de la pregunta
print()