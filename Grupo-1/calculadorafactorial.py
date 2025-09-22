def factorial(n):
    if n < 0:
        return none
    if n == 0 or n ==1:
        return 1
    resultado = 1
    for i in range(2, n+1):
        resultado*= i
    return resultado
    
numero = int(input("Ingrese un numero: "))
resultado = factorial(numero)
if resultado is none:
    print("No existe el factorial de numeros negativos")
else:
    print("El factorial de", numero, "es", resultado)