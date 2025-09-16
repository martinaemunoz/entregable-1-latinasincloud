# Dado un párrafo de texto, cuenta la frecuencia de aparición de cada palabra 
# y almacena el resultado en un diccionario.

def contar_frecuencia_palabras(parrafo):
    # Eliminar signos de puntuación y convertir a minúsculas
    signos = ".,;:!?\"'()[]{}"
    for signo in signos:
        parrafo = parrafo.replace(signo, "")
    parrafo = parrafo.lower()
    # Dividir el párrafo en palabras
    palabras = parrafo.split()
    # Contar la frecuencia de cada palabra
    frecuencia = {}
    for palabra in palabras:
        if palabra in frecuencia:
            frecuencia[palabra] += 1
        else:
            frecuencia[palabra] = 1
    return frecuencia

while True:
    print("Ingresa un párrafo de texto:")
    parrafo = input()
    if not parrafo.strip():
        print("No se ingresó ningún texto, inténtalo nuevamente")
    else:
        frecuencia_palabras = contar_frecuencia_palabras(parrafo)
        print("Frecuencia de palabras:", frecuencia_palabras)
        break