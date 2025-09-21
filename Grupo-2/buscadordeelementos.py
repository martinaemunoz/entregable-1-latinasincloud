#ENTRADA
lista1 = input("Ingrese los primeros elementos separados por comas: ")
#CONVERTIMOS EN LISTA LOS PRIMEROS ELEMENTOS
primera_lista = [x.strip() for x in lista1.split(",")]
lista2 = input("Ingrese los segundos elementos separados por comas: ")
#CONVERTIMOS EN LISTA LOS SEGUNDOS ELEMENTOS
segunda_lista = [x.strip() for x in lista2.split(",")]
#ENCONTRAMOS ELEMENTOS EN COMUN
comunes = []
for elemento in primera_lista:
    if elemento in segunda_lista and elemento not in comunes:
        comunes.append(elemento)
#SALIDA
print(f"Lista 1: {primera_lista}")
print(f"Lista 2: {segunda_lista}")
print(f"Elementos en comun: {comunes}")
