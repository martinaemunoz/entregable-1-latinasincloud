from agregar_carrito import agregarCarrito
from generar_ticket import generarTicket

def main():
    print("¡Bienvenido a tu mercadito en línea!")
    carrito = agregarCarrito()
    if carrito:
        generarTicket(carrito)
    else:
        print("No se han agregado productos al carrito. Gracias por visitarnos.")


if __name__ == "__main__":
    main()