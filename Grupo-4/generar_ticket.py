# 020 Al finalizar la compra, muestra un resumen detallado 
# que incluya los productos comprados, el subtotal, 
# el descuento aplicado (si corresponde) y el total final a pagar.

from calcular_subtotal import calcularSubtotal
from aplicar_descuentos import aplicarDescuento

def generarTicket(carrito):
    subtotal = calcularSubtotal(carrito)
    total, descuento = aplicarDescuento(subtotal)

    print("\n----- Ticket de la Compra -----")
    print("Productos comprados:")
    for producto in carrito:
        print(f"  - {producto}")
    print(f"Subtotal: ${subtotal:.2f}")
    if descuento > 0:
        print(f"Descuento aplicado: -${descuento:.2f}")
    print(f"Total a pagar: ${total:.2f}")
    print("-------------------------------\n")
    print("¡Gracias por tu compra!")