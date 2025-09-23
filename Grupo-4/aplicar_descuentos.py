# 019 Modifica el programa para que aplique 
# un descuento del 10% si el subtotal de la compra 
# supera un monto determinado (por ejemplo, $9990).

def aplicarDescuento(subtotal, monto_descuento=9990, porcentaje_descuento=0.10):
    if subtotal > monto_descuento:
        descuento = subtotal * porcentaje_descuento # calcula el descuento
        total_conDescuento = subtotal - descuento # aplica el descuento al subtotal
        return total_conDescuento, descuento
    else:
        return subtotal, 0 # no aplica descuento