#ENTRADA 
palabra = input("Ingrese una palabra o frase: ").lower ()
#ELIMINAR ESPACIOS Y CARACTERES NO ALFABETICOS
palabra_limpia = "".join(c for c in palabra if c.isalpha())
#VERIFICAR SI ES IGUAL AL REVES
if palabra_limpia == palabra_limpia[::-1]:
    print("Es un palindromo.")
else:
    print("No es un palindromo.")