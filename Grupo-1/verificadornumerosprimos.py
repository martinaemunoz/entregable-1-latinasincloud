def es_primo(num):
    if num <= 1:
        return false
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return false
    return true
    
n = int(input("ingrese un número:"))
if es_primo(n):
    print(n, "es primo")
else:
    print(n, "no es primo")