#ENTRADA
numeros = input("Ingresa numeros separados por comas: ")
#CONVERTIMOS EN LISTA
lista_numeros = [int(x.strip()) for x in numeros.split(",")]
print(f"Lista original: {lista_numeros}")
#BURBUJA
lista_ordenada = lista_numeros.copy()
n = len(lista_ordenada)
for i in range(n):
    for j in range(0, n - i - 1):
        if lista_ordenada[j] > lista_ordenada[j + 1]:
            lista_ordenada[j], lista_ordenada[j + 1] = lista_ordenada[j+1], lista_ordenada[j]
#SALIDA
print(f"Lista ordenada de menor a mayor: {lista_ordenada}")