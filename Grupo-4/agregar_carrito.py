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
    while True:
        print("Productos disponibles:")
        for producto, precio in claveProductos.items():
            print(f"  {producto}: ${precio}")
        
        productoSeleccionado = input("Ingresa el nombre del producto que deseas agregar al carrito (o 'salir' para finalizar): ").strip().lower()
        productoSeleccionado = normalizar(productoSeleccionado)
        
        if productoSeleccionado == 'salir':
            print("Finalizando la compra. Nos vemos pronto!")
            break

        encontrado = None
        for producto in claveProductos.keys():
            if normalizar(producto) == productoSeleccionado:
                encontrado = producto
                break

        if encontrado:
            carrito.append(encontrado)
            print(f"Producto '{encontrado}' agregado al carrito.")
        else:
            print("Producto no encontrado, inténtalo nuevamente.")

    return carrito