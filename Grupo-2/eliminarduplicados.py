#ENTRADA
lista = input("Ingrese elementos separados por comas: ")
#CONVERTIMOS EN LISTA LOS ELEMENTOS INGRESADOS
lista_original = [x.strip() for x in lista.split(",")]
#ELIMINAMOS LOS DUPLICADOS
lista_sin_duplicados = []
for elemento in lista_original:
    if elemento not in lista_sin_duplicados:
        lista_sin_duplicados.append(elemento)
#SALIDA
print(f"Lista original: {lista_original}")
print(f"Lista sin duplicados: {lista_sin_duplicados}")
