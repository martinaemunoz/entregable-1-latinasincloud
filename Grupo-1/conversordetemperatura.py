def celsius_a_fahrenheit(c):
    return( c * 9/5) + 32
def fahrenheit_a_celsius(f):
    return (f - 32) * 5/9

c = float(input("Ingresa la temperatura en C°: "))
print(c , "°C equivale a", celsius_a_fahrenheit(c), "°F")

f = float(input("Ingresa temperatura en °F: "))
print(f, "°F equivale a", fahrenheit_a_celsius(f), "°C")
