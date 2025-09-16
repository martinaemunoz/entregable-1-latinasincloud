# Crea un programa que funcione como una agenda. 
# Debe permitir al usuario añadir un contacto (nombre, teléfono), 
# buscar un contacto por su nombre y eliminar un contacto. 
# Usa un diccionario para almacenar la agenda.

def anadir_contacto(agenda, nombre, telefono):
    if nombre not in agenda:
        agenda[nombre] = telefono
        print("Contacto añadido exitosamente")
    else:
        print("El contacto ya existe, inténtalo nuevamente")
    return agenda

def buscar_contacto(agenda, nombre):
    nombre_buscar = nombre.strip().lower()
    for nombre_contacto, busqueda in agenda.items():
        if nombre_contacto.strip().lower() == nombre_buscar:
            return busqueda
    return "Contacto no encontrado, inténtalo nuevamente"
    
def eliminar_contacto(agenda, nombre):
    if nombre in agenda:
        confirmar = input(f"Estás seguro que deseas eliminar el contacto {nombre}? (s/n): ")
        if confirmar.lower() == 's':
            del agenda[nombre]
            print("Contacto eliminado exitosamente")
        elif confirmar.lower() == 'n':
            print("El contacto ha sido eliminado.")
        else:
            print("Opción inválida, debes ingresar s para sí o n para no.")
    else:
        print("El contacto no existe, inténtalo nuevamente")
    return agenda

agenda = {}

while True:
    print("Bienvenido a tu agenda de contactos. Selecciona una opción:")
    print("1. Añadir contacto")
    print("2. Buscar contacto")
    print("3. Eliminar contacto")
    print("4. Salir")
    opcion = input()
    
    if opcion == '1':
        nombre = input("Ingresa el nombre del contacto: ")
        telefono = input("Ingresa el teléfono del contacto: ")
        if not telefono.isdigit() or len(telefono) != 8:
            print("El teléfono debe contener solo números y tener exactamente 8 dígitos. Inténtalo nuevamente.")
        else:
            agenda = anadir_contacto(agenda, nombre, telefono)
        
    elif opcion == '2':
        nombre = input("Ingresa el nombre del contacto a buscar: ")
        numero = buscar_contacto(agenda, nombre)
        print(f"El teléfono del contacto {nombre} es: {numero}")
        
    elif opcion == '3':
        nombre = input("Ingresa el nombre del contacto a eliminar: ")
        agenda = eliminar_contacto(agenda, nombre)
        
    elif opcion == '4':
        print("Saliendo de la agenda de contactos.")
        break
        
    else:
        print("Opción no válida, inténtalo nuevamente.")
