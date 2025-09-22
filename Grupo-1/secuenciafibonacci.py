def fibonacci(n):
    secuencia = [0,1]
    while len(secuencia) < n:
        secuencia.append(secuencia[-1] + secuencia[-2])
    return secuencia[:n]

cantidad = int(input("¿Cuantos numeros de la secuencia fibonacci quieres generar?"))

print ("Secuencia de Fibonacci:", fibonacci(cantidad))