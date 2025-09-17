# Permite al usuario ingresar nombres de estudiantes y sus calificaciones. 
# Almacénalos en un diccionario y luego calcula 
# y muestra el promedio de calificaciones de toda la clase.

def agregar_nota(diccionario, nombre, nota):
    if nombre not in diccionario:
        diccionario[nombre] = []
    diccionario[nombre].append(nota)
    return diccionario

def calcular_promedio(diccionario):
    total_notas = 0
    total_estudiantes = 0
    for notas in diccionario.values():
        total_notas += sum(notas)
        total_estudiantes += len(notas)
    if total_estudiantes == 0:
        return 0
    return total_notas / total_estudiantes

notas_estudiantes = {}

while True:
    print("Bienvenido a tu gestor de notas. Selecciona una opción:")
    print("1. Ingresa el nombre del estudiante y su nota")
    print("2. Ver notas ingresadas")
    print("3. Terminar y calcular promedio")
    opcion = input()
    if opcion == '1':
        nombre = input("Ingresa el nombre del estudiante: ")
        try:
            nota = float(input("Ingresa la nota del estudiante (0-7): ").replace(',', '.'))
            if 0 <= nota <= 7:
                notas_estudiantes = agregar_nota(notas_estudiantes, nombre, nota)
                print(f"Nota {nota} agregada para {nombre}.")
            else:
                print("La nota debe estar entre 0 y 7. Inténtalo nuevamente.")
        except ValueError:
            print("Entrada inválida. Asegúrate de ingresar un dígito para la nota.")
    elif opcion == '2':
        if not notas_estudiantes:
            print("No hay notas ingresadas aún.")
        else:   
            print("Notas ingresadas:")
            for estudiante, notas in notas_estudiantes.items():
                print(f"  {estudiante}: {', '.join(str(n) for n in notas)}")
    elif opcion == '3':
        if not notas_estudiantes:
            print("No se han ingresado notas. No se puede calcular el promedio.")
            continue
        else:
            print("Calculando promedio y saliendo...")
        break
    else:
        print("Opción inválida, inténtalo nuevamente.")


promedio = calcular_promedio(notas_estudiantes)
print(f"El promedio de calificaciones de la clase es: {promedio:.2f}")