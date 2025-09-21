#ENTRADA
palabra = input("Ingrese una palabra: ").lower()
#LISTA DE VOCALES Y CONSONANTES
consonantes = ["b","c","d","f","g","h","j","k","l","m","n","ñ","p","q","r","s","t","v","w","y","x","z"]
vocales = ["a", "e", "i", "o", "u"]
#CONTADORES
contador_vocales = 0
contador_consonantes = 0
#PROCESAMIENTO
for caracter in palabra:
    if caracter in vocales:
        contador_vocales += 1 
    elif caracter in consonantes:
        contador_consonantes += 1
#SALIDA       
print(f"Su palabra contiene {contador_vocales} vocales y {contador_consonantes} consonantes.")