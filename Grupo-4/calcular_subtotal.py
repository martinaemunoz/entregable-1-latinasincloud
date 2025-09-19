# 018 Crea una función que reciba el carrito de compras 
# y el catálogo de productos, y calcule el costo total
# de la compra sin aplicar impuestos ni descuentos.

from definir_productos import claveProductos

def calcularSubtotal(carrito):
    subtotal = 0
    for producto in carrito:
        # agregar a claveProductos
            subtotal += claveProductos[producto]
    return subtotal

