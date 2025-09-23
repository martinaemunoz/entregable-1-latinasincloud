# Crea un diccionario que funcione como un traductor de español a inglés. 
# Debe contener al menos 10 palabras 
# y permitir al usuario ingresar una palabra en español para obtener su traducción.

def traducir_palabra(diccionario, palabra):
    palabra_normalizada = palabra.strip().lower()
    if palabra_normalizada in diccionario:
        return diccionario[palabra_normalizada]
    
diccionario_traduccion = {
    "hola": "hello",
    "chao": "goodbye",
    "gracias": "thank you",
    "por favor": "please",
    "perro": "dog",
    "gato": "cat",
    "casa": "house",
    "libro": "book",
    "colegio": "school",
    "comida": "food"
}

while True:
    print("Bienvenido a tu traductor de español a inglés.")
    print("Ingresa una palabra en español para traducir al inglés (o 'salir' para salir del traductor):")
    palabra = input()
    if palabra.strip().lower() == 'salir':
        print("Saliendo del traductor. Nos vemos pronto!")
        break
    elif palabra.strip().lower() in diccionario_traduccion:
        traduccion = traducir_palabra(diccionario_traduccion, palabra)
        print(f"La traducción al inglés de '{palabra}' es: {traduccion}")
    elif palabra.strip().lower() not in diccionario_traduccion:
        print("Palabra no encontrada en el diccionario, inténtalo nuevamente")
    elif not palabra.strip():
        print("No se ingresó ninguna palabra, inténtalo nuevamente")
