# Define un diccionario para un inventario de productos. 
# La clave será el nombre del producto 
# y el valor será otro diccionario con su "precio" y "stock" (cantidad disponible).

claveProducto = {}

def inventarioTienda(precio, stock):
    if precio > 0 and stock >= 0:
        return {"precio": precio, "stock": stock}
    else:
        print("El precio debe ser mayor a 0 y/o el stock no puede ser negativo.")
        return None
    
while True:
    print("Bienvenido a tu inventario de tienda. Ingresa el nombre del producto (o 'salir' para salir del inventario):")
    nombreProducto = input().strip()
    if nombreProducto.lower() == 'salir':
        print("Saliendo del inventario. Nos vemos pronto!")
        break
    elif not nombreProducto:
        print("No se ingresó ningún nombre de producto, inténtalo nuevamente")
        continue
    
    try:
        precioProducto = float(input(f"Ingresa el precio del producto '{nombreProducto}': ").replace(',', '.'))
        stockProducto = int(input(f"Ingresa el stock del producto '{nombreProducto}': "))
        
        producto = inventarioTienda(precioProducto, stockProducto)
        if producto:
            claveProducto[nombreProducto] = producto
            print(f"Producto '{nombreProducto}' añadido/actualizado exitosamente.")
            print("Inventario actual:")
            for producto, detalles in claveProducto.items():
                print(f"  {producto}: Precio = {detalles['precio']}, Stock = {detalles['stock']}")
    except ValueError:
        print("Entrada inválida. Asegúrate de ingresar un número válido para el precio y un número entero para el stock.")

    