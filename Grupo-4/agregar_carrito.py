# 017 Muestra al usuario los productos disponibles 
# y permite que seleccione productos para agregarlos 
# a una lista que simulará ser un "carrito de compras".

from definir_productos import claveProductos
import unicodedata

def normalizar(seleccion):
    return ''.join(
        char for char in unicodedata.normalize('NFD', seleccion) # separa los caracteres base de sus tildes
        if unicodedata.category(char) != 'Mn' # elimina los caracteres de marca (tildes)
    ).lower().strip()

def agregarCarrito():
    carrito = []
    input("\n ¡Tienes un 10% de descuento por compras mayores a $9990! Presiona enter para continuar...")
    while True:
        print("\n Productos disponibles:")
        for producto, precio in claveProductos.items():
            print(f"  {producto}: ${precio}")
        productoSeleccionado = input("\n Ingresa el nombre del producto que deseas agregar al carrito (o 'salir' para finalizar): ").strip().lower()
        productoSeleccionado = normalizar(productoSeleccionado)
        
        if productoSeleccionado == 'salir':
            print("\n Finalizando la compra. Nos vemos pronto!")
            break

        encontrado = None
        for producto in claveProductos.keys():
            if normalizar(producto) == productoSeleccionado: # compara sin importar mayúsculas, minúsculas o tildes
                encontrado = producto
                break

        if encontrado:
            carrito.append(encontrado)
            print(f"\n Producto '{encontrado}' agregado al carrito.")
        else:
            print("\n Producto no encontrado, inténtalo nuevamente.")

    return carrito